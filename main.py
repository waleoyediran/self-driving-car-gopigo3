from controller import PS4Controller
from utils import throttle
from utils.throttle import throttle2


class TrainDrive(object):
    def __init__(self):
        self.ps4 = PS4Controller()
        self.ps4.init()
        self.ps4.listen()

    # @throttle2(1)
    # def get_drive_data(self):
    #     print("Test")
    #     return self.ps4.get_controller_data()


if __name__ == "__main__":
    td = TrainDrive()
    # while True:
    #     print(td.get_drive_data())
