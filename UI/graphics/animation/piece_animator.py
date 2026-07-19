#PieceAnimator – ניהול מצב האנימציה של כל כלי ובחירת הפריים המתאים.
#היכן נמצא הכלי מבחינה גרפית עכשיו?

class PieceAnimator:
    """
    Controls visual movement of pieces.
    """
    def __init__(self):

        self._motions = {}
        self._time = 0

    def start_motion(
            self,
            piece_id,
            start_x,
            start_y,
            end_x,
            end_y,
            duration_ms
    ):
        """
        Starts a visual movement.
        """


        self._motions[piece_id] = {

            "start_x": start_x,
            "start_y": start_y,

            "end_x": end_x,
            "end_y": end_y,

            "duration": duration_ms,

            "elapsed": 0
        }



    def update(self, dt_ms):
        """
        Advances animation time.
        """
        finished = []
        self._time += dt_ms

        for piece_id, motion in self._motions.items():

            motion["elapsed"] += dt_ms


            if motion["elapsed"] >= motion["duration"]:

                finished.append(piece_id)



        for piece_id in finished:

            del self._motions[piece_id]



    def get_position(
            self,
            piece_id
    ):
        """
        Returns current pixel position.
        """

        motion = self._motions.get(piece_id)

        if motion is None:
            return None


        #כמה אחוז מהתנועה כבר עבר
        progress = (
            motion["elapsed"]
            /
            motion["duration"]
        )

        x = (
            motion["start_x"]
            +
            (
                motion["end_x"]
                -
                motion["start_x"]
            )
            *
            progress
        )


        y = (
            motion["start_y"]
            +
            (
                motion["end_y"]
                -
                motion["start_y"]
            )
            *
            progress
        )


        return (
            int(x),
            int(y)
        )
    ############33
    # Returns the index of the current frame for a piece's animation based on elapsed time and frames per second.
    def get_frame_index(self, piece_id, frames_count, fps,loop):

        motion = self._motions.get(piece_id)

        if motion is None:
            frame_time = 1000 / fps

            index = int(self._time / frame_time)

            if loop:
                return index % frames_count

            return min(index, frames_count - 1)

#no divid with zero
        if fps <= 0:
            return 0
        
        frame_time = 1000 / fps


        index = int(
            motion["elapsed"] / frame_time
        )
        if loop:
            return index % frames_count

        return min(index, frames_count - 1)