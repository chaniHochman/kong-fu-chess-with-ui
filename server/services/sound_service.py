#מודיעה ללקוח איזה צליל לנגן
class SoundService:
    """
    Sends sound commands
    to clients.
    """


    # Initialize sound service.
    def __init__(
        self,
        bus
    ):

        self.bus = bus

        self.register_events()



    # Subscribe to sound events.
    def register_events(self):

        self.bus.subscribe(
            "MOVE_ACCEPTED",
            self.play_move_sound
        )


        self.bus.subscribe(
            "GAME_ENDED",
            self.play_end_sound
        )



    # Create move sound event.
    def play_move_sound(
        self,
        event
    ):

        sound_event = {
            "type":
            "PLAY_SOUND",

            "sound":
            "move.wav"
        }


        self.bus.publish(
            sound_event
        )



    # Create game end sound event.
    def play_end_sound(
        self,
        event
    ):

        sound_event = {

            "type":
            "PLAY_SOUND",

            "sound":
            "victory.wav"
        }


        self.bus.publish(
            sound_event
        )