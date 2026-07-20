# מחלקת Session מייצגת חיבור אחד לשרת.
# היא שומרת:
# המשתמש המחובר
# הסוקט שלו
# האם הוא מחובר
# באיזה חדר הוא נמצא

#מחלקה זו מייצגת משתמש רק בזמן שהוא מחובר 
class Session:
    """
    Represents one connected client.

    Stores temporary information
    about an online player.
    """


    # Create a new client session.
    def __init__(
        self,
        user,
        client_socket
    ):

        self.user = user

        self.client_socket = client_socket

        self.room = None

        self.game = None

        self.connected = True