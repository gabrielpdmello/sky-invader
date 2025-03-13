from Code.const import WIN_HEIGHT, COLLISION_DELAY
from Code.enemy import Enemy
from Code.enemyShot import EnemyShot
from Code.entity import Entity
from Code.hp import HP
from Code.player import Player
from Code.playerShot import PlayerShot


class EntityMediator:
    # removes health from entities if they go out of screen
    @staticmethod
    def __verify_outside_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.centery > WIN_HEIGHT + ent.height:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.centery < 0:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.centery > WIN_HEIGHT + ent.height:
                ent.health = 0
        if isinstance(ent, HP):
            if ent.rect.centery > WIN_HEIGHT + ent.height:
                ent.health = 0

    # verify collision between every entity in a given array
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_outside_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    # checks if two entities are colliding
    @staticmethod
    def __detect_collision(ent1, ent2):
        if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):
            return True


    @staticmethod
    def __apply_damage(ent1, ent2):
        ent1.health -= ent2.damage
        ent2.health -= ent1.damage
        if ent1.health <= 0:
            ent1.destroyed_by = ent2.name

        if ent2.health <= 0:
            ent2.destroyed_by = ent1.name

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # collision will only happen between these entities
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            EntityMediator.__verify_collision_shot(ent1, ent2)
        elif isinstance(ent2, Enemy) and isinstance(ent1, PlayerShot):
            EntityMediator.__verify_collision_shot(ent2, ent1)
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            EntityMediator.__verify_collision_shot(ent1, ent2)
        elif isinstance(ent2, Player) and isinstance(ent1, EnemyShot):
            EntityMediator.__verify_collision_shot(ent2, ent1)
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            EntityMediator.__verify_collision_aircraft(ent1, ent2)
        elif isinstance(ent2, Player) and isinstance(ent1, Enemy):
            EntityMediator.__verify_collision_aircraft(ent2, ent1)
        elif isinstance(ent1, Player) and isinstance(ent2, HP):
            EntityMediator.__verify_collision_health(ent2, ent1)
        elif isinstance(ent2, HP) and isinstance(ent1, Player):
            EntityMediator.__verify_collision_health(ent2, ent1)

    # verify collision between shot and aircraft
    @staticmethod
    def __verify_collision_shot(shot, aircraft):
        if EntityMediator.__detect_collision(shot, aircraft):
            EntityMediator.__apply_damage(shot, aircraft)

    # verify collision between aircraft
    @staticmethod
    def __verify_collision_aircraft(player, enemy):
        if EntityMediator.__detect_collision(player, enemy) and player.collision_delay <= 0:
            EntityMediator.__apply_damage(player, enemy)
            player.collision_delay = COLLISION_DELAY

    @staticmethod
    def __verify_collision_health(health, player):
        if EntityMediator.__detect_collision(health, player):
            EntityMediator.__apply_damage(health, player)
            player.health = 100

    # removes entities with no health left
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