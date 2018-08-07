import pygame

from utils.throttle import throttle

MAX_FORCE = 5.0
MIN_SPEED = 100
MAX_SPEED = 300
ALLOWANCE = 0.2

STRAIGHT = 'straight'
LEFT = 'left'
RIGHT = 'right'


class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    steering_orientation = STRAIGHT
    force = 0.0

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def get_controller_data(self):
        return self.force, self.steering_orientation

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value, 2)

                if 0 not in self.axis_data or 1 not in self.axis_data:
                    continue

                if self.axis_data[0] < -0.6:
                    self.steering_orientation = LEFT
                elif self.axis_data[0] > 0.6:
                    self.steering_orientation = RIGHT
                else:
                    self.steering_orientation = STRAIGHT

                if self.axis_data[1] < -0.5:
                    self.force = (self.axis_data[1] + 0.5) * -2.
                elif self.axis_data[1] > 0.5:
                    self.force = (self.axis_data[1] - 0.5) * -2.
                else:
                    self.force = 0.0

                self.move()

    @throttle(0.2)
    def move(self):
        print(self.get_controller_data())
