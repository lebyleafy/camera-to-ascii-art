from cv2 import VideoCapture, resize, flip
import asciify

cam = VideoCapture(0)
cam.set(3, 180)
cam.set(4, 240)

while True:

    s, img = cam.read()

    if s:
        img = flip(resize(img, (200, 63)), 1)
        asciify.asciify(img)

cam.release()
