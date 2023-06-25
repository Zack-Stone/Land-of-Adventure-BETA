import designs, status

class Item():
  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class Gold(Item):
  def __init__(self, amt):
    self.amt = amt
    super().__init__(name="Gold", description="A round coin with {} stamped on the front.".format(str(self.amt)), value = self.amt)

class Weapon(Item):
  def __init__(self, name, description, value, damage, durability):
    self.damage = damage
    self.durability = durability
    super().__init__(name, description, value)

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDurability: {}".format(self.name, self.description, self.value, self.damage, self.durability)

class Rock(Weapon):
  def __init__(self):
    super().__init__(name="Rock", description="a large rock, looks like it could hurt if used as a weapon.", value=0, damage=5, durability=1000)

class OldSword(Weapon):
  def __init__(self):
    super().__init__(name=" Old Sword", description="a big Sword with a long rusted blade and warn wood handle.", value=10, damage=29, durability=7)

class Sword(Weapon):
  def __init__(self):
    super().__init__(name="Sword", description="A long butiful blade that shines in the sumlight and a new clean wodden hilt.", value=25, damage=35, durability=14)

class Oldshortsword(Weapon):
  def __init__(self):
    super().__init__(name="Old Short Sword", description="A worn sword with a short copper blade with a small chiped hilt.", value=7, damage=25, durability=12)
  
  def __str__(self):
    return "{}\n===========\n".format(self.name) + designs.OLD_SHORT_SWORD + "{}\nValue: {}\nDamage: {}\nDurability: {}".format(self.description, self.value, self.damage, self.durability)

class Shortsword(Weapon):
  def __init__(self):
    super().__init__(name="Short Sword", description="A sword with a blade not as short as a dagger but not as long as a sword.", value=17, damage=30, durability=24)

class Oldlongsword(Weapon):
  def __init__(self):
    super().__init__(name="Old Long Sword", description="A chipted old sword with a very long blade", value=12, damage=27, durability=10)

class Longsword(Weapon):
  def __init__(self):
    super().__init__(name="Long Sword", description="A shiny new sword with jewls encrusted into the hilt and a very long blade.", value=25, damage=40, durability=30)

class Blockingitem(Item):
  def __init__(self, name, description, value, resistance, durability):
    self.resistance = resistance
    self.durability = durability
    super().__init__(name, description, value)

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\nResistance: {}\nDurability {}".format(self.name, self.description, self.value, self.resistance, self.durability)

class Oldshield(Blockingitem):
  def __init__(self):
    super().__init__(name="Old Shield", description="a huge rusted shield with strange symbols on the front.", value=10, resistance=20, durability=10)

  def __str__(self):
    return "{}\n===========\n".format(self.name) + designs.OLD_SHIELD + "{}\nValue: {}\nDamage: {}\nDurability: {}".format(self.description, self.value, self.resistance, self.durability)

class Shield(Blockingitem):
  def __init__(self):
    super().__init__(name="Sheild", description="a sheild", value=20, resistance=27, durability=20)

class TestWeapon(Weapon):
  def __init__(self):
    super().__init__(name="Test", description="pass", value=99999, damage=99999, durability=99999)

class TestSheild(Blockingitem):
  def __init__(self):
    super().__init__(name="Test Sheild", description="pass", value=99999, resistance=99999, durability=99999)

class LeaveItem(Item):
  def __init__(self):
    super().__init__("Exit Shop", "", 0)

class SpellBook(Item):
  def __init__(self, spells):
    self.spells = spells
    super().__init__(name="Spell Book", description="a spell book", value=None)

  def viewSpells(self):
    for spell in self.spells:
      print("\n==========================================================\n" + spell.name + " - Cast time: " + str(spell.cast_time) + " - Damage: " + str(spell.damage) + "\n==========================================================\n")

  def loadSpell(self, spell):
    self.spells.append(spell)

#class MasterSheild(Blockingitem):
 # def __inot__(name="Master Shield", description)

class Spell(Item):
  def __init__(self, name, description, cast_time, damage, status):
    self.cast_time = cast_time
    self.damage = damage
    self.status = status
    super().__init__(name, description, value=None)

class FireBolt(Spell):
  def __init__(self):
    super().__init__(name="Fire Bolt", description="", cast_time=1, damage=25,  status=status.Burn())

class PoisonBeam(Spell):
  def __init__(self):
    super().__init__(name="Poison Beam", description="", cast_time=2, damage=27, status=status.Poison())

class BasicSpellBook(SpellBook):
  def __init__(self):
    basicbook = [FireBolt(), HealingAura()]
    super().__init__(spells=basicbook)

class IceBolt(Spell):
  def __init__(self):
    super().__init__(name="Ice Bolt", description="", cast_time=2, damage=35, status=status.Frozen())

class ThunderShock(Spell):
  def __init__(self):
    super().__init__(name="Thunder Bolt", description="A large bolt of lighning strikes your enemy", cast_time=0, damage=15, status=status.Paralyzed())

class HealingAura(Spell):
  def __init__(self):
    super().__init__(name="Healing Aura", description="Heals damage done to you", cast_time=0, damage=0, status=status.Heal())

class ElementalSpell(Spell):
  def __init__(self, name, description, cast_time, damage, pos_status, neg_status):
    self.pos_status = pos_status
    self.neg_status = neg_status
    super().__init__(name, description, cast_time, damage, None)

class YinANdYangBeam(Spell):
  def __init__(self):
    super().__init__(name="Beam of Yin and Yang", description="", cast_time=5, damage=100, status=status.Yang())
