import time
from base_camera import BaseCamera


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(f'./static/images/mario/mario{f}.jpg', 'rb').read() for f in range(1, 13)]

    @staticmethod
    def frames():

        
        while True:
            print('sending image')
            time.sleep(0.1)
            yield Camera.imgs[int(time.time()) % 12]
