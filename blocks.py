from pygame import *
import os
import baze

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
FOREST_WIDTH = 64
FOREST_HEIGHT = 96
PLATFORM_COLOR = "#000000"
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/platform.png" % ICON_DIR)
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Platform1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/myGroundpr.png" % ICON_DIR)
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Platform2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/platform2.png" % ICON_DIR)
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Platform3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/platform3.png" % ICON_DIR)
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Forest(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((FOREST_WIDTH, FOREST_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/forest.png" % ICON_DIR)
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, 0, 0)


class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("%s/blocks/шипы.png" % ICON_DIR)