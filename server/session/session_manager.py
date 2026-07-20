# מנהלת את כל ה־Sessions הפעילים.


from server.session.session import Session


class SessionManager:
    """
    Manages connected client sessions.
    """

    # Initialize session manager.
    def __init__(self):

        self.sessions = {}

    # Create a session for a new client.
    def create_session(
        self,
        client_socket
    ):

        session = Session(
            client_socket
        )

        self.sessions[
            client_socket
        ] = session

        return session

    # Find session by client socket.
    def get_session(
        self,
        client_socket
    ):

        return self.sessions.get(
            client_socket
        )

    # Remove disconnected session.
    def remove_session(
        self,
        client_socket
    ):

        if client_socket in self.sessions:

            del self.sessions[
                client_socket
            ]