# פתיחת SQLite.
# יצירת טבלאות.
# ביצוע שאילתות.

import sqlite3



class Database:
    """
    Manages SQLite database connection.
    """



    def __init__(self, path):

        """
        Open database connection.
        """

        self.connection = sqlite3.connect(path)



    def create_tables(self):

        """
        Create all required tables.
        """


        cursor = self.connection.cursor()


        cursor.execute("""

        CREATE TABLE IF NOT EXISTS users
        (
        id INTEGER PRIMARY KEY,

        username TEXT UNIQUE,

        password_hash TEXT,

        rating INTEGER DEFAULT 1200
        )

        """)


        self.connection.commit()