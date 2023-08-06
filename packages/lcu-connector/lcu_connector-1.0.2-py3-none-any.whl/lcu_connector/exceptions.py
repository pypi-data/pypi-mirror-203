class SessionError(Exception):
    """An exception that is raised when the connector is not started.
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'The connector was not started, start it with Connector.start().'


class ClientProcessError(Exception):
    """Exception raised when the League Client is closed.
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'League Client is closed, please open it first before starting a connection.'


class MissingLockfileError(Exception):
    """Exception raised when the lockfile is not found.
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Lockfile not found, try closing League Client and reopening.'
