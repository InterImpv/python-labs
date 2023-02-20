#!/usr/bin/env python3

# helper function
def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class entity:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.max_hp = 0
        self.damage = 0
        self.defence = 0
        self.attack_weight = 0
        self.defend_weight = 0
        self.heal_weight = 0
    
    # for print()
    def __str__(self):
        return f"{self.name}:\n\tHP:\t{self.hp} / {self.max_hp}\n\tDMG:\t{self.damage}\n\tDEF:\t{self.defence}"

    def is_dead(self):
        return (self.hp <= 0)

    def make_player(self):
        self.name = 'Player'
        self.hp = 12
        self.max_hp = 12
        self.damage = 6
        self.defence = 2
        self.attack_weight = 0
        self.defend_weight = 0
        self.heal_weight = 0
        return

    # dumps entity to json
    def save_to(self, path):
        try:
            with open(path, mode='w', encoding='utf-8') as save_file:
                json.dump(self.__dict__, save_file, indent=4)
        except:
            print(f"{__file__}: json dump failed for {path}")

    def load_from_dict(self, target):
        FIELDS = ['name', 'hp', 'max_hp', 'damage', 'defence', 'attack_weight', 'defend_weight', 'heal_weight']
        # check if all the required fields are present for deserialization
        # stolen from stackoverflow
        if not all(field in target for field in FIELDS):
            raise ValueError
        # there should be a better way, but this is simple & straight-forward
        # though extremely error-prone
        try:
            self.name = str(target[FIELDS[0]])
            self.hp = int(target[FIELDS[1]])
            self.max_hp = int(target[FIELDS[2]])
            self.damage = int(target[FIELDS[3]])
            self.defence = int(target[FIELDS[4]])
            self.attack_weight = int(target[FIELDS[5]])
            self.defend_weight = int(target[FIELDS[6]])
            self.heal_weight = int(target[FIELDS[7]])
        except:
            print(f"{__file__}: can not parse object")
            raise ValueError

    # loads entity from json file
    def load_from_file(self, path):
        # print(f"{__file__}: loading player")
        try:
            with open(path, mode='r', encoding='utf-8') as save_file:
                save = json.load(save_file)
            # deserialize from dictionary
            self.load_from_dict(save)
            return True
        # makeshift error detection
        except ValueError as err:
            print(f"{__file__}: \"{path}\" has no required fields or is invalid")
            return False
        except OSError as err:
            print(f"{__file__}: can not open \"{err.filename}\"")
            return False
        # this was hard to get
        except json.decoder.JSONDecodeError as err:
            print(f"{__file__}: \"{path}\" {err.msg.lower()} at line ({err.lineno})")
            return False
            
    # loads random enemy entity from json array
    def load_random(self, path):
        # print(f"{__file__}: loading random enemy")
        try:
            with open(path, mode='r', encoding='utf-8') as save_file:
                save = json.load(save_file)
            # deserialize from dictionary
            self.load_from_dict(random.choice(save))
            return True
        # makeshift error detection
        except ValueError as err:
            print(f"{__file__}: \"{path}\" is invalid")
            return False
        except OSError as err:
            print(f"{__file__}: can not open \"{err.filename}\"")
            return False
        # this was hard to get
        except json.decoder.JSONDecodeError as err:
            print(f"{__file__}: \"{path}\" {err.msg.lower()} at line ({err.lineno})")
            return False

    def sum_weights(self):
        return self.attack_weight + self.defend_weight + self.heal_weight

    def roll_dmg(self):
        if not self.is_dead():
            dmg = random.randint(0, self.damage)
            if dmg > 0:
                print(f"{self.name} rolled {dmg} damage.")
            else:
                print(f"{self.name} missed!")
            return dmg
        else:
            return 0
            
    def roll_heal(self):
        if not self.is_dead():
            new_hp = random.randint(1, 6)
            print(f"{self.name} healed {new_hp} hp!")
            self.hp = clamp(self.hp + new_hp, 0, self.max_hp)
        else:
            return self.hp

def fight(player, action, enemy):
    player_dmg = 0
    enemy_dmg = 0

    # workaround for DEFEND action
    player_defence = player.defence
    enemy_defence = enemy.defence

    # check player death
    if player.is_dead():
        print(f"{player.name} is dead!")
        return

    # player actions
    if action == 'attack':
        player_dmg = clamp(player.roll_dmg() - enemy.defence, 0, player.damage)
    elif action == 'defend':
        print(f'{player.name} defends!')
        player.defence = player.defence * 2
    elif action == 'heal':
        player.roll_heal()
    
    # check enemy death
    if enemy.is_dead():
        print(f"{enemy.name} is dead!")
        return

    # enemy actions (random)
    enemy_action = random.randint(0, enemy.sum_weights())
    if 0 <= enemy_action < enemy.attack_weight:
        enemy_dmg = clamp(enemy.roll_dmg() - player.defence, 0, enemy.damage)
    elif enemy.attack_weight <= enemy_action < enemy.attack_weight + enemy.defend_weight:
        print(f'{enemy.name} defends!')
        enemy.defence = enemy.defence * 2
    else:
        enemy.roll_heal()

    # clamp all hp
    player.hp = clamp(player.hp - enemy_dmg, 0, player.max_hp)
    enemy.hp = clamp(enemy.hp - player_dmg, 0, enemy.max_hp)

    # return old defence values
    player.defence = player_defence
    enemy.defence = enemy_defence
    return
    
A_ACTIVE = ['attack', 'defend', 'heal']
A_PASSIVE = ['show']

def main(args):
    player = entity()
    enemy = entity()
    # Command-line argument parser
    p = argparse.ArgumentParser()
    # Available arguments: --* are optional, others are mandatory
    p.add_argument('--action', '-a',
        choices=(A_ACTIVE + A_PASSIVE),
        default='show',
        help='your action this turn'
    )
    p.add_argument('--restart', '-r',
        action='store_true',
        help='restart game and override everything'
    )
    p.add_argument('--new', '-n',
        action='store_true',
        help='generate new random enemy to fight'
    )
    # Parse
    args = p.parse_args()

    # check flags
    if args.restart:
        player.make_player()
        ret = enemy.load_random("enemies.json")
        if not ret:
            print(f"{__file__}: can not find \"enemies.json\"")
            return -1
    elif args.new:
        enemy.load_random("enemies.json")
        # load current player file
        ret = player.load_from_file("player.json")
        if not ret:
            print(f"{__file__}: can not find \"player.json\"")
            return -1
    else:
        # load current player file
        ret = player.load_from_file("player.json")
        if not ret:
            print(f"{__file__}: can not find \"player.json\"")
            return -1

        # load current enemy file
        ret = enemy.load_from_file("enemy.json")
        if not ret:
            print(f"{__file__}: can not find \"enemy.json\"")
            return -1
        # take offensive action
        if args.action in A_ACTIVE:
            fight(player, args.action, enemy)
    # show stats
    print(enemy)
    print(player)
    # save everything
    player.save_to("player.json")
    enemy.save_to("enemy.json")

    return 0

if __name__ == '__main__':
    import sys
    import random
    import argparse
    import json
    sys.exit(main(sys.argv))