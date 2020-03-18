import threading, time

class ThreadCamera():

    def __init__(self):
        self.frame = None
        self.thread = None
        self.run = True


    def start_camera_thread(self, stream):
        thread = threading.Thread(target=self.camera_thread, args=(stream,), daemon=True)
        self.thread = thread
        self.run = True

        thread.start()


    def stop_camera_thread(self):
        self.run = False
        self.thread.join()


    def camera_thread(self, stream):
        
        while self.run:
            if stream != None:
                self.frame = stream.frame

            time.sleep(1/30)

    
    def get_frame(self):
        return self.frame