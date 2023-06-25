import items, enemies, actions, Game, designs, Puzzle, classes, items_dagger, rangeditems
# from colorama import Fore, Back, Style

class MapTile:
  def __init__(self, x, y, name, visited=False, inspect=False):
    self.x = x
    self.y = y
    self.name = name
    self.visited = visited
    self.inspect = inspect

  def intro_text(self):
    raise NotImplementedError()

  def modify_player(self, player):
    raise NotImplementedError()

  def adjacent_moves(self):
    """Returns all move actions for adjacent tiles"""
    moves = []
    #TODO: import Game and set to Game.WORLD_CHOICE
    world_inst = Game.WORLD_CHOICE
    if world_inst.tile_exists(self.x, self.y+1):
      moves.append(actions.MoveEast())
    if world_inst.tile_exists(self.x, self.y-1):
      moves.append(actions.MoveWest())
    if world_inst.tile_exists(self.x-1, self.y):
      moves.append(actions.MoveNorth())
    if world_inst.tile_exists(self.x+1, self.y):
      moves.append(actions.MoveSouth())
    return moves

  def available_actions(self):
    """Returns all of the available actions in this room"""

    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())
    moves.append(actions.ViewMap())

    if self.inspect == True:
      moves.append(actions.Inspect())

    if type(Game.CLASS_CHOICE) == classes.Mage:
      moves.append(actions.ViewSpells())

    return moves

class StartingRoom(MapTile):
  def intro_text(self):
	# was return Fore.GREEN + ... + Style.RESET_ALl
    return """
    You are in a empty room.
    how wonderful!
    """

  def modify_player(self, player):
    #Room has not action on player
    self.visited=True
    pass

class LootRoom(MapTile):
  def __init__(self, x, y, item_f, item_x, item_a, name):
    self.item = self.choose_item(item_f, item_x, item_a)
    self.this_player = None
    super().__init__(x, y, name)
    self.item_taken = False

  def choose_item(self, f, x, a):
    if isinstance(Game.CLASS_CHOICE, classes.Assassin):
      return x
    if isinstance(Game.CLASS_CHOICE, classes.Archer):
      return a
    if isinstance(Game.CLASS_CHOICE, classes.Mage) and not isinstance(f, items.Gold):
      print("There is nothing here, move along")
      return None
    return f

  def modify_player(self, player):
    self.visited = True
    self.this_player = player
    if not self.item_taken:
      self.add_loot()
    else:
      return
      
  def add_loot(self):
    self.this_player.inventory.append(self.item)
    self.item_taken = True

class EnemyRoom(MapTile):
  def __init__(self, x, y, enemy, name):
    self.enemy = enemy
    self.player_facing = None
    self.inverserange = 1
    super().__init__(x, y, name)

  def run_status(self, target):
    if target.status != None:
      target.do_status()
    


  def modify_player(self, player):
    self.visited = True
    self.player_facing = player
    player.enemy_facing = self.enemy
    if self.enemy.is_alive():

      #status call
      self.run_status(self.enemy)
      self.run_status(player)

      #archer interaction
      if isinstance(Game.CLASS_CHOICE, classes.Archer) and (self.inverserange > 0 or self.enemy.combat_tick == 1):
        print("You see a {} from a distance".format(self.enemy.name))
        if self.enemy.combat_tick==1 or self.enemy.hot_swap:
          self.set_inverse()
        else:
          if self.enemy.combat_tick > 1:
            self.inverserange -= 1
        print("Your remaining range is: " + str(self.inverserange))
        
        if self.enemy.combat_tick > 1 and self.inverserange == 0:
          player.give_back_ranged()

      else:
        player.HP -= self.enemy.damage
        print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.HP))
        print("Enemy has {} HP".format(self.enemy.HP))

    self.enemy.combat_tick += 1

  def set_inverse(self):
    self.inverserange = self.player_facing.p_range

  def available_actions(self):
    if self.enemy.is_alive():
      return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.Block(enemy=self.enemy), actions.UseSkill()]
    else:
      return self.adjacent_moves()

  def __str__(self):
    return "You face a {}".format(self.enemy.name)

class EmptyCavePath(MapTile):
  def intro_text(self):
    return"""
    another bland peice of empty cave.
    """

  def modify_player(self, player):
    self.visited = True
    pass

class GiantSpiderRoom(EnemyRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, enemies.GiantSpider(), name)

  def intro_text(self):
    if self.enemy.is_alive():
      return designs.SPIDER_TEXT
    else:
      return"""
      a dead spider lays on the ground
      """

class FindDaggerRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items_dagger.Dagger(), items_dagger.Dagger(), items_dagger.Dagger(), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a Dagger with a plaque in front of it.
      it reads "a Dagger".

      you got the Dagger!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Dagger" but it is empty
      """

class FindSmallGoldRoom(LootRoom):
  def __init__(self,x, y, name):
    super().__init__(x, y, items.Gold(50), items.Gold(50), items.Gold(50), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
    You see a faint glitter in the corner of the room.
    You found 50 gp!
    """
    else:
      return """
      You found the gold here already!!
      """

class OgreRoom(EnemyRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, enemies.Ogre(), name)

  def intro_text(self):
    if self.enemy.is_alive():
      return"""
      As you walk into this room you see a huge Ogre!
      """
    else:
      return"""
      as you walk into this room you see 
      the rotting corpse of an Ogre.
      You are disgusted.
      """

class GoblinRoom(EnemyRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, enemies.Goblin(), name)

  def intro_text(self):
    if self.enemy.is_alive():
      return"""
      As you walk into this room you see a small little green guy you assume its a goblin, it attacks you!
      """
    else:
      return"""
      as you walk into this room you see what at first glance is a small green rock.
      You are disgusted.
      """

class QueenSpiderRoom(EnemyRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, enemies.QueenSpider(), name)

  def intro_text(self):
    if self.enemy.is_alive():
      return"""
      As you walk into this room you see a spider it looks to be very angry, it attacks you!
      """
    else:
      return"""
      as you walk into this room you see a large green blob on the floor.
      You are disgusted.
      """
class OgreLordRoom(EnemyRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, enemies.OgreLord(), name)

  def intro_text(self):
    if self.enemy.is_alive():
      return"""
      As you walk into this room you see a very lrage ogre dressed in gold, it attacks you!
      """
    else:
      return"""
      as you walk into this room you see a bunch of gold armor on the floor. 
      You do want to pick it up.
      """

