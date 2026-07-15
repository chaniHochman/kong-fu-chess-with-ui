import cv2

#הפיכת תמונה בלי שקיפות לתמונה עם שקיפות
def ensure_alpha(img):
    """
    Ensures that an OpenCV image has an alpha channel.

    BGR  -> BGRA
    BGRA -> unchanged
    """

    if img is None:
        raise ValueError("Image cannot be None")


    # תמונה ללא שקיפות
    if len(img.shape) == 3:

        channels = img.shape[2]

        if channels == 3:
            return cv2.cvtColor(
                img,
                cv2.COLOR_BGR2BGRA
            )


    # כבר יש שקיפות
    return img