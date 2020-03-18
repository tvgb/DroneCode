import threading, time

class ThreadCamera():

    def __init__(self):
        self.frame = None
        self.thread = None
        self.run = True
        self.isRunning = False


    def start_camera_thread(self, stream):

        if not self.isRunning:
            thread = threading.Thread(target=self.camera_thread, args=(stream,), daemon=True)
            self.thread = thread
            self.run = True
            self.isRunning = True

            thread.start()
        else:
            print('Thread has already been started.')


    def stop_camera_thread(self):

        if self.isRunning:
            self.run = False
            self.isRunning = False
            self.frame = None
            self.thread.join()
        
        else:
            print('Cannot stop thread that is not running.')


    def camera_thread(self, stream):
        
        while self.run:
            if stream != None:
                self.frame = stream.frame

            time.sleep(1/30)

    
    def get_frame(self):
        return self.frame
