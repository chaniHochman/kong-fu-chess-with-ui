# מנהלת את כל ה־Sessions הפעילים.


class SessionManager:
    """
    Manages all connected client sessions.
    """


    # Initialize session storage.
    def __init__(self):

        self.sessions = {}

    # Add a new session.
    def add_session(
        self,
        session
    ):

        username = (
            session.user.username
        )

        self.sessions[
            username
        ] = session

    # Find session by username.
    def get_session(
        self,
        username
    ):

        return self.sessions.get(
            username
        )

    # Remove disconnected session.
    def remove_session(
        self,
        username
    ):

        if username in self.sessions:

            del self.sessions[
                username
            ]

    # Return all active sessions.
    def get_all_sessions(
        self
    ):

        return list(
            self.sessions.values()
        )