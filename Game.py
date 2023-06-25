import world, classes, designs, map_tile, status
from player import Player
# from colorama import Fore, Back, Style

WORLD_CHOICE = None
CLASS_CHOICE = None

def begin():
	#had Back.WHITE + Fore.BLACK + Style.BRIGHT + ...  + Style.RESET_ALL
  print(designs.INTRO_GAME)
  # had Fore.BLUE + ...  + Style.RESET_ALL
  print(designs.INTRO_TEXT)
  rulesandworld = input("Do you want to know the rules of the game? \ny: Yes \nn: No\n")
  if rulesandworld == "y":
	  makesure = input("\nAre you sure? \ny: Yes \nn: No\n")
	  if makesure == "y":
		  print("\nThis is a text-based adventiure game called land of adventure \n In this game you use commands that appear on screen to do actions in things such as exploring, battaling, and interacting with items in the world\nThe goal of this game is to make it to the end of the chosen map\nIf your HP is depleated, you die and restart the game\n")
	  if makesure == "n":
		  print("\nAlright \n")
  elif rulesandworld == "n":
	  print("\nAlright \n")

def choose_class():
  #return specific player instance: classes.Something()
  all_classes = {
  'f': classes.Fighter(),
  'm': classes.Mage(),
  'x': classes.Assassin(),
  'a': classes.Archer()
  }

  print("Choose your class: ")
  for j in all_classes:
    print(j + ": " + all_classes[j].name)

  choice = input()
  chosen_class = all_classes[choice]

  print("   you choose {}, {}!".format(chosen_class.name, chosen_class.description))

  global CLASS_CHOICE
  #set class choice to same type as player, but different instance
  all_classes_2 = [classes.Fighter(), classes.Mage(), classes.Assassin(), classes.Archer()]
  for obj in all_classes_2:
    if type(obj) == type(chosen_class):
      CLASS_CHOICE = obj

  return chosen_class

def choose_world():
  #allow world choice 
  all_worlds = {
  'e': world.EasyKingdom(),
  'a': world.AdeptVille(),
  'h': world.HardTown()
  }

  print("Choose your world: ")
  for j in all_worlds:
    print(j + ": " + all_worlds[j].name)

  choice = input()
  chosen_world = all_worlds[choice]

  # had ... + Fore.BLUE + Back.WHITE ...  + Style.RESET_ALL
  print(" you are starting on "  + "{}!".format(chosen_world.name))
  
  global WORLD_CHOICE
  WORLD_CHOICE = chosen_world
  return chosen_world


def play():
  begin()
  #TODO choose world
  our_world = choose_world()
  player = choose_class()
  room = our_world.getTile(our_world.StartingXY[0], our_world.StartingXY[1])
  player.location_x, player.location_y = our_world.StartingXY[0], our_world.StartingXY[1]
  print(room.intro_text())
  while player.is_alive() and not player.victory:
    #Game loop
    room = our_world.getTile(player.location_x, player.location_y)

    #stop status check
    do_we_run = True
    if isinstance(room, map_tile.EnemyRoom):
      if room.enemy.status != None:
        for sts in room.enemy.status_list:
          if isinstance(sts, status.StopStatus):
            if sts.status_time > 0:
              do_we_run = False
              print("The {} can't move for {} turns".format(room.enemy.name, sts.status_time))
              sts.run_stop()

    if do_we_run:
      room.modify_player(player)

    if player.is_alive() and not player.victory:
      print("Choose an action:")
      available_actions = room.available_actions()
      for action in available_actions:
        print(action)
      action_input = input('Action: ')
      for action in available_actions:
        if action_input == action.hotkey:
          player.do_action(action, **action.kwargs)
          break
  if player.victory:
    print("YOU WIN\n")
    print("CREDITS\n")
    print("~~~~~HALF OF EVERTHING: DEVIN~~~~~\n")
    print("~~~~~HALF OF EVERTHING: ZACK~~~~~\n")

  else:
    print("YOU LOSE")
if __name__ == "__main__":
  play()