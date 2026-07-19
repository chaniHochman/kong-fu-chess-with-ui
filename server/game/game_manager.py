# יצירת משחק חדש.
# מציאת משחק קיים.
# הוספת שחקנים.
# ניהול כמה משחקים במקביל.

from server.game.game_session import GameSession



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