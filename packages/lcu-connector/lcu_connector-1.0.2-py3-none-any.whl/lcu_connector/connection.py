import json
from typing import Dict, Optional

from requests import Response, Session

from .exceptions import SessionError
from .riot import RiotSSL


class Connection:
    """Represents a connection object that allows for sending requests to the Riot API.

    Attributes:
        __session (Session]): A session object for sending HTTP requests.
        __riotSSL (RiotSSL): An SSL object for handling Riot SSL certificate.
        __ssl (Path): The path to the SSL certificate file.
    """

    def __init__(self) -> None:
        """Initializes the Connection object.
        """
        self.__session: Optional[Session] = None
        self.__riotSSL = RiotSSL()
        self.__ssl = self.__riotSSL.file

    def start(self) -> None:
        """Starts a new session with the provided headers and SSL verification.
        """
        self.__session = Session()
        self.__session.headers = self.headers
        self.__session.verify = self.__ssl

    def stop(self):
        """Closes the session if it exists and sets it to None.

        Raises:
            SessionError: If there is no active session.
        """
        if self.__session is not None:
            self.__session.close()
            self.__session = None

    def __check_session(self):
        """Checks if there is an active session. Raises a SessionError if not.
        """
        if self.__session is None:
            raise SessionError()

    def __new_url(self, api_url: str) -> str:
        """Returns a new URL by appending the given API URL to the instance URL.

        Args:
            api_url (str): The API URL to append to the instance URL.

        Returns:
            str: The new URL formed by appending the API URL to the instance URL.
        """
        return self.url + api_url

    def get(self, api_url: str) -> Response:
        """Sends a GET request to the specified API URL and returns the response.

        Args:
            api_url (str): The URL of the API to send the request to.

        Returns:
            Response: The response object from the GET request.
        """
        self.__check_session()
        return self.__session.get(self.__new_url(api_url))

    def post(self, api_url: str, data: Dict) -> Response:
        """Sends a POST request with the given data to the specified API URL using the active session.

        Args:
            api_url (str): The URL of the API to send the request to.
            data (Dict): The data to send with the POST request.

        Returns:
            Response: The response object containing the server's response to the request.
        """
        self.__check_session()
        return self.__session.post(self.__new_url(api_url), data=json.dumps(data))

    def put(self, api_url: str, data: Dict) -> Response:
        """Sends a PUT request with the given data to the specified API URL using the active session.

        Args:
            api_url (str): The URL of the API endpoint.
            data (Dict): The data to be sent in the request.

        Returns:
            Response: The response object from the request.
        """
        self.__check_session()
        return self.__session.put(self.__new_url(api_url), data=json.dumps(data))

    def delete(self, api_url: str) -> Response:
        """Sends a DELETE request to the specified API URL using the active session.

        Args:
            api_url (str): The URL of the API endpoint to delete.

        Returns:
            Response: The response object from the DELETE request.
        """
        self.__check_session()
        return self.__session.delete(self.__new_url(api_url))

    @property
    def connected(self) -> bool:
        """Checks if the connection is established.

        Returns:
            bool: Returns True if the connection is established, otherwise False.
        """
        pid = self.pid is not None
        ssl = self.__ssl.exists()
        session = self.__session is not None
        return bool(pid and ssl and session)
