# מנהל את כל החדרים בשרת.
# יצירת חדר חדש.
#  שמירת חדרים הפעילים.
# חיפוש חדר לפי `רroom_id.
#  הכנסת שחקן לחדר.
#  מחיקת חדר שאין בו משתמשים.
#  פרסום אירועיםMessageBus.
from room.room import Room

from bus.event import Event

from bus.event_type import EventType



class RoomManager:
    """
    Manages all active game rooms.

    Responsible for creating,
    finding, joining and removing rooms.
    """


    # Initialize room manager.
    def __init__(
        self,
        bus
    ):

        self.bus = bus

        self.rooms = {}



    # Create a new game room.
    def create_room(
        self
    ):
        room = Room()

        self.rooms[room.room_id ] = room

        self.bus.publish(
            Event(
                EventType.ROOM_CREATED,
                {
                    "room_id":
                    room.room_id
                }
            )
        )
        return room



    # Find room by room id.
    def get_room(
        self,
        room_id
    ):

        return self.rooms.get(
            room_id
        )



    # Add player session into existing room.
    def join_room(
        self,
        room_id,
        session
    ):


        room = self.get_room(
            room_id
        )


        if room is None:

            return None



        role = room.add_session(
            session
        )



        self.bus.publish(

            Event(

                EventType.PLAYER_JOINED_ROOM,

                {

                    "room_id":
                    room_id,


                    "username":
                    session.user.username,

                    #תפקיד
                    "role":
                    role

                }

            )

        )

        return role



    # Remove player from room.
    def leave_room(
        self,
        room_id,
        session
    ):

        room = self.get_room(
            room_id
        )

        if room is None:

            return

        room.remove_session(
            session
        )
        self.bus.publish(

            Event(

                EventType.PLAYER_LEFT_ROOM,

                {

                    "room_id":
                    room_id,

                    "username":
                    session.user.username

                }

            )

        )

        self.remove_empty_room(
            room
        )

    # Delete room if no users exist.
    def remove_empty_room(
        self,
        room
    ):

        if (

            room.white_player is None

            and

            room.black_player is None

            and

            len(room.viewers) == 0

        ):

            del self.rooms[
                room.room_id
            ]

            self.bus.publish(

                Event(

                    EventType.ROOM_REMOVED,

                    {
                        "room_id":
                        room.room_id
                    }

                )

            )

    # Return all active rooms.
    def get_all_rooms(
        self
    ):

        return list(
            self.rooms.values()
        )