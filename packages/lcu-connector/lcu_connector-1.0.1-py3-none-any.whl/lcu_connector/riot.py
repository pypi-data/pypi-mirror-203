from pathlib import Path

from psutil import WINDOWS, Process, process_iter
from requests import request

from .exceptions import ClientProcessError, MissingLockfileError


class Lockfile:
    """Class that manages the lockfile and its data.

    Attributes:
        path (str): The path of the lockfile.
        name (str): The name of the lockfile.
        pid (str): The process ID of the lockfile.
        port (str): The port of the lockfile.
        password (str): The password of the lockfile.
        protocol (str): The protocol of the lockfile.
    """

    def __init__(self, path: Path) -> None:
        """Initialize the object with the given lockfile path.

        Args:
            path: A string representing the lockfile path.
        """
        self.__path = path
        self.name: str = None
        self.pid: str = None
        self.port: str = None
        self.password: str = None
        self.protocol: str = None
        self.__setup_attr()

    def __setup_attr(self) -> None:
        """Set up attributes with the lockfile data.
        """
        if self.__path.exists():
            data = self.__path.read_text().split(':')
            self.name = data[0]
            self.pid = data[1]
            self.port = data[2]
            self.password = data[3]
            self.protocol = data[4]


class LeaguClient:
    """Class representing a League of Legends client.

    Attributes:
        __process_name (str): The name of the League client executable file.
        __process (psutil.Process): The process object representing the League client.
        __lockfile (Lockfile): The lockfile object representing the League client's lockfile.
    """

    def __init__(self) -> None:
        """Initializes a new client object and validates the League client process and lockfile.
        """
        self.__process_name = 'LeagueClient.exe' + ('.app' if not WINDOWS else '')
        self.__process = self.__get_process()
        self.__lockfile = self.__get_lockfile()

    def __get_process(self) -> Process:
        """Return the League Client process.

        Returns:
            Process: League Client process.

        Raises:
            ClientProcessError: If no process with the specified name is found.
        """
        for process in process_iter():
            if process.name() == self.__process_name:
                return process
        raise ClientProcessError()

    def __get_lockfile(self) -> Lockfile:
        """Retrieve the lockfile path from the process and return a Lockfile object.

        Returns:
            Lockfile: A Lockfile object representing the lockfile path.

        Raises:
            MissingLockfileError: If the lockfile path cannot be found.
        """
        if self.__process:
            files = self.__process.open_files()
            for file in files:
                if file.path.endswith('lockfile'):
                    return Lockfile(Path(file.path))
        raise MissingLockfileError()

    @property
    def lockfile(self) -> Lockfile:
        """Getter method for the lockfile attribute.

        Returns:
            Lockfile: The Lockfile object representing the lockfile of the current instance.
        """
        return self.__lockfile


class RiotSSL:
    def __init__(self) -> None:
        """Initialize an instance of the class with a Path object pointing to the './riotgames.pem' file
        and calls the private method '__update_path()'. This method is typically called when a new instance of the class is created.
        """
        self.__file = Path('riotgames.pem')
        self.__update_path()

    def __update_path(self) -> None:
        """Update the file path, if the file does not exist, the method retrieves the file from the specified URL
        and writes it to the file path.
        """
        if not self.__file.exists():
            res = request(
                'get',
                'https://gist.githubusercontent.com/pySiriusDev/c1ec2f6681cef67217b4875707c92b5a/raw/384e19bc32dcbfbdbd7d20fb2b744341cb209ae7/riotgames.pem'
            )
            with open(self.__file, 'w', encoding='utf-8') as file:
                file.write(res.text)

    @property
    def file(self) -> Path:
        """Returns the value of the file attribute.

        Returns:
            Path: A Path object representing the `riotgames.pem` file attribute.
        """
        return self.__file
