from base64 import b64encode
from typing import Dict, Optional

from .connection import Connection
from .riot import LeaguClient


class BaseConnector():
    """Base class that stores the attributes for the `Connector`.

    Attributes:
        __pid (str): The private ID of the connector.
        __url (str): The private URL of the connector.
        __auth (str): The private authentication key of the connector.
        __headers (Dict): The private headers of the connector.
    """

    def __init__(self) -> None:
        """Defines the attributes of the `BaseConnector` class.
        """
        self.__pid: str = ''
        self.__url: str = ''
        self.__auth: str = ''
        self.__headers: Dict = {}

    @property
    def pid(self) -> str:
        """Getter for the pid attribute.

        Returns:
            str: The value of the pid attribute.
        """
        return self.__pid

    @pid.setter
    def pid(self, pid: str) -> None:
        """Setter for the pid attribute.

        Args:
            pid (str): The value to set for the pid attribute.
        """
        self.__pid = pid

    @property
    def url(self) -> str:
        """Getter for the url attribute.

        Returns:
            str: The value of the url attribute.
        """
        return self.__url

    @url.setter
    def url(self, url: str) -> None:
        """Setter for the url attribute.

        Args:
            url (str): The value to set for the url attribute.
        """
        self.__url = url

    @property
    def auth(self) -> str:
        """Getter method for the auth property.

        Returns:
            str: The value of the auth property.
        """
        return self.__auth

    @auth.setter
    def auth(self, auth: str) -> None:
        """Setter method for the auth property.

        Args:
            auth (str): The value to set the auth property to.
        """
        self.__auth = auth

    @property
    def headers(self) -> Dict:
        """Getter method for the headers property.

        Returns:
            Dict: The value of the headers property.
        """
        return self.__headers

    @headers.setter
    def headers(self, headers: Dict) -> None:
        """Setter method for the headers property.

        Args:
            headers (Dict): The value to set the headers property to.
        """
        self.__headers = headers


class Connector(Connection, BaseConnector):
    """Represents a connector for a Riot Games client.

    Inherits from:
        BaseConnector
        Connection

    Attributes:
        pid (int): The process ID of the client.
        url (str): The URL of the client connection.
        auth (str): The authorization for the client connection.
        headers (dict): The headers for the client connection.
    """

    def __init__(self, start: Optional[bool] = False) -> None:
        """Initializes a new instance of the `Connector`, and initiates the connection
        if the class be instantiated with `True` being passed as a `start` parameter.

        Args:
            start (bool, optional): Whether to start the instance. Defaults to False.
        """
        super().__init__()
        self.__setup_attr()
        if start:
            self.start()

    def __setup_attr(self) -> None:
        """Set up attributes for the `Connector` instance.
        """
        client = LeaguClient()
        lockfile = client.lockfile

        self.pid = lockfile.pid
        self.url = f'{lockfile.protocol}://127.0.0.1:{lockfile.port}'
        self.auth = b64encode(f'riot:{lockfile.password}'.encode('ascii')).decode('ascii')
        self.headers = {
            "host": f'127.0.0.1:{lockfile.port}',
            "Authorization": f'Basic {self.auth}',
            "Accept": 'application/json'
        }
