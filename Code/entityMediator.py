from Code.const import WIN_HEIGHT
from Code.enemy import Enemy
from Code.enemyShot import EnemyShot
from Code.entity import Entity
from Code.player import Player
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
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                if ent1.health <= 0:
                    ent1.destroyed_by = ent2.name

                if ent2.health <= 0:
                    ent2.destroyed_by = ent1.name
                # ent1.last_dmg = ent2.name
                # ent2.last_dmg = ent1.name

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.destroyed_by == 'Shots/player_shot':
            for ent in entity_list:
                if ent.name == 'Player/1B':
                    ent.score += enemy.score