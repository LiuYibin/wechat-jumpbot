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
MODE = "manual"

# ----------------------------------------------------------------------------
# Params

def get_bot_params(model="ip7"):

    bot_params = {
        "TIME_COEFF": 2.,
        "COORD_Y_START_SCAN": 200,
        "PIECE_BASE_HEIGHT_HALF": 13,
        "PIECE_BODY_WIDTH": 49,
        "SWIPE_X1": 375,
        "SWIPE_Y1": 1055,
        "SWIPE_X2": 375,
        "SWIPE_Y2": 1055
    }

    if model == "ip7":
        bot_params["TIME_COEFF"] = 2.
        bot_params["COORD_Y_START_SCAN"] = 200
        bot_params["PIECE_BASE_HEIGHT_HALF"] = 13
        bot_params["PIECE_BODY_WIDTH"] = 49
        bot_params["SWIPE_X1"] = 375
        bot_params["SWIPE_Y1"] = 1055
        bot_params["SWIPE_X2"] = 375
        bot_params["SWIPE_Y2"] = 1055

    else:
        return bot_params

    return bot_params
