# יצירת משחק חדש.
# מציאת משחק קיים.
# הוספת שחקנים.
# ניהול כמה משחקים במקביל.

from server.game.server_game import GameSession

class GameManager:
    """
    Controls all active games
    running on the server.
    """

    def __init__(self):

        """
        Initialize empty game list.
        """

        self.games = []



    def create_game(self, game_engine):

        """
        Create a new game session.

        Returns the new game.
        """


        game = GameSession(
            game_engine
        )


        self.games.append(game)


        return game



    def find_available_game(self):

        """
        Search for a game
        that has only one player.

        Returns None if no game exists.
        """


        for game in self.games:


            if len(game.players) == 1:

                return game



        return None



    def join_game(self, player, game_engine):

        """
        Add a player to an existing game.

        If no game exists,
        create a new one.
        """


        game = (
            self.find_available_game()
        )


        if game is None:


            game = self.create_game(
                game_engine
            )



        game.add_player(player)


        return game
    
    from game.server_game import ServerGame

from bus.event import Event

from bus.event_type import EventType



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

        game = ServerGame(
            room,
            game_engine
        )


        self.games[
            room.room_id
        ] = game



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