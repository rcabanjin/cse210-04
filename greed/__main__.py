import os
import random

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.rocks import Rocks
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the banner2
    banner2 = Actor()
    banner2.set_text("ghjhjhjhj")
    banner2.set_font_size(FONT_SIZE)
    banner2.set_color(WHITE)
    banner2.set_position(Point(CELL_SIZE + 10, 0))
    cast.add_actor("banners2", banner2)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
       # text = chr(random.randint(33, 111))
        message = messages[n]

        x1 = random.randint(1, COLS - 1)
        y1 = random.randint(1, ROWS - 1)
        position1 = Point(x1, y1)
        position1 = position1.scale(CELL_SIZE)

        x2 = random.randint(1, COLS - 1)
        y2 = random.randint(1, ROWS - 1)
        position2 = Point(x2, y2)
        position2 = position2.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact1 = Gem()
        # artifact.set_text(text) commented out
        artifact1.set_text(random.choice('*')) # this part is editted/ for gems(*) and rocks(0)
        artifact1.set_font_size(random.choice([15, 20, 25])) # font sizes: 15, 20, 25
        artifact1.set_color(color)
        artifact1.set_position(position1)
        artifact1.set_message(message)
        artifact1.set_velocity(Point(0, 5))
        cast.add_actor("artifacts", artifact1)

        artifact2 = Rocks()
        # artifact.set_text(text) commented out
        artifact2.set_text(random.choice('O')) # this part is editted/ for gems(*) and rocks(0)
        artifact2.set_font_size(random.choice([15, 20, 25])) # font sizes: 15, 20, 25
        artifact2.set_color(color)
        artifact2.set_position(position2)
        artifact2.set_message(message)
        artifact2.set_velocity(Point(0, 5))
        cast.add_actor("artifacts", artifact2)


    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()