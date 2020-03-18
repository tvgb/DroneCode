import time
from base_camera import BaseCamera

class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    # imgs = open('./image/test_image.jpg', 'rb').read()

    stream = None

    @staticmethod
    def frames():

        while True:
            # img = open('./image/test_image.jpg', 'rb').read()
            if Camera.stream != None:
                frame = Camera.stream.get_latest_frame()
                time.sleep(1)
            
                yield frame

    
    @staticmethod
    def set_stream(stream):
        Camera.stream = stream
