from time import time

class Camera(object):
    def __init__(self):
        self.frames = [open(f'./static/images/mario/mario{f}.jpg', 'rb').read() for f in range(1, 13)]

    def get_frame(self):
        return self.frames[int(time()) % 12]