#RoomManager מנהל את כל החדרים בשרת.

import random
import string



from server.rooms.room import Room




class RoomManager:
    """
    Manages all active rooms
    in the server.
    """



    def __init__(self):

        """
        Initialize empty rooms collection.
        """


        self.rooms = {}



    def create_room(self):

        """
        Create a new room
        with unique ID.
        """


        room_id = (
            self.generate_room_id()
        )

        room = Room(room_id)

        self.rooms[room_id] = room

        return room



    def generate_room_id(self):

        """
        Generate random room identifier.
        """

        chars = (
            string.ascii_uppercase
        )

        return "".join(

            random.choice(chars)

            for _ in range(6)

        )

    def join_room(self, room_id, user):

        """
        Add user to existing room.
        """
        room = self.rooms.get(
            room_id
        )

        if room is None:

            return None

        role = room.add_user(
            user
        )

        return role