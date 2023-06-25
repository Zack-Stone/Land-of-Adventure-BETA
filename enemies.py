class Enemy:
  def __init__(self, HP, XP, name, description, damage):
    self.HP = HP
    self.XP = XP
    self.name = name
    self.description = description
    self.damage = damage
    self.status = None
    self.combat_tick = 0
    self.hot_swap = False
    self.status_list = []
  
  def is_alive(self):
    return self.HP > 0
  
  def do_damage(self, player_damage):
    self.HP -= player_damage
 
  def attack(self, player):
    """does self.damage to player.HP"""
    player.HP -= self.damage

  def do_status(self):
    #self.status.do_status(self)
    for status in self.status_list:
      status.do_status(self)
    
  def gain_status(self, status):
    self.status = status
    self.status_list.append(status)

    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", HP=25, damage=10, XP=5, description="a nasty huge spider with black and green skin, looks scary!")
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", HP=40, damage=20, XP=15, description="a toweing beast with light gray skin and a large club.")

class Goblin(Enemy):
  def __init__(self):
    super().__init__(name="Goblin", HP=50, damage=30,
    XP=25, description="A small green man like monster that weilds a killer axe")

class QueenSpider(Enemy):
  def __init__(self):
    super().__init__(name="Queen Spider", HP=100, damage=40, XP=25,description="a towering spider, its head is coverd in smaller spiders")

class OgreLord(Enemy):
  def __init__(self):
    super().__init__(name="Ogre Lord", HP=160, damage=80, XP=100, description="A huge ogre that is coverd in gold armor")

class KingoftheDungeon(Enemy):
  def __init__(self):
    super().__init__(name="King of the Dungeon", HP=200, damage=120, XP=1000000000000, description="A goblin dressed in kings garb, you know that this has been the thing watching over you this whole time")
