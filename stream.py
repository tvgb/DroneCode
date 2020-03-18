import tempfile, os, csv, cv2
import olympe
from pathlib import Path


class Stream:
    def __init__(self, drone):
        self.drone = drone
    
        self.tempd = tempfile.mkdtemp(prefix="olympe_streaming_test_")
        print("Olympe streaming example output dir: {}".format(self.tempd))

        self.h264_frame_stats = []
        self.h264_stats_file = open(os.path.join(self.tempd, 'h264_stats.csv'), 'w+')
        self.h264_stats_writer = csv.DictWriter(self.h264_stats_file, ['fps', 'bitrate'])
        self.h264_stats_writer.writeheader()

        self.dirname = 'image'
        Path(self.dirname).mkdir(parents=True, exist_ok=True)

        self.frame = None

    def start(self):
        
        self.drone.set_streaming_output_files(
            h264_data_file=os.path.join(self.tempd, 'h264_data.264'),
            h264_meta_file=os.path.join(self.tempd, 'h264_metadata.json'),
            # Here, we don't record the (huge) raw YUV video stream
            # raw_data_file=os.path.join(self.tempd,'raw_data.bin'),
            # raw_meta_file=os.path.join(self.tempd,'raw_metadata.json'),
        )

        # Setup your callback functions to do some live video processing
        self.drone.set_streaming_callbacks(
            raw_cb=self.yuv_frame_cb #,
            #h264_cb=self.h264_frame_cb
        )

        # Start video streaming
        self.drone.start_video_streaming()

    
    def stop(self):
        # Properly stop the video stream and disconnect
        self.drone.stop_video_streaming()
        # self.drone.disconnection()
        self.h264_stats_file.close()

    def yuv_frame_cb(self, yuv_frame):
        """
        This function will be called by Olympe for each decoded YUV frame.
            :type yuv_frame: olympe.VideoFrame
        """
        
        # the VideoFrame.info() dictionary contains some useful informations
        # such as the video resolution
        info = yuv_frame.info()
        height, width = info["yuv"]["height"], info["yuv"]["width"]

        # convert pdraw YUV flag to OpenCV YUV flag
        cv2_cvt_color_flag = {
            olympe.PDRAW_YUV_FORMAT_I420: cv2.COLOR_YUV2BGR_I420,
            olympe.PDRAW_YUV_FORMAT_NV12: cv2.COLOR_YUV2BGR_NV12,
        }[info["yuv"]["format"]]

        # yuv_frame.as_ndarray() is a 2D numpy array with the proper "shape"
        # i.e (3 * height / 2, width) because it's a YUV I420 or NV12 frame

        # Use OpenCV to convert the yuv frame to RGB
        cv2frame = cv2.cvtColor(yuv_frame.as_ndarray(), cv2_cvt_color_flag)
        self.frame = cv2frame

        # status = cv2.imwrite(os.path.join(self.dirname, 'test_image.jpg'), cv2frame)
        
        # Use OpenCV to show this frame
        # cv2.imshow("Olympe Streaming Example", cv2frame)
        # cv2.waitKey(1)  # please OpenCV for 1 ms...

    def get_latest_frame(self):
        return self.frame