# שמירת מצב משחק אחד.
# חיבור שחקנים למשחק.
# קבלת מהלכים.
# הפעלת GameEngine.
# שליחת עדכון מצב.

# היא לא אחראית על תקשורת רשת.

class GameSession:
    """
    Represents one active chess game.

    Holds the game state
    and communicates with GameEngine.
    """



    def __init__(self, game_engine):

        """
        Initialize game session.

        Store the GameEngine
        responsible for game rules.
        """


        self.game_engine = game_engine


        self.players = []



        self.status = "active"



    def add_player(self, player):

        """
        Add player to the game.

        First player gets white.
        Second player gets black.
        """


        if len(self.players) == 0:

            player.color = "white"


        elif len(self.players) == 1:

            player.color = "black"


        else:

            player.role = PlayerRole.VIEWER



        self.players.append(player)



    def handle_move(self, move):

        """
        Send a move request
        to GameEngine.

        Returns the move result.
        """


        result = (
            self.game_engine.request_move(
                move.source,
                move.target
            )
        )


        return result
    
    
    def can_move(self, player):
        """
        Check if player is allowed
        to make a move.
        """

        return player.role != PlayerRole.VIEWER