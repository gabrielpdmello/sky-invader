from Code.const import ENTITY_SPEED
from Code.entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.rect = self.surf.get_rect(left=position[0] - self.width / 2, top=position[1] + self.height / 2)

    def move(self, axis):
        self.rect.centery -= ENTITY_SPEED[self.name]
