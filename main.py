from datetime import datetime
import pprint
import time

from picamera import PiCamera
from time import sleep

from controller import PS4Controller


class Application(object):

    def __init__(self):
        self.controller = PS4Controller()
        self.controller.init()

        # self.camera.start_preview()
        # Camera warm-up time
        # sleep(2)

    def start_data_capture(self):
        print "Starting Capture"
        self.controller.start_controller_worker()

        with PiCamera() as camera:
            while True:
                print(self.controller.get_stick_params())
                image_file_name = datetime.now().strftime('photo_%H_%M_%d_%m_%Y.jpg')
                camera.capture(image_file_name)
                time.sleep(0.1)

            print "End Capture"

        # try:
        #     camera = PiCamera()
        #     #
        #     camera.resolution = (1024, 768)
        #
        #
        # finally:
        #     camera

    def __del__(self):
        pass
        # self.camera.stop_preview()


if __name__ == "__main__":
    app = Application()
    app.start_data_capture()
