# ftp2sftp.py - A FTP to SFTP bridge
# Copyright (C) 2023  Sebastian Meyer <sparrow.242.de@gmail.com>
# You should have received a copy of the GNU General Public License V3
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import logging
import paramiko
import pathlib

from collections import namedtuple
from datetime import datetime as DateTime
from datetime import timezone
from logging.handlers import TimedRotatingFileHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from stat import S_ISDIR

from ftp2sftp.__about__ import version

Address = namedtuple("Address", ("host", "port", "username", "password", "path"))


def connect_sftp(host, port, username, password):
    """Connect a SFTP server, returns (transport, SFTP-Client)
    
    This functions connects to a SFTP Server and returs a tuple with
    a paramiko/SSH-transport object and an SFTP-Client object.

    Parameters
    ----------
    host : str
        The hostname or IP of the SFTP server
    port : int
        The SFTP server's port
    username : str
        username to log into the SFTP server
    password : str
        password to log into the SFTP server


    Returns
    -------
    tuple
        first element: paramiko.transport.Transport
        second element: paramiko.sftp_client.SFTPClient
    """

    logging.info(f"Try to connect SFTP: {host}:{port} as user '{username}'")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username, password)
    sftp_client = paramiko.SFTPClient.from_transport(transport)
    return (transport, sftp_client)


class Authorizer(DummyAuthorizer):
    """ Subclass of the dummy example to have the option to
    manage users without a local directory on the filesystem"""

    def add_user(
        self, username, password, homedir, perm='elr',
        msg_login="Login successful.", msg_quit="Goodbye."
    ):
        """Add a user to the virtual users table.

        We overwrite the function because we don't need a homedir
        on the local filesystem.
        """
        if self.has_user(username):
            raise ValueError('user %r already exists' % username)
        self._check_permissions(username, perm)
        self.user_table[username] = {
            'pwd': str(password),
            'perm': perm,
            'operms': {},
            'msg_login': str(msg_login),
            'msg_quit': str(msg_quit),
            'home': homedir
        }


class FTP2SFTPHandler(FTPHandler):

    # this parameter has to be set from outside before the
    # initialization through the server.
    # This kind of monkey patching is more stable than also
    # subclassing the server only to pass this information.
    sftp_config = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def handle_close(self):
        logging.debug(f"call handle_close")
        self.fs.close_sftp_connection()
        super().handle_close()


class SFTPConnectedFS():
    
    def __init__(self, home, handler):
        self.handler = handler
        self._root = home
        logging.info(f"Home directory for the FTP user: {self._root}")
        self._cwd = self._root
        self._sftp_root = handler.sftp_config["basedir"] or "/"
        self.ssh_transport, self.sftp_client = connect_sftp(
            handler.sftp_config["host"], handler.sftp_config["port"],
            handler.sftp_config["username"], handler.sftp_config["password"]
        )

    def chdir(self, path):
        new_path = path
        logging.debug(f"call chdir : {path} -> {new_path}")
        self.sftp_client.chdir(new_path)
        self.cwd = self.fs2ftp(new_path)

    def close_sftp_connection(self):
        logging.debug(f"call close_sftp_connection")
        self.ssh_transport.close()

    @property
    def cwd(self):
        logging.debug(f"call cwd : -> {self._cwd}")
        return self._cwd

    @cwd.setter
    def cwd(self, path):
        # We need a little workaround here to resolve posix files (for the
        # SFTP server) on a not posix system. We use pathlib and cut of the
        # drive letter if it appears.
        new_cwd_path = pathlib.Path(path).resolve()
        new_cwd = new_cwd_path.as_posix()
        if new_cwd.startswith(new_cwd_path.drive):
            new_cwd = new_cwd[len(new_cwd_path.drive):]
        logging.debug(f"call set cwd : {path} -> {new_cwd}")
        self._cwd = new_cwd

    def format_mlsx(self, basedir, listing, perms, facts, ignore_err=True):
        logging.debug(
            f"call format_mlsx : {basedir}, {listing}, {perms}, {facts}, {ignore_err} -> ..."
        )
        for entry in self.sftp_client.listdir_iter(basedir):
            values = []
            if "type" in facts:
                values.append(f"type=dir" if S_ISDIR(entry.st_mode) else f"type=file")
            if "perm" in facts:
                values.append("perm=r")
            if "size" in facts:
                values.append(f"size={entry.st_size}")
            if "modify" in facts:
                dt = DateTime.fromtimestamp(entry.st_mtime, tz=timezone.utc)
                ts = dt.strftime("%Y%m%d%H%M%S")
                values.append(f"modify={ts}")
            values.append(f" {entry.filename}\n")
            response = ";".join(values).encode()
            logging.debug(f" response format_mlsx : {response}")
            yield response

    def fs2ftp(self, fspath):
        if fspath.startswith("."):
            fspath = fspath[1:]
        fspath = f"{fspath[len(self._sftp_root):]}" if fspath.startswith(self._sftp_root) else fspath
        ftppath = f"{self._root.rstrip('/')}/{fspath.lstrip('/')}"
        logging.debug(f"call fs2ftp : {fspath} -> {ftppath}")
        return ftppath

    def ftp2fs(self, ftppath):
        if not ftppath.startswith("/"):
            ftppath = f"{self._cwd}/{ftppath}"
        fspath = f"{ftppath[len(self._root):]}" if ftppath.startswith(self._root) else ftppath
        fspath = f"{self._sftp_root.rstrip('/')}/{fspath.lstrip('/')}"
        logging.debug(f"call ftp2fs : {ftppath} -> {fspath}")
        return fspath

    def getmtime(self, path):
        stat = self.sftp_client.stat(path)
        mtime = stat.st_mtime
        logging.debug(f"call getmtime : {path} {mtime}")
        return mtime

    def isdir(self, path):
        is_dir = None
        try:
            stat = self.sftp_client.stat(path)
        except FileNotFoundError:
            is_dir = False
        if is_dir is None:
            is_dir = S_ISDIR(stat.st_mode)
        logging.debug(f"call isdir : {path} -> {is_dir}")
        return is_dir
    
    def isfile(self, path):
        is_file = None
        try:
            stat = self.sftp_client.stat(path)
        except FileNotFoundError:
            is_file = False
        if is_file is None:
            is_file = not S_ISDIR(stat.st_mode)
        logging.debug(f"call isfile : {path} -> {is_file}")
        return is_file

    def lexists(self, path):
        exists = True
        try:
            _ = self.sftp_client.stat(path)
        except FileNotFoundError:
            exists =  False
        logging.debug(f"call lexists : {path} -> {exists}")
        return exists

    def listdir(self, path):
        listing = self.sftp_client.listdir(path)
        logging.debug(f"call listdir : {path} -> {listing}")
        return listing
    
    def mkdir(self, path):
        logging.debug(f"call mkdir : {path}")
        self.sftp_client.mkdir(path)

    def open(self, filename, mode):
        logging.debug(f"call open : {filename}, {mode}")
        sftp_open = self.sftp_client.open(filename, mode)
        # the .name property of the handle is used by the FTP library.
        sftp_open.name = filename
        return sftp_open
    
    def realpath(self, path):
        if not path.startswith("/"):
            cwd = self._cwd[:-1] if self._cwd.endswith("/") else self._cwd
            realpath = realpath = f"{cwd}/{path}"
        else:
            realpath = path
        realpath = self.ftp2fs(realpath)
        logging.debug(f"call realpath : {path} -> {realpath}")
        return realpath

    def rename(self, src, dst):
        logging.debug(f"call rename : {src} {dst}")
        self.sftp_client.rename(src, dst)

    def remove(self, path):
        logging.debug(f"call remvoe : {path}")
        self.sftp_client.remove(path)

    def rmdir(self, path):
        logging.debug(f"call rmdir : {path}")
        self.sftp_client.rmdir(path)

    @property
    def root(self):
        logging.debug(f"call root : {self._root}")
        return self._root

    def utime(self, path, timeval):
        logging.debug(f"call utime : {path} {timeval}")
        self.sftp_client.utime(path, (timeval, timeval))

    def validpath(self, path):
        is_valid = True
        logging.debug(f"call validpath : {path} -> {is_valid}")
        return is_valid


