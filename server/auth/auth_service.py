# המחלקה אחראית על כל הפעולות הקשורות למשתמשים:

# הרשמת משתמש חדש.
# התחברות.
# בדיקה האם המשתמש כבר קיים.
# טעינת נתוני המשתמש.

# היא לא פונה ישירות ל־TCP Server, אלא עובדת מול ה־Database ומפרסמת תוצאות ל־MessageBus.

from server.auth.user import User


class AuthService:
    """
    Handles user registration
    and login operations.
    """

    # Initialize authentication service.
    def __init__(self, database):

        self.database = database


    # Register a new user.
    def register(
        self,
        username,
        password_hash
    ):

        user = self.database.find_user(
            username
        )
        #if username exsist
        if user is not None:

            return False
        
        #add to database
        self.database.add_user(
            username,
            password_hash
        )

        return True


    # Authenticate an existing user.
    def login(
        self,
        username,
        password_hash
    ):

        user = self.database.find_user(
            username
        )

        if user is None:

            return None

        if user[2] != password_hash:

            return None

        return User(
            user[0],
            user[1],
            user[2],
            user[3]
        )