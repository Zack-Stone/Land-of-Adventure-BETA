from player import Player
import items, items_dagger, skills, rangeditems

class Fighter(Player):
  def __init__(self):
    inventory = [items.Oldshortsword(), items.Oldshield(), items.Rock(), items.Gold(75)]
    description = "A strong warrior that starts with 110 HP, 50 Gold, an Old Short Sword, and an Old Shield"
    HP = 210
    name = "Fighter"
    starter_skills = [skills.ShieldBubble(), skills.ShieldBash()]
    mana = 10
    super().__init__(inventory, description, HP, name, starter_skills, mana)


class Mage(Player):
  def __init__(self):
    inventory = [items.BasicSpellBook(), items.Rock()]
    description = "A very cool Mage who is very mage-like"
    HP = 220
    name = "Mage"
    starter_skills = []
    mana = 0
    super().__init__(inventory, description, HP, name, starter_skills, mana)


class Assassin(Player):
  def __init__(self):
    inventory = [items_dagger.Dagger(), items_dagger.OldDuelDaggers()]
    description = "A sneaky Assassin"
    HP = 200
    name = "Assassin"
    starter_skills = [skills.SneakAttack(), skills.PoisonSpray()]
    mana = 12
    super().__init__(inventory, description, HP, name, starter_skills, mana)


class Archer(Player):
  def __init__(self):
    inventory = [rangeditems.OldBow(), items_dagger.Dagger(), items.Shield]
    description = "A fast archer"
    HP = 205
    name = "Archer"
    starter_skills = [skills.Backflip(), skills.ElementalArrow()]
    mana = 12
    super().__init__(inventory, description, HP, name, starter_skills, mana)