from pico2d import *
import game_framework
import game_world
import title_mode
from boy import Boy
from grass import Grass

paused = False
pause_key_down = False
pause_started_at = 0.0
paused_key_releases = []


def toggle_pause():
    global paused, pause_started_at

    if paused:
        boy.idle_started_at += get_time() - pause_started_at
        for event in paused_key_releases:
            boy.handle_event(event)
        paused_key_releases.clear()
    else:
        pause_started_at = get_time()

    paused = not paused


def handle_events():
    global pause_key_down

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if not pause_key_down:
                toggle_pause()
            pause_key_down = True
        elif event.type == SDL_KEYUP and event.key == SDLK_p:
            pause_key_down = False
        elif not paused:
            boy.handle_event(event)
        elif event.type == SDL_KEYUP:
            paused_key_releases.append(event)



def init():
    global boy, paused, pause_key_down, pause_started_at

    paused = False
    pause_key_down = False
    pause_started_at = 0.0
    paused_key_releases.clear()

    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy)




def update():
    if not paused:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    global boy, paused, pause_key_down
    game_world.clear()
    boy = None
    paused = False
    pause_key_down = False
    paused_key_releases.clear()


