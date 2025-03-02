from Code.const import WIN_HEIGHT
from Code.enemy import Enemy
from Code.enemyShot import EnemyShot
from Code.entity import Entity
from Code.playerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.centery > WIN_HEIGHT + ent.height:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.centery < 0:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.centery > WIN_HEIGHT + ent.height:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)