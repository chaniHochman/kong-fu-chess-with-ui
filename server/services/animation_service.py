#מודיעה ללקוח איזו אנימציה להפעיל
class AnimationService:
    """
    Sends animation commands
    to clients.
    """


    # Initialize animation service.
    def __init__(
        self,
        bus
    ):

        self.bus = bus

        self.register_events()



    # Subscribe to animation events.
    def register_events(self):

        self.bus.subscribe(
            "GAME_STARTED",
            self.start_animation
        )


        self.bus.subscribe(
            "GAME_ENDED",
            self.end_animation
        )



    # Send start animation command.
    def start_animation(
        self,
        event
    ):

        animation_event = {

            "type":
            "START_ANIMATION",

            "animation":
            "game_start"

        }


        self.bus.publish(
            animation_event
        )



    # Send end animation command.
    def end_animation(
        self,
        event
    ):

        animation_event = {

            "type":
            "END_ANIMATION",

            "animation":
            "victory"

        }


        self.bus.publish(
            animation_event
        )