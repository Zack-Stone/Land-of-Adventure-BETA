import items, random, Game, map_tile, time, skills, rangeditems, status
# from colorama import Fore, Back, Style

class Player():
  def __init__(self, inventory, description, HP, name, skills, mana):
    self.description = description
    self.inventory = inventory
    self.XP = 0
    self.HP = HP
    self.name = name
    self.location_x, self.location_y = 4, 0
    self.victory = False
    self.skills = skills
    self.mana = mana
    self.enemy_facing = None
    self.p_range = 0
    self.status = None
    self.hidden_inv = []

  def is_alive(self):
    return self.HP > 0

  def print_inventory(self):
    print("===========================================================")
    print("HP: {}".format(self.HP))
    print("XP: {}".format(self.XP))
    if self.status:
      print("Status: {}".format(self.status.name), end="")
      print(" - turns left: {}".format(self.status.status_time))
    print("Mana: {}".format(self.mana))
    for i in self.inventory:
      if type(i) == items.Gold:
        print("Gold: {}".format(i.amt))
    print("===========================================================")
    for item in self.inventory:
      print(item, '\n')
    print("===========================================================")

  def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    #TODO: import Game, world_inst = Game.WORLD_CHOICE
    world_inst = Game.WORLD_CHOICE
    print(world_inst.getTile(self.location_x, self.location_y).intro_text())

  def move_north(self):
    self.move(dx=-1, dy=0)

  def move_south(self):
    self.move(dx=1, dy=0)

  def move_east(self):
    self.move(dx=0, dy=1)

  def move_west(self):
    self.move(dx=0, dy=-1)

  def attack(self, enemy):
    """
    1. Show weapons in self.inventory
    2. Allow choice from weapons
    3. Do attack
    """

    #MAGE CLASS ONLY
    if self.name == "Mage":
      self.mage_attack(enemy)
      return

    if self.name == "Assassin":
      self.assassin_attack(enemy)
      return

    #Showing weapons
    weapons_inv = {}
    for i in range(len(self.inventory)):
      if isinstance(self.inventory[i], items.Weapon):
        weapons_inv[str(i)] = self.inventory[i]
    print("Choose weapon: ")
    if self.name == "Archer" and enemy.combat_tick == 1:
	  # was print(Fore.GREEN + Style.BRIGHT + ... + Style.RESET_ALL)
      print("\nRanged weapons can only be chosen once at the start of combat\n")
    elif self.name == "Archer":
	  # was print(Fore.GREEN + Style.BRIGHT + ...  + Style.RESET_ALL)
      print("\nSwitching to a melee weapon will hotswap and forfeit any remaining range\n")
    for j in weapons_inv:
      if isinstance(weapons_inv[j], rangeditems.RangedWeapon):
        print(j + ": " + weapons_inv[j].name + " - " + str(weapons_inv[j].damage) + " dmg" + " - " + str(weapons_inv[j].durability) + " durability" + " - " + str(weapons_inv[j].range_) + " range")
      else:
        print(j + ": " + weapons_inv[j].name + " - " + str(weapons_inv[j].damage) + " dmg" + " - " + str(weapons_inv[j].durability) + " durability")

    #Allowing choice
    choice = input()
    chosen_weapon = weapons_inv[choice]

    #range check
    #first tick interaction ranged / not ranged weapons
    if isinstance(chosen_weapon, rangeditems.RangedWeapon) and enemy.combat_tick == 1:
      self.remove_ranged(chosen_weapon)
      self.p_range = chosen_weapon.range_
    elif not isinstance(chosen_weapon, rangeditems.RangedWeapon) and enemy.combat_tick == 1:
      self.p_range = 0
      self.remove_ranged(None)

    #hotswap - you have range but choose a melee weapon
    if enemy.combat_tick > 1 and self.p_range > 0 and not isinstance(chosen_weapon, rangeditems.RangedWeapon):
      self.p_range = 0
      self.remove_ranged(None)
      enemy.hot_swap = True

    #once combat has ended
    if self.enemy_facing != None:
      if not self.enemy_facing.is_alive():
        self.give_back_ranged()
        self.p_range = 0

    #Do attack
    print("You use {} against {}!".format(chosen_weapon.name, enemy.name))
    enemy.do_damage(chosen_weapon.damage)
    if not enemy.is_alive():
      print("you killed {}!".format(enemy.name))
    else:
      print("{} HP is {}.".format(enemy.name, enemy.HP))
    
    #Check and alter durability
    chosen_weapon.durability -= 1
    if chosen_weapon.durability <= 0:
      print("{} has broken!".format(chosen_weapon.name))
      self.inventory.remove(chosen_weapon)
    
  def remove_ranged(self, save_weapon):
    for item in self.inventory:
      if isinstance(item, rangeditems.RangedWeapon) and item != save_weapon:
        self.inventory.remove(item)
        self.hidden_inv.append(item)

  def give_back_ranged(self):
    for item in self.hidden_inv:
      self.inventory.append(item)
      self.hidden_inv.remove(item)

  def do_status(self):
    self.status.do_status(self)

  def assassin_attack(self, enemy):
    weapons_inv = []
    for i in self.inventory:
      if isinstance(i,items.Weapon):
        weapons_inv.append(i)
    chosen_weapon = self.print_a_dict_of_something(weapons_inv)

    print("You use {} against {}!".format(chosen_weapon.name, enemy.name))
    time.sleep(1.5)
    print("It hit twice!")
    enemy.do_damage(chosen_weapon.damage *2) 
    if not enemy.is_alive():
      print("you killed {}!".format(enemy.name))
    else:
      print("{} HP is {}.".format(enemy.name, enemy.HP))
    
    #Check and alter durability
    chosen_weapon.durability -= 1
    if chosen_weapon.durability <= 0:
      print("{} has broken!".format(chosen_weapon.name))
      self.inventory.remove(chosen_weapon)
  



  def mage_attack(self, enemy):
    spell_book = None
    for i in range(len(self.inventory)):
      if isinstance(self.inventory[i], items.SpellBook):
        spell_book = self.inventory[i]

    spells_dict = {}
    for i in range(len(spell_book.spells)):
      spells_dict[i] = spell_book.spells[i]

    print("Choose spell: ")
    for j in spells_dict:
      print(str(j) + ": " + spell_book.spells[j].name + " - " + str(spell_book.spells[j].damage) + " dmg" + " - " + str(spell_book.spells[j].cast_time) + " Cast Time")

    choice = input()
    chosen_spell = spells_dict[int(choice)]

    #&&&&&&&&&&&&&&&& SWITCH TARGET &&&&&&&&&&&&&&&&&&&&&&&&&
    if isinstance(chosen_spell, items.HealingAura): #or other spells
      print("you heal {} damage!\n".format(chosen_spell.status.damage))
      print("you now have {} HP!\n".format(self.HP))
      self.status = chosen_spell.status
    else:
      if isinstance(chosen_spell, items.YinANdYangBeam):
        print("you deal {} damage!\n".format(chosen_spell.damage))
        print("you take {} damage!\n".format(chosen_spell.status.damage))
        self.status = chosen_spell.status
      #Do attack
      cast_time = chosen_spell.cast_time
      while cast_time > 0:
        print("you are casting your spell.\n")
        time.sleep(1.5)
        print("The {} attacks you\n".format(enemy.name))
        print("     Your HP: {}".format(self.HP))
        print("     Enemy HP: {}".format(enemy.HP))
        print("     Your turns left: {}\n".format(cast_time))
        enemy.attack(self)
        cast_time -= 1
      time.sleep(1.5)
      print("The {} does {} damage!\n       You have {} HP remaining\n".format(enemy.name, enemy.damage, self.HP))

      print("You cast {} against {}!".format(chosen_spell.name, enemy.name))
      enemy.do_damage(chosen_spell.damage)
      if not enemy.is_alive():
        print("you killed {}!".format(enemy.name))
      else:
        print("{} HP is {}.".format(enemy.name, enemy.HP))

  def block(self, enemy):
    """blocks shield amount from enemy attack"""
    #TODO make equip
    best_shield = None
    max_block = 0
    for i in self.inventory:
      if isinstance(i, items.Blockingitem):
        if i.resistance > max_block:
          max_block = i.resistance
          best_shield = i

    print("You use {} to block {} from {}".format(best_shield.name, best_shield.resistance, enemy.name))
    enemy.damage = enemy.damage - best_shield.resistance
    if enemy.damage <= 0:
      enemy.damage = 0
    best_shield.durability -= 1
    if best_shield.durability <= 0:
      print("{} has broken!".format(best_shield.name))
      self.inventory.remove(best_shield)
      

  def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
      action_method(**kwargs)

  def flee(self, tile):
    """Moves the player ramdomly to an adjacent tile"""
    available_moves = tile.adjacent_moves()
    r = random.randint(0, len(available_moves) - 1)
    self.do_action(available_moves[r])

  def heal(self, amt):
    """Given amt heals the player that much - NOTE: can overheal"""
    self.HP += amt

  def gain_mana(self, amt):
    mana2add = Game.CLASS_CHOICE.mana - self.mana
    self.mana += mana2add

  def view_map(self):
    """Opens the players map"""
    our_world = Game.WORLD_CHOICE.getTileMap()
    for i in our_world:
      print()
      for j in i:
        if (j != None and j.visited):
		  # was print(Fore.GREEN + ... +  + Style.RESET_ALL, ... )
          print("| {} |".format(j.name), end="")
        else:
		  # was print print(Fore.GREEN + ... +  + Style.RESET_ALL, ... )
          print("~~~~~~~", end="")
      print()
    print()

  def take_gold(self, amt):
    """Gives amt of gold to player"""
    for i in self.inventory:
      if type(i) == items.Gold:
        i.amt += amt

  def enter_shop(self):
    """asks for y/n input from player, and returns True of False accordingly"""
    choice = input("\ndo you enter the small shop? \ny: Yes \nn: No\n")
    print()
    return choice == 'y'

  def leave_shop(self):
    pass

  def get_item(self, goods):
    player_gold = 0
    for i in self.inventory:
      if type(i) == items.Gold:
        print("Gold: {}".format(i.amt))
        player_gold = i.amt

    goods_dict = {}
    for i in range(len(goods)):
      goods_dict[str(i)] = goods[i]
    print("Choose to buy: ")
    for j in goods_dict:
      print(j + ": " + goods_dict[j].name + " - " + str(goods_dict[j].value) + " Gold")
    
    choice = input()
    chosen_item = goods_dict[choice]
    
    if type(chosen_item) == items.LeaveItem:
      print("You saw the wares were not worthwhile and left")
      return

    if player_gold > chosen_item.value:
      print("You bought {} for {} gold!".format(chosen_item.name, chosen_item.value))

      self.inventory.append(chosen_item)
      for i in self.inventory:
        if type(i) == items.Gold:
         i.amt -= chosen_item.value
    else:
      print("You dont have enough gold to buy that!")
      # print("The End\n")
      # print("try again maybe?")
      pass


  def sell_item(self):
    for i in self.inventory:
      if type(i) == items.Gold:
        print("Gold: {}".format(i.amt))
    
    inv_dict = {}
    for i in range(len(self.inventory)):
      if not isinstance(self.inventory[i], items.Gold):
        inv_dict[str(i)] = self.inventory[i]
    print("Choose to sell:")
    for j in inv_dict:
      print(j + ": " + inv_dict[j].name + " - " + str(inv_dict[j].value) + " Gold")

    #choice of item to sell
    choice = input()
    chosen_item = inv_dict[choice]

    #remove item, replace with value
    print("You sold {} for {} gold!".format(chosen_item.name, chosen_item.value))
    self.inventory.remove(chosen_item)
    for i in self.inventory:
      if type(i) == items.Gold:
        i.amt += chosen_item.value

  def load_spell(self, spell):
    self.get_spell_book()
    spell_book = self.spell_book

    spells_len = len(spell_book.spells)
    if spells_len < 4:
      spell_book.loadSpell(spell)
    else:
      spells_dict = {}
      for i in range(len(spell_book.spells)):
        spells_dict[i] = spell_book.spells[i]

      print("Do you wish to switch a spell out?\n")
      choice = input("y/n")
      if choice == "y":
        for j in spells_dict:
          print(str(j) + ": " + spell_book.spells[j].name + " - " + str(spell_book.spells[j].damage) + " dmg" + " - " + str(spell_book.spells[j].cast_time) + " Cast Time")
        choice = input()
        chosen_spell = spells_dict[int(choice)]

        spell_book.spells.remove(chosen_spell)
        spell_book.load_spell(spell)
        print("\nyou have removed {} for {}!\n".format(chosen_spell.name, spell.name))
      else:
        print("\nYou discard {}\n".format(spell.name))

  def get_spell_book(self):
    spell_book = None
    for i in range(len(self.inventory)):
      if isinstance(self.inventory[i], items.SpellBook):
        spell_book = self.inventory[i]
    self.spell_book = spell_book

  def view_spells(self):
    self.get_spell_book()
    self.spell_book.viewSpells()

  def use_skill(self):
    chosen_skill = self.print_a_dict_of_something(self.skills)
    #direct to skills.py based on class
    chosen_skill.activate(player=self, enemy=self.enemy_facing)

  def print_a_dict_of_something(self, lst):
    """takes a list of things, prints out the choices, returns the chosen item"""
    dict_thing = {}
    for i in range(len(lst)):
      dict_thing[i] = lst[i]
    for j in dict_thing:
      print(str(j) + ": " + dict_thing[j].name)

    choice = input()
    return dict_thing[int(choice)]

  def inspect(self):
    pass