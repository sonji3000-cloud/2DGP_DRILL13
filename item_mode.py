from pathlib import Path

from pico2d import (SDL_KEYDOWN, SDL_KEYUP, SDL_QUIT, SDLK_0, SDLK_1, SDLK_ESCAPE,
                    clear_canvas, get_canvas_height, get_canvas_width,
                    get_events, load_font, load_image, update_canvas)

import game_framework
import game_world

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


def handle_events(events=None):
    import play_mode

    if events is None:
        events = get_events()
    return_to_play = False
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYUP:
            play_mode.record_item_key_release(event)
        elif not return_to_play and event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                return_to_play = True
            elif event.key == SDLK_0:
                play_mode.boy.ball_type = 'NONE'
                return_to_play = True
            elif event.key == SDLK_1:
                play_mode.boy.ball_type = 'SMALL'
                return_to_play = True

    # 복귀 키 뒤에 같은 묶음으로 들어온 키 해제도 반영한 후 복귀한다.
    if return_to_play:
        game_framework.pop_mode()


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    center_x = get_canvas_width() // 2
    center_y = get_canvas_height() // 2
    image.draw(center_x, center_y)
    font.draw(center_x - 130, center_y - 135,
              '0: none / 1: small ball', (255, 255, 255))
    font.draw(center_x - 130, center_y - 160,
              '2: coming soon', (255, 255, 255))
    font.draw(center_x - 130, center_y - 185,
              'Esc: cancel', (255, 255, 255))
    update_canvas()
