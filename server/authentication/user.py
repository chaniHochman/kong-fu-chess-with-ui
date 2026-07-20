#שומרת נתוני משתמש

class User:
    """
    Represents one registered player.
    """

    # Create a new user object.
    def __init__(
        self,
        username,
        password_hash,
        rating=1200
    ):

        

        self.username = username

        self.password_hash = password_hash

        self.rating = rating