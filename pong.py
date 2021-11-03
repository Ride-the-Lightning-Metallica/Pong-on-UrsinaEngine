from ursina import *

app = Ursina()


class Player(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            color=color.white,
            scale=(0.3, 1),
            x=7
        )

    def update(self):
        self.y += (held_keys['up arrow'] -
                   held_keys['down arrow']) * time.dt * 3


player = Player()

app.run()
