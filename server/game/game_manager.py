#אחראי על ניהול משחקים פעילים
# יצירת משחק חדש.
# מציאת משחק קיים.
# הוספת שחקנים.
# ניהול כמה משחקים במקביל.

from game.server_game import ServerGame

from bus.event import Event

from bus.event_type import EventType

from game.game_session import GameSession

class GameManager:
    """
    Manages all active games.
    """
    
    # Initialize game manager.
    def __init__(
        self,
        bus
    ):

        self.bus = bus

        self.games = {}

    # Create game from ready room.
    def create_game(
        self,
        room,
        game_engine
    ):

        server_game = ServerGame(
            room,
            game_engine
        )


        game_session = GameSession(
            room,
            server_game,
            self.bus
        )

        self.games[
            room.room_id
        ] = game_session

        self.bus.publish(

            Event(

                EventType.GAME_STARTED,

                {
                    "room_id":
                    room.room_id
                }

            )

        )
        return game

    # Find game by room id.
    def get_game(
        self,
        room_id
    ):

        return self.games.get(
            room_id
        )

    # Handle player move.
    def handle_move(
        self,
        room_id,
        move
    ):

        game = self.get_game(
            room_id
        )

        if game is None:

            return None

        result = game.make_move(
            move
        )

        if result.success:

            self.bus.publish(

                Event(

                    EventType.MOVE_ACCEPTED,

                    {
                        "move":
                        move
                    }

                )

            )

        else:

            self.bus.publish(

                Event(

                    EventType.MOVE_REJECTED,

                    {
                        "move":
                        move
                    }
                )
            )

        return result