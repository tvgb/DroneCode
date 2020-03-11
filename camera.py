import time
from base_camera import BaseCamera


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = open('./image/test_image.jpg', 'rb').read()

    @staticmethod
    def frames():

        while True:
            time.sleep(1/30)
            yield Camera.imgs
