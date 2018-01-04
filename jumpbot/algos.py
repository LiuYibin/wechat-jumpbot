import math

import settings


def get_press_time(piece_x, piece_y, board_x, board_y):
        distance = math.sqrt((board_x - piece_x) ** 2 + (board_y - piece_y) ** 2)
        press_time = distance * settings.TIME_COEFF / 1000
        return press_time
