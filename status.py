class Status():
  def __init__(self, damage, status_time, name):
    self.damage = damage
    self.status_time = status_time
    self.name = name

  def do_status(self):
    raise NotImplementedError

class DamageStatus(Status):
  def __init__(self, damage, status_time, name):
    self.target = None
    super().__init__(damage, status_time, name)

  def do_status(self, target):
    print("{} has {}, and it will wear off in {} turns".format(target.name, self.name, self.status_time))
    self.target = target
    if self.status_time > 0:
      self.target.HP -= self.damage
      self.status_time -= 1

class StopStatus(Status):
  def __init__(self, damage, status_time, name):
    super().__init__(damage, status_time, name)

  def do_status(self, target):
    pass

  def run_stop(self):
    self.status_time -= 1

class HealStatus(Status):
  def __init__(self, damage, status_time, name):
    self.target = None
    super().__init__(damage, status_time, name)

  def do_status(self, target):
    self.target = target
    if self.status_time > 0:
      self.target.HP += self.damage
      self.status_time -= 1

class Burn(DamageStatus):
  def __init__(self):
    super().__init__(damage=3, status_time=5, name="Burn")

class Poison(DamageStatus):
  def __init__(self):
    super().__init__(damage=2, status_time=7, name="Poison")

class Scald(DamageStatus):
  def __init__(self):
    super().__init__(damage=5, status_time=7, name="Scald")

class Bond(HealStatus):
  def __init__(self):
    super().__init__(damage=25, status_time=1, name="Bond")

class Heal(HealStatus):
  def __init__(self):
    super().__init__(damage=20, status_time=1, name="Heal")
    
class Yin(DamageStatus):
  def __init__(self):
    super().__init__(damage=100, status_time=1, name="Yin")

class Yang(DamageStatus):
  def __init__(self):
    super().__init__(damage=75, status_time=1, name="Yang")

class Stun(StopStatus):
   def __init__(self):
     super().__init__(damage=0, status_time=2, name="Stun")

class Frozen(StopStatus):
   def __init__(self):
     super().__init__(damage=5, status_time=5, name="Frozen")

class Paralyzed(StopStatus):
   def __init__(self):
     super().__init__(damage=10, status_time=3, name="Paralyzed")

class Vines(StopStatus):
  def __init__(self):
    super().__init__(damage=1, status_time=3, name="Vines")

