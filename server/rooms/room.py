#Room מייצגת חדר משחק אחד.
# שמירת המשתמשים בחדר.
# קביעת תפקיד.
# בדיקה האם החדר מלא.
class Room:
    """
    Represents one game room.

    Stores players and viewers
    connected to the room.
    """



    def __init__(self, room_id):

        """
        Create a new room.

        Initialize empty players
        and viewers lists.
        """


        self.room_id = room_id


        self.players = []


        self.viewers = []



    def add_user(self, user):

        """
        Add a user to the room.

        First two users become players.
        Other users become viewers.
        """


        if len(self.players) < 2:

            self.players.append(user)

            return "PLAYER"


        else:

            self.viewers.append(user)

            return "VIEWER"



    def is_full(self):

        """
        Check if room already has
        two active players.
        """


        return len(self.players) == 2