from controller import PS4Controller


class TrainDrive(object):
    def __init__(self):
        self.ps4 = PS4Controller()
        self.ps4.init()

    def drive(self):
        self.ps4.listen()


if __name__ == "__main__":
    td = TrainDrive()
    td.drive()
