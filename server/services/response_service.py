class ResponseService:
    """
    Sends server responses back to clients.

    This class does not know:
    - authentication logic
    - game logic
    - rooms logic

    It only sends messages.
    """



    # Creates response service and subscribes to events.
    def __init__(
        self,
        bus
    ):

        self._bus = bus


        self._bus.subscribe(
            "LOGIN_SUCCESS",
            self._send_login_success
        )


        self._bus.subscribe(
            "LOGIN_FAILED",
            self._send_login_failed
        )



    # Sends successful login response.
    def _send_login_success(
        self,
        event
    ):

        connection = event.data["connection"]


        connection.send(
            {
                "type":"LOGIN_SUCCESS"
            }
        )



    # Sends failed login response.
    def _send_login_failed(
        self,
        event
    ):

        connection = event.data["connection"]


        connection.send(
            {
                "type":"LOGIN_FAILED",
                "reason":
                event.data["reason"]
            }
        )