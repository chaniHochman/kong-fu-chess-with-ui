# from __future__ import annotations

# import pathlib
import cv2
class mouse:
    def __init__(self):
        self.img = None
        
    def show_image_with_mouse_callback(self, img):
        #OpenCV מבקש ממערכת ההפעלה ליצור חלון בשם "Image".
        cv2.imshow("Image", img.img)
        #צריך לומר ל־OpenCV מי יטפל בעכבר
        cv2.setMouseCallback("Image", self.mouse_callback)#mouse_callback-שם של פונקציה



    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_RBUTTONDOWN:
            print(f"Right button clicked at ({x}, {y})")
