from pico2d import *
import game_framework
import logo_mode


if __name__ == '__main__':
    open_canvas(800, 600)
    try:
        game_framework.run(logo_mode)
    finally:
        close_canvas()
