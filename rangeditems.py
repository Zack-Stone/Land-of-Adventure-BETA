from items import Weapon

class RangedWeapon(Weapon):
  def __init__(self, range_, n, d, v, dmg, dur):
    self.range_ = range_
    super().__init__(name=n, description=d, value=v, damage=dmg, durability=dur)

class Bow(RangedWeapon):
  def __init__(self):
    super().__init__(range_=2, n="Bow", d="A nice and shiny bow that loos as if it was just made", v=25, dmg=10, dur=20)
    
class OldBow(RangedWeapon):
  def __init__(self):
    super().__init__(range_=2, n="Old Bow", d="An old and worn out bow that looks like at could break at any moment", v=20, dmg=1, dur=16)
    # dmg was 7

class OldLongBow(RangedWeapon):
  def __init__(self):
    super().__init__(range_=4, n="Old Longbow", d="A very long bow that looks to be rotting", v=25, dmg=13, dur=16)

class LongBow(RangedWeapon):
  def __init__(self):
    super().__init__(range_=4, n="LongBow", d="A vary new looking huge bow", v=25, dmg=17, dur=16)

class OldCrossBow(RangedWeapon):
  def __init__(self):
    super().__init__(range_=1, n="Old Crossbow", d="A very old small crossbow", v=25, dmg=30, dur=16)

class CrossBow(RangedWeapon):
  def __init__(self):
    super().__init__(range_=1, n="Crossbow", d="A new crossbow that is made out of silver and dark oak wood", v=25, dmg=35, dur=20)






    
    

  