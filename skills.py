import time, items, status, rangeditems

class Skill:
  def __init__(self, name, definition, damage, mana_cost):
    self.name = name
    self.definition = definition
    self.damage = damage
    self.mana_cost = mana_cost

  def activate(self):
    raise NotImplementedError

  def average_item_damage(self, player):
    result_dmg = 0
    num_weapons = 0
    for i in player.inventory:
      if isinstance(i, items.Weapon):
        result_dmg += i.damage
        num_weapons += 1
    return result_dmg/num_weapons
    
class SneakAttack(Skill):
  def __init__(self):
    super().__init__(name="Sneak Attack", definition="", damage=20, mana_cost=6)

  def activate(self, player, enemy):
    """do damage to enemy, however you like"""
    if self.mana_cost < player.mana:
      print("You use Sneak Attack on {}!".format(enemy.name))
      
      time_cost = 1
      dmg_done = self.average_item_damage(player) * 2
      while time_cost > 0:
        print("you dash behind your enemy!\n")
        time.sleep(1.5)
        print("{} attacks you, but you avoid it\n".format(enemy.name))
        time.sleep(1.5)
        print("you strike {} in the back, you deal {} damage!\n".format(enemy.name, dmg_done))
        
        enemy.do_damage(dmg_done)
        player.mana -= self.mana_cost

        time_cost -= 1

    else:
      print("You don't have enough mana!")
      return

class PoisonSpray(Skill):
  def __init__(self):
    self.status_effect=None
    super().__init__(name="Poison Spray", definition="", damage=0, mana_cost=2)

  def activate(self, player, enemy):
    self.status_effect=status.Poison()
    if self.mana_cost < player.mana:
      print ("You use Poison Spray on {}!".format(enemy.name))
      enemy.gain_status(self.status_effect)
      player.mana -= self.mana_cost

class ShieldBubble(Skill):
  def __init__(self):
    super().__init__(name="Shield Bubble", definition="", damage=0, mana_cost=6)

  def activate(self, player, enemy):
    if self.mana_cost < player.mana:
      print("You use Shield Bubble!")

      time_cost = 1
      dmg = self.average_item_damage(player)
      while time_cost > 0:
        print("A clear bubble appears around you\n{} attacks, the attack bounces off the bubble\n".format(enemy.name))
        enemy.do_damage(dmg)
        time.sleep(1.5)
        print("the bubble looks like it could burst any time now\n{} attacks again!\n".format(enemy.name))
        time.sleep(1.5)
        enemy.do_damage(dmg)
        print("The bubble pops!\n you are now vulnerable to attacks\n")

        player.mana -= self.mana_cost
        time_cost -= 1
      print("You did {} total damage!\n".format(dmg*2))
    else:
      print("you dont have enough mana!")
      return 


class ShieldBash(Skill):
  def __init__(self):
    self.status_effect=None
    super().__init__(name="Shield Bash", definition="", damage=10, mana_cost=4)

  def activate(self, player, enemy):
    self.status_effect=status.Stun()
    if self.mana_cost < player.mana:
      print ("You ram into {} with your sheild!".format(enemy.name))
      enemy.gain_status(self.status_effect)
      player.mana -= self.mana_cost

class Backflip(Skill):
  def __init__(self):
    super().__init__(name="Backflip", definition="", damage=0, mana_cost=6)

  def activate(self, player, enemy):
    if self.mana_cost < player.mana:
      #choose bow - requires player.p_range = chosen bow range
      ranged_inv = []
      for item in player.inventory:
        if isinstance(item, rangeditems.RangedWeapon):
          ranged_inv.append(item)
      print("Choose a bow: ")
      player.print_a_dict_of_something(ranged_inv)

      enemy.combat_tick = 1
      print("You gracefully leap behind your enemy, flashing a smile at the camera")
      player.mana -= self.mana_cost

class ElementalArrow(Skill):
  def __init__(self):
    super().__init__(name="Elemental Arrow", definition="", damage=15, mana_cost=7)

  def activate(self, player, enemy):
    self.status_effect=status.Burn()
    self.status_effect_two=status.Scald()
    self.status_effect_three=status.Vines()
    if self.mana_cost < player.mana:
      print ("You hit the {} with an arrow of pure enegry!".format(enemy.name))
      enemy.gain_status(self.status_effect)
      enemy.gain_status(self.status_effect_two)
      enemy.gain_status(self.status_effect_three)
      print("The {} is now, trapped in vines, is burnt and scalded!".format(enemy.name))
      player.mana -= self.mana_cost