#רושמת אירועים ללוג
from datetime import datetime


class LoggerService:
    """
    Handles server event logging.

    Receives events from MessageBus
    and saves them into log file.
    """


    # Initialize logger service.
    def __init__(
        self,
        bus
    ):

        self.bus = bus

        self.file_name = (
            "logs/server.log"
        )

        self.register_events()



    # Subscribe to logging events.
    def register_events(self):

        self.bus.subscribe(
            "PLAYER_CONNECTED",
            self.write_log
        )

        self.bus.subscribe(
            "PLAYER_DISCONNECTED",
            self.write_log
        )

        self.bus.subscribe(
            "MOVE_ACCEPTED",
            self.write_log
        )

        self.bus.subscribe(
            "GAME_STARTED",
            self.write_log
        )

        self.bus.subscribe(
            "GAME_ENDED",
            self.write_log
        )



    # Write event information into log file.
    def write_log(
        self,
        event
    ):

        timestamp = datetime.now()

        text = (
            f"{timestamp} "
            f"{event}\n"
        )


        with open(
            self.file_name,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(text)