class KingoftheDungeonRoom(EnemyRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, enemies.KingoftheDungeon(), name)

  def intro_text(self):
    if self.enemy.is_alive():
      return"""
      As you walk into this room you see a short goblin that is dressed in kings garb it look at you mencingly, it attacks you!
      """
    else:
      return"""
      How are you reading this? you need to go into the next room to finish the game!
      """


  def modify_player(self, player):
    if self.enemy.is_alive(): 
      player.HP -= self.enemy.damage
      print("The Boss does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.HP))
    else:
      player.victory = True
      
class LeaveCaveRoom(MapTile):
  def intro_text(self):
    return"""
    you won!
    """

  def modify_player(self, player):
    player.victory = True

class PuzzleRoom(MapTile):
  this_player = None

  def __init__(self, x, y, name):
    super().__init__(x, y, name)
    self.SUCCESS = False

  def intro_text(self):
    if not self.SUCCESS:
      return """\n you walk into the room and see a large red door \n it is locked.\n"""
    else:
      return """\n you walk into the room and see a large red door \n it is unlocked and open \n"""

  def modify_player(self, player):
    """BREAKING ABSTRACTION LAWS"""
    self.visited = True
    self.this_player = player

    #if we haven't won, do this process.
    if not self.SUCCESS:
      print ("guess a letter")
      guess = input("")
      print (" ")
      puzzle_inst = Puzzle.HangMan()
      puzzle_inst.start(guess, 6, [])
      self.SUCCESS = puzzle_inst.SUCCESS

  def get_starting_room(self):
    return Game.WORLD_CHOICE.StartingXY

  def available_actions(self):
    """Returns all of the available actions in this room"""
    moves = []
    while not self.SUCCESS:
      self.available_actions_fail()
    moves = self.available_actions_success()
    return moves

  def available_actions_success(self):
    moves = super().adjacent_moves()
    moves.append(actions.ViewInventory())
    return moves

  def available_actions_fail(self):
    self.this_player.HP -= 10
    print("\n--- You took 10 damage! Your health is now {} ---\n".format(self.this_player.HP))
    self.modify_player(self.this_player)

class ActionRoom(MapTile):
  def __init__(self, x, y, amt, method, name):
    """
    method = actions.Heal, actions.TakeGold
    """
    self.this_player = None
    self.amt = amt
    self.method = method
    super().__init__(x, y, name)
    self.amt_taken = False

  def intro_text(self):
    return NotImplementedError

  def modify_player(self, player):
    self.visited = True
    self.this_player = player
    if not self.amt_taken:
      response = input("y/n\n")
      if response == 'y':
        self.amt_taken = True
        self.method(self.amt).method(self.this_player, self.amt)
      elif response == 'n':
        return

class MedicalRoom(ActionRoom):
  def __init__(self, x, y, amt, name):
    method = actions.Heal
    super().__init__(x, y, amt, method, name)

  def intro_text(self):
    if not self.amt_taken:
      return"""\n you see a small tent with a red cross\ndo you heal yourself?\n"""
    else:
      return"""\n the tent has been destoryed\ntheres nothing you can do.\n"""

class ManaRoom(ActionRoom):
  def __init__(self, x, y, amt, name):
    method = actions.GainMana
    super().__init__(x, y, amt, method, name)

  def intro_text(self):
    if not self.amt_taken:
      return"""\n you see a small pad with the anicant symbol for mana ingraves into it, it is glowing\ndo you gain back your mana?"""
    else:
      return"""\n a weird ring sits in the middle of the room\ntheres nothing you can do.\n"""

class FindGoldRoom(ActionRoom):
  def __init__(self, x, y, amt, name):
    method = actions.TakeGold
    super().__init__(x, y, amt, method, name)

  def intro_text(self):
    if not self.amt_taken:
      return"""\n you see a pile of gold in the middle of the room\ndo you take the gold?\n"""
    else:
      return"""\nthere is nothing but a few loose coins in this room\n"""

class FindOldSwordRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.OldSword(), items_dagger.OldNunchucks(), rangeditems.OldBow(), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a rusted old sword with a plaque in front of it.
      it reads "this is a old sword."

      you got the old Sword!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Old Sword" but it is empty
      """

class FindOldShortSwordRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.Oldshortsword(), items_dagger.OldDuelDaggers(), rangeditems.OldCrossBow(), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a rusted old short sword with a plaque in front of it.
      it reads "this is a old short sword."

      you got the old Short Sword!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Old ShortSword" but it is empty
      """

class FindSwordRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.Sword(), items_dagger.Nunchucks(), rangeditems.Bow(), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a shinling and glinting sword with a plaque in front of it.
      it reads "a Sword".

      you got the Sword!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Sword" but it is empty
      """

class FindShortSwordRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.Shortsword(), items_dagger.DuelDaggers(), rangeditems.CrossBow(), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a shining Shortsword with a plaque in front of it.
      it reads "a Shortsword".

      you got the Shortsword!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Shortsword" but it is empty
      """

class FindOldLongSwordRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.Oldlongsword(), items_dagger.OldDuelHandaxe(), rangeditems.OldLongBow(), name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a rusted Longsword with a plaque in front of it.
      it reads "a Dagger".

      you got the Old Longsword!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Old Longsword" but it is empty
      """

class FindLongSwordRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.Longsword(), items_dagger.DuelHandaxe(), rangeditems.LongBow(), name)
    
  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a shining Longsword with a plaque in front of it.
      it reads "a Longsword".

      you got the Longsword!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Longsword" but it is empty
      """

class FindShieldRoom(LootRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, items.Shield(), None, None, name)

  def intro_text(self):
    if not self.item_taken:
      return"""
      in the middle of this room there is a stone pedestal.
      on the pedestal you see a glinting Shield with a plaque in front of it.
      it reads "a Shield".

      you got the Shield!
      """
    else:
      return"""
      the stone pedestal is empty there is a plaque that says "a Sheild" but it is empty
      """

class ShopRoom(MapTile):
  def __init__(self, x, y, goods, name):
    self.goods = goods
    self.inside = False
    super().__init__(x, y, name)

  def intro_text(self):
    return """\nas you enter the room you see a small tent in\na wharm glow flows out from the inside\n"""

  def modify_player(self, player):
    if not self.inside:
      self.inside = player.enter_shop()
    self.visited = True

  def available_actions(self):
    """if entered, return list of buy, sell, or leave,
        else, normal available-actions"""
    moves = []
    if self.inside:
      moves.append(actions.GetItem(self.goods))
      moves.append(actions.SellItem())
      moves.append(actions.ViewInventory())
      #moves.append(actions.LeaveShop())
      self.inside = False
    else:
      moves = self.adjacent_moves()
      #moves.append(actions.EnterShop())
      moves.append(actions.ViewInventory())
      moves.append(actions.ViewMap())
    return moves

class SpellRoom(MapTile):
  def __init__(self, x, y, name, spell):
    self.spell = spell
    self.item_taken = False
    super().__init__(x, y, name)

  def modify_player(self, player):
    """use player.load_spell"""
    self.visited = True
    self.this_player = player
    if not self.item_taken:
      if isinstance(Game.CLASS_CHOICE, classes.Mage):
        player.load_spell(self.spell)
    else:
      self = EmptyCavePath(self.x, self.y, "ECP")

class FindIceBolt(SpellRoom):
  def __init__(self, x, y, name):
    super().__init__(x, y, name, items.IceBolt())

  def intro_text(self):
      if isinstance(Game.CLASS_CHOICE, classes.Mage):
        if not self.item_taken:
          return"""
          You see a dusty book in the middle of the room it reads "Ice Bolt".
          """
        else:
          return"""
          You see a book with all the pages blank.
          """
      else:
        return """
        You see a book with symbols you cannot read.
        """