from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}
    image_files = {
        'SMALL': 'ball21x21.png',
        'LARGE': 'ball41x41.png',
    }

    def __init__(self, x, y, velocity, ball_type='SMALL'):
        if ball_type not in Ball.images:
            Ball.images[ball_type] = load_image(Ball.image_files[ball_type])
        self.image = Ball.images[ball_type]
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
