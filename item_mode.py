from pathlib import Path

from pico2d import (SDL_QUIT, clear_canvas, get_canvas_height,
                    get_canvas_width, get_events, load_font, load_image,
                    update_canvas)

import game_framework

image = None
font = None


def init():
    global image, font
    image = load_image(str(Path(__file__).with_name('item_select.png')))
    font = load_font('C:/Windows/Fonts/arial.ttf', 18)


def finish():
    global image, font
    image = None
    font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return


def update():
    pass


def render():
    clear_canvas()
    center_x = get_canvas_width() // 2
    center_y = get_canvas_height() // 2
    image.draw(center_x, center_y)
    font.draw(center_x - 130, center_y - 135,
              '0 / 1 / 2: coming soon', (255, 255, 255))
    update_canvas()
