import items, classes, world

def print_map():
  our_world = world.AdeptVille().getTileMap()
  for i in our_world:
    print()
    for j in i:
      if (j != None):
        print("| {} |".format(j.name), end="")
      else:
        print("~~~~~~~", end="")
    print()
  print()

def choose_char():
  all_classes = {
    'f': classes.Fighter(),
    'm': classes.Mage(),
    'x': classes.Assassin(),
    'a': classes.Archer()
  }
  print("Choose class from following:")
  for i in all_classes:
    print(i + ": " + all_classes[i].description)
  choice = input()
  return all_classes[choice]