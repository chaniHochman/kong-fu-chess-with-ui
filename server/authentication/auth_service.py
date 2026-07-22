# המחלקה אחראית על כל הפעולות הקשורות למשתמשים:

# הרשמת משתמש חדש.
# התחברות.
# בדיקה האם המשתמש כבר קיים.
# טעינת נתוני המשתמש.

# היא לא פונה ישירות ל־TCP Server, אלא עובדת מול ה־Database ומפרסמת תוצאות ל־MessageBus.

import hashlib

from authentication.user import User
from bus.event import Event
from bus.event_type import EventType



class AuthService:
    """
    Handles user registration
    and login operations.

    Communicates with Database
    and publishes authentication
    events through MessageBus.
    """


    # Initialize authentication service.
    def __init__(
        self,
        database,
        bus
    ):

        self.database = database

        self.bus = bus



    # Register a new user.
    def register(
        self,
        username,
        password
    ):

        existing_user = (
            self.database.get_user(
                username
            )
        )

        if existing_user:

            self.bus.publish(
                Event(
                    EventType.LOGIN_FAILED,
                    {
                        "reason":
                        "username_exists"
                    }
                )
            )

            return False



        password_hash = (
            self.hash_password(
                password
            )
        )


        self.database.save_user(
            username,
            password_hash
        )


        self.bus.publish(
            Event(
                EventType.LOGIN_SUCCESS,
                {
                    "username":
                    username
                }
            )
        )


        return True



    # Authenticate existing user.
    def login(
        self,
        username,
        password
    ):

        user = (
            self.database.get_user(
                username
            )
        )


        if not user:

            self.bus.publish(
                Event(
                    EventType.LOGIN_FAILED,
                    {
                        "reason":
                        "user_not_found"
                    }
                )
            )

            return None

        stored_hash = user[1]

        #המר סיסמה לגיבוב מאובטח
        password_hash = (
            self.hash_password(
                password 
            )
        )

        if password_hash != stored_hash:

            self.bus.publish(
                Event(
                    EventType.LOGIN_FAILED,
                    {
                        "reason":
                        "wrong_password"
                    }
                )
            )

            return None

        logged_user = User(
            user[0],
            user[1],
            user[3]
        )


        self.bus.publish(
            Event(
                EventType.LOGIN_SUCCESS,
                {
                    "username":
                    username
                }
            )
        )

        return logged_user

    # Create password hash.
    def hash_password(
        self,
        password
    ):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()