#מחלקת Database אחראית לכל העבודה מול SQLite.
import sqlite3


class Database:
    """
    Handles all database operations.
    """

    # Open database connection.
    def __init__(self, database_path):

        self.connection = sqlite3.connect(
            database_path
        )

        self.create_tables()


    # Create database tables if they do not exist.
    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT UNIQUE,

                password_hash TEXT,

                rating INTEGER
            )
            """
        )

        self.connection.commit()


    # Insert a new user into the database.
    def add_user(
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
    def find_user(
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