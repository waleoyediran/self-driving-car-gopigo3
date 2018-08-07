import os
import pprint

import math
import pygame

MAX_FORCE = 5.0
MIN_SPEED = 100
MAX_SPEED = 300
ALLOWANCE = 0.2


class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def get_controller_data(self):
        distance = math.hypot(self.axis_data[0], self.axis_data[1])
        force = abs(distance)

        if force < ALLOWANCE:
            return 0, 0

        return force, self.calculate_angle()

    def calculate_angle(self):
        side_x, side_y = self.axis_data[0], self.axis_data[1]
        if abs(side_x) < 0 or abs(side_y) < ALLOWANCE:
            return 0

        if side_x == 0:
            return 0

        tan_x = abs(side_y) / abs(side_x)
        atan_x = math.atan(tan_x)

        angle_x = atan_x * 180 / math.pi

        if side_y < 0:
            angle_x = angle_x * -1

        if side_x < 0 and side_y < 0:
            angle_x = 270 + abs(angle_x)
        elif side_x < 0 < side_y:
            angle_x = 270 - abs(angle_x)
        elif side_x > 0 and side_y > 0:
            angle_x = 90 + abs(angle_x)
        else:
            angle_x = 90 - abs(angle_x)

        return angle_x

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value, 2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False

                #
                # print(self.get_controller_data())
                # os.system('clear')
                # pprint.pprint(self.button_data)
                if 0 not in self.axis_data or 1 not in self.axis_data:
                    continue
                print(self.get_controller_data())
                # pprint.pprint(self.axis_data)
