import threading, time

class ThreadCamera():

    def __init__(self):
        self.frame = None
        self.thread = None


    def start_camera_thread(self, stream):
        thread = threading.Thread(target=self.camera_thread, args=(stream,), daemon=True)
        thread.start()


    def stop_camera_thread(self):
        self.thread.join()


    def camera_thread(self, stream):
        
        while True:
            if stream != None:
                self.frame = stream.frame
                time.sleep(1)

    
    def get_frame(self):
        return self.frame