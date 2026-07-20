#המחלקה מייצגת אירוע פנימי שעובר בתוך השרת.
class EventType:
    """
    Contains all internal server event types.
    """

    PLAYER_CONNECTED = (
        "PLAYER_CONNECTED"
    )

    PLAYER_DISCONNECTED = (
        "PLAYER_DISCONNECTED"
    )

    LOGIN_SUCCESS = (
        "LOGIN_SUCCESS"
    )

    LOGIN_FAILED = (
        "LOGIN_FAILED"
    )

    GAME_STARTED = (
        "GAME_STARTED"
    )

    GAME_ENDED = (
        "GAME_ENDED"
    )

    MOVE_REQUESTED = (
        "MOVE_REQUESTED"
    )

    MOVE_ACCEPTED = (
        "MOVE_ACCEPTED"
    )

    MOVE_REJECTED = (
        "MOVE_REJECTED"
    )

    BOARD_UPDATED = (
        "BOARD_UPDATED"
    )

    PLAY_SOUND = (
        "PLAY_SOUND"
    )

    START_ANIMATION = (
        "START_ANIMATION"
    )

    END_ANIMATION = (
        "END_ANIMATION"
    )

    ROOM_CREATED = "ROOM_CREATED"


    PLAYER_JOINED_ROOM = "PLAYER_JOINED_ROOM"


    PLAYER_LEFT_ROOM = "PLAYER_LEFT_ROOM"


    ROOM_REMOVED = "ROOM_REMOVED"