import random
import json

class Character:
    def get__init__(self,name,age):
        self.name = name
        self.age = age
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()

    @staticmethod
    def roll_dice():
        rolled_dice= []
        for i in range(0,4):
            rolled_dice.append(random.ranint(1,6))

        rolled_dice.remove(min(rolled_dice))
        return sum(rolled_dice)

    def __repr__(self):
        return self.name

class Game():
    def __init__(self):
        self.num_players = int(input('how many players are playing?'))
        self.players= []
        for num in range(1,self.num_players + 1):
            print(f'________enter info for character #{num}______')
            self.add_player()
            print('\n')

    def add_player(self):
        name = input('whats the name of your character?')
        age = input('whats your age?')
        player = Character(name,age)
        self.players.append(player)

    def write_txt(self):
        write_str = f'''D&D Character Sheet

        total players: {len(self.players)}
        '''

        for index,player in enumerate(self.players):
            add_str = f'''

            ___Character #{index+1}___
            name: {player.name}
            age: {player.age}
            strength: {player.strength}
            dexterity: {player.dexterity}
            constitution: {player.constitution}
            intelligence: {player.intelligence}
            wisdom: {player.wisdom}
            charisma: {player.charisma}

            '''

            write_str += add_str

        with open('game_txt','w') as f:
            f.write(write_str)

    def write_json(self):
        players_dict_list = []
        for player in self.players:
            player_dict = {
                'name': player.name,
                'age': player.age,
                'strength': player.strength,
                'dexterity': player.dexterity,
                'constitution': player.constitution,
                'intelligence': player.intelligence,
                'wisdom': player.wisdom,
                'charisma': player.charisma
            }
            players_dict_list.append(player_dict)

        with open('game_json.json','w') as f:
            json.dump(players_dict_list,f,indent=2)

g1 = Game()
g1.write_json()

