# Wechat Jump Bot (iOS)
# ----------------------------------------------------------------------------

import os

CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
PROJECT_DIR = "jumpbot/"

# ----------------------------------------------------------------------------
# Configurations

CONFIG_DIR = "config/"
CONFIG_FILE = PROJECT_DIR + CONFIG_DIR + "config.json"

# ----------------------------------------------------------------------------
# Screenshot

DATA_DIR = "data/"
IMAGE = "screen.png"
IMAGE_DIR = PROJECT_DIR + DATA_DIR + IMAGE

# ----------------------------------------------------------------------------

# mode: ['auto', 'manual']
MODE = "auto"

# ----------------------------------------------------------------------------
# Params

# Manual Mode:
# - iphone X: 0.00125
# - iphone 6/7: 0.0021
# Auto Mode:
# - iphone 6/7: 2.0
TIME_COEFF = 2.0

# Auto Mode:
COORD_Y_START_SCAN = 200
PIECE_BASE_HEIGHT_HALF = 13
PIECE_BODY_WIDTH = 49
SWIPE_X1 = 375
SWIPE_Y1 = 1055
SWIPE_X2 = 375
SWIPE_Y2 = 1055
