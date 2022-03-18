

class Room:
    def __init__(self, s):
        self.name = s
        self.character = None
        self.z = {}
        self.descr = None
        self.it = None
    def set_description(self, s):
        self.descr = s
    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.descr)
        for dir in self.z:
            print(f'The {self.z[dir].name} is {dir}')
    def link_room(self, r, dir):
        self.z[dir] = r
    def set_character(self, d):
        self.character = d
    def get_character(self):
        return self.character
    def get_item(self):
        return self.it
    def set_item(self, d):
        self.it = d
    def move(self, dir):
        return self.z[dir]
    
class Enemy:
    killed = 0
    def __init__(self, s, t):
        self.name = s
        self.desc = t
    def set_conversation(self, s):
        self.conv = s
    def set_weakness(self, s):
        self.weak = s
    def describe(self):
        print(f'{self.name} is here!')
        print(self.desc)
    def talk(self):
        print(f"[{self.name} says]: {self.conv}") 
    def fight(self, x):
        return x == self.weak
    def get_defeated(self):
        return Enemy.killed
class Item:
    def __init__(self, s):
        self.name = s
    def set_description(self, s):
        self.desc = s
    def get_name(self):
        return self.name
    def describe(self):
        print(f"The [{self.name}] is here - {self.desc}")