def setup_logger(loglevel, logdir, keeplog):
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger()
    logger.setLevel(logging.getLevelName(loglevel))
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.getLevelName(loglevel))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.info(f"Logging is active on level {logging.getLevelName(logger.level)}")
    if logdir:
        logfile = logdir / "ftp2sftp_log.txt"
        handler = TimedRotatingFileHandler(
            logfile, when="d", interval=1, backupCount=keeplog,
        )
        handler.setLevel(logging.getLevelName(loglevel))
        handler.setFormatter(formatter)
        logger.addHandler(handler)


def parse_address(address):
    user_part, server_part = address.split("@")
    user, password = user_part.split(":")
    server_part_elements = server_part.split(":")
    host, port = server_part_elements[:2]
    path = server_part_elements[2] if len(server_part_elements) > 2 else None
    return Address(host, int(port), user, password, path)


def parse_arguments_options():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
    )
    parser.add_argument("--ftp", type=parse_address, required=True,
        help="Information where to start the FTP server: username:password@host:port:/homedir"
    )
    parser.add_argument("--sftp", type=parse_address, required=True,
        help="Information how to connect the SFTP server: username:password@host:port:/homedir"
    )
    parser.add_argument("--loglevel", type=str, default="INFO",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
        help="Set the loglevel for logging. (Default: INFO)"
    )
    parser.add_argument("--logdir", type=pathlib.Path, default=None,
        help="Directory to write the log. Logs will be sperated in files daily"
    )
    parser.add_argument("--keeplog", type=int, default=7,
        help="How long (in days) keep the logfile if logdir is set (Default: 7)"
    )
    args = parser.parse_args()
    return args


def main():
    print(f"ftp2sftp.py (Version {version})")
    print("Copyright (C) 2023  Sebastian Meyer <sparrow.242.de@gmail.com>")
    print("Licensed under GNU GPL (https://www.gnu.org/licenses/gpl-3.0.html)")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions.")
    options = parse_arguments_options()
    setup_logger(options.loglevel, options.logdir, options.keeplog)
    logging.info("fpt2sftp is starting...")
    authorizer = Authorizer()
    authorizer.add_user(
        options.ftp.username, options.ftp.password, perm="elradfmwMT",
        homedir = options.ftp.path or f"/home/{options.ftp.username}"
    )
    handler = FTP2SFTPHandler
    handler.authorizer = authorizer
    handler.abstracted_fs = SFTPConnectedFS
    sftp_config = {
        "host": options.sftp.host,
        "port": options.sftp.port,
        "username": options.sftp.username,
        "password": options.sftp.password,
        "basedir": options.sftp.path
    }
    handler.sftp_config = sftp_config
    server = FTPServer((options.ftp.host, options.ftp.port), handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
