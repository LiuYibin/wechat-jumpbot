import wda

import settings
import random

class Connector:


    def __init__(self, image_dir=settings.IMAGE_DIR):
        self.image_dir = image_dir

        self.client = wda.Client()
        self.session = self.client.session()


    def connector_screenshot(self):
        self.client.screenshot(self.image_dir)


    def connector_taphold(self, value):
        x = 260 + random.randint(-20, 20)
        y = 380 + random.randint(-20, 20)
        self.session.tap_hold(x, y, value)
