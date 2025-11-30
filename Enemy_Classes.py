class Enemy:

    def __init__(self, name, health = None, mana = None, strength = None):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength


    def __str__(self):
        ret = f'Объект {self.__class__.__name__}: Имя: {self.name}, Здоровье = {self.health}, Мана = {self.mana}, Сила = {self.strength}'
        return ret

class Mage(Enemy):
    pass

class Ogre(Enemy):
    pass

if __name__ == '__main__':
        a = Mage('Маг', 100, 50, 25 )
        print(a)

