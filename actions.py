from player import Player

class Action():
  def __init__(self, method, name, hotkey, **kwargs):
    self.method = method
    self.name = name
    self.hotkey = hotkey
    self.kwargs = kwargs

  def __str__(self):
    """
        N
        |
     W-----E
        |
        S
    i: View Inventory
    ==========
    a: Attack
    b: Block
    f: Flee
    ==========
    """
    return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
  def __init__(self):
    super().__init__(method=Player.move_north, name='Move North', hotkey='n')

class MoveSouth(Action):
  def __init__(self):
    super().__init__(method=Player.move_south, name='Move South', hotkey='s')

class MoveWest(Action):
  def __init__(self):
    super().__init__(method=Player.move_west, name="Move West", hotkey='w')

class MoveEast(Action):
  def __init__(self):
    super().__init__(method=Player.move_east, name="Move East", hotkey='e')

class ViewInventory(Action):
  """prints the player's inventory"""
  def __init__(self):
    super().__init__(method=Player.print_inventory, name="View Inventory", hotkey='i')

class Attack(Action):
  def __init__(self, enemy):
    super().__init__(method=Player.attack, name='Attack', hotkey='a', enemy=enemy)

class Block(Action):
  def __init__(self, enemy):
    super().__init__(method=Player.block, name='Block', hotkey='b', enemy=enemy)

class Flee(Action):
  def __init__(self, tile):
    super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class Heal(Action):
  def __init__(self, amt):
    super().__init__(method=Player.heal, name="Heal", hotkey='h', amt=amt)

class GainMana(Action):
  def __init__(self, amt):
    super().__init__(method=Player.gain_mana, name="Gain Mana", hotkey='G', amt=amt)

class ViewMap(Action):
  def __init__(self):
    super().__init__(method=Player.view_map, name="View Map", hotkey='m')
    
class TakeGold(Action):
  def __init__(self, amt):
    super().__init__(method=Player.take_gold, name="Take Gold", hotkey='_', amt=amt)
    
class EnterShop(Action):
  def __init__(self):
    super().__init__(method=Player.enter_shop, name="Enter Shop", hotkey='q')

class GetItem(Action):
  def __init__ (self, goods):
    super().__init__(method=Player.get_item, name="Buy", hotkey='b', goods=goods)

class SellItem(Action):
  def __init__(self):
    super().__init__(method=Player.sell_item, name="Sell", hotkey='s')

class LeaveShop(Action):
  def __init__(self):
    super().__init__(method=Player.leave_shop, name="Leave Shop", hotkey='l')

class CastSpell(Action):
  def  __init__(self):
    super().__init__(method=Player.cast_spell, name="Cast Spell", hotkey='c')

class ViewSpells(Action):
  def __init__(self):
    super().__init__(method=Player.view_spells, name="View Spells", hotkey='v')

class UseSkill(Action):
  def __init__(self):
    super().__init__(method=Player.use_skill, name="Use Skill", hotkey='s')

class Inspect(Action):
  def __init__(self):
    super().__init__(method=Player.inspect, name="Inspect", hotkey='Figure out later')