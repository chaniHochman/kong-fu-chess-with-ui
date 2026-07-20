# SQLite אחראית לכל העבודה מול 

# save_user()— שמירת משתמש חדש.
# get_user()— חיפוש משתמש.
# get_rating()— קבלת דירוג.
# update_rating()— עדכון דירוג.
import sqlite3



class Database:
    """
    Handles SQLite database operations.
    """


    # Initialize database connection.
    def __init__(
        self,
        filename="game.db"
    ):

        self.connection = sqlite3.connect(
            filename
        )

        self.create_tables()



    # Create database tables.
    def create_tables(self):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY,

                username TEXT UNIQUE,

                password_hash TEXT,

                rating INTEGER
            )
            """
        )


        self.connection.commit()

    # Insert a new user into the database.
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
                password_hash,
                rating
            )
        #מכניס את הערכים שאח"כ במקום הסימני שאלה
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,

            (
                username,
                password_hash,
                1200
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
            SELECT *

            FROM users

            WHERE username = ?
            """,

            (username,)
        )

        return cursor.fetchone()
    

    # Get current player rating.
    def get_rating(
        self,
        username
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            SELECT rating

            FROM users

            WHERE username = ?
            """,
            (
                username,
            )
        )


        row = cursor.fetchone()


        if row:

            return row[0]


        return None



    # Update player rating.
    def update_rating(
        self,
        username,
        new_rating
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            UPDATE users

            SET rating = ?

            WHERE username = ?
            """,
            (
                new_rating,
                username
            )
        )


        self.connection.commit()