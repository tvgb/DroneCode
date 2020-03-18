import time
from base_camera import BaseCamera
from stream import 


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    # imgs = open('./image/test_image.jpg', 'rb').read()

    @staticmethod
    def frames(stream):

        while True:
            # img = open('./image/test_image.jpg', 'rb').read()
            frame = stream.get_latest_frame()
            time.sleep(1)
            yield frame
