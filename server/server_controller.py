# לקרוא הודעות מה־MessageBus.
# לשלוח אותן ל־GameManager.
# לחבר בין שכבת הרשת לבין שכבת המשחק.

# היא לא מכירה חוקי שחמט.
# היא רק מתאמת.

from server.game.game_manager import GameManager



class ServerController:
    """
    Coordinates communication between
    network layer and game layer.
    """


    def __init__(self, bus, game_manager):

        """
        Initialize controller.

        Receives the MessageBus
        and GameManager instances.
        """

        self.bus = bus

        self.game_manager = game_manager



    def run(self):

        """
        Start processing events
        from the MessageBus.
        """

        while True:

            event = self.bus.consume()

            if event is not None:

                self.handle_event(event)



    def handle_event(self, event):

        """
        Analyze incoming events
        and send them to the correct handler.
        """


        if event["type"] == "JOIN":


            self.handle_join(event)


        elif event["type"] == "MOVE":

            self.handle_move(event)


    def handle_join(self, event):

        """
        Handle a new player request.

        Creates or joins a game.
        """

        player = event["data"]


        game = (
            self.game_manager.join_game(
                player,
                None
            )
        )

        print(
            "Player joined:",
            player
        )

    def handle_move(self, event):

        """
        Handle a chess move.

        Sends the move
        to the correct game session.
        """

        game = event["game"]


        result = (
            game.process_event(event)
        )

        return result