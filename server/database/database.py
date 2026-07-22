# SQLite אחראית לכל העבודה מול 

# save_user()— שמירת משתמש חדש.
# get_user()— חיפוש משתמש.
# get_rating()— קבלת דירוג.
# update_rating()— עדכון דירוג.
import sqlite3


class Database:
    """
    Responsible only for SQLite operations.

    It knows:
    - tables
    - SQL queries
    - saving data

    It does not know:
    - users logic
    - authentication
    - games
    """



    # Open database connection.
    def __init__(
        self,
        path="game.db"
    ):

        self.connection = sqlite3.connect(
            path,
            check_same_thread=False
        )

        self.create_tables()



    # Create all database tables.
    def create_tables(self):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY,

                username TEXT UNIQUE,

                password_hash TEXT,

                rating INTEGER DEFAULT 1200
            )
            """
        )


        self.connection.commit()



    # Save a new user.
    def save_user(
        self,
        username,
        password_hash
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password_hash
            )

            VALUES
            (
                ?,
                ?
            )
            """,
            (
                username,
                password_hash
            )
        )


        self.connection.commit()



    # Find user by username.
    def get_user(
        self,
        username
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            SELECT
            id,
            username,
            password_hash,
            rating

            FROM users

            WHERE username = ?
            """,
            (
                username,
            )
        )


        return cursor.fetchone()



    # Update player rating.
    def update_rating(
        self,
        username,
        rating
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            UPDATE users

            SET rating = ?

            WHERE username = ?
            """,
            (
                rating,
                username
            )
        )


        self.connection.commit()

    def get_rating(self, username):
        """
        Return player rating.
        """

        cursor = self.connection.cursor()

        cursor.execute(

            """
            SELECT rating
            FROM users
            WHERE username = ?
            """,

            (username,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]