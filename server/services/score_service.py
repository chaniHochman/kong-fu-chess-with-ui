#מעדכנת דירוג ELO
#לעבור על קובץ זה ולחשב בצורה נכונה
class ScoreService:
    """
    Calculates and updates ELO ratings.
    """


    # Initialize score service.
    def __init__(
        self,
        bus,
        database
    ):

        self.bus = bus

        self.database = database

        self.register_events()



    # Subscribe to game end event.
    def register_events(self):

        self.bus.subscribe(
            "GAME_ENDED",
            self.update_rating
        )



    # Update player ratings after game.
    def update_rating(
        self,
        event
    ):

        winner = event.payload["winner"]

        loser = event.payload["loser"]


        winner_rating = (
            self.database.get_rating(
                winner
            )
        )


        loser_rating = (
            self.database.get_rating(
                loser
            )
        )


        new_winner = self.calculate_elo(
            winner_rating,
            loser_rating,
            True
        )


        new_loser = self.calculate_elo(
            loser_rating,
            winner_rating,
            False
        )


        self.database.update_rating(
            winner,
            new_winner
        )


        self.database.update_rating(
            loser,
            new_loser
        )



    # Calculate new ELO rating.
    def calculate_elo(
        self,
        player_rating,
        opponent_rating,
        win
    ):

        expected = (
            1 /
            (
                1 +
                10 **
                (
                    (opponent_rating -
                    player_rating)
                    /
                    400
                )
            )
        )


        result = 1 if win else 0


        new_rating = (
            player_rating
            +
            32 *
            (
                result -
                expected
            )
        )


        return int(new_rating)