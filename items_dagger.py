import items

class Dagger(items.Weapon):
  def __init__(self):
    super().__init__(name="Dagger", description="A dagger with a long silver blade", value=10, damage=10, durability= 7)


class OldDuelDaggers(items.Weapon):
  def __init__(self):
    super().__init__(name="Old Duel Daggers", description="Two rusted, silver daggers", value=20, damage=10, durability=10)

class DuelDaggers(items.Weapon):
  def __init__(self):
    super().__init__(name="Duel Daggers", description="Two sharp, silver daggers", value=20, damage=15, durability=10)

class OldNunchucks(items.Weapon):
  def __init__(self):
    super().__init__(name="Old Nunchucks", description="An old rotting pair of nunchucks", value=20, damage=15, durability=10)

class Nunchucks(items.Weapon):
  def __init__(self):
    super().__init__(name="Old Nunchucks", description="A new pair of silver nunchucks", value=20, damage=17, durability=10)

class OldDuelHandaxe(items.Weapon):
  def __init__(self):
    super().__init__(name="Old Duel Handaxe", description="A rusted over pair of axes that look to be silver", value=20, damage=19, durability=10)

class DuelHandaxe(items.Weapon):
  def __init__(self):
    super().__init__(name="Duel Handaxe", description="A shiny pair of axes that gleam in the sunlight", value=20, damage=22, durability=10)



