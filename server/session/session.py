# מחלקת Session מייצגת חיבור אחד לשרת.
# היא שומרת:
# המשתמש המחובר
# הסוקט שלו
# האם הוא מחובר
# באיזה חדר הוא נמצא


class Session:
    """
    Represents one connected client session.
    """

    # Create a new session.
    def __init__(
        self,
        client_socket
    ):

        self.client_socket = client_socket

        self.user = None

        self.room = None

        self.connected = True