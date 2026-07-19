#שומרת נתוני משתמש

class User:
    """
    Represents one registered player.
    """

    # Create a new user object.
    def __init__(
        self,
        user_id,
        username,
        password_hash,
        rating=1200
    ):

        self.user_id = user_id

        self.username = username

        self.password_hash = password_hash

        self.rating = rating