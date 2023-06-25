import random

class HangMan:
  potential_answers = ["awkward", "bagpipes", "banjo", "bungler", "crypt", "dwarves", "fishook", "haiku", "jazzy","kayak"]

  def __init__(self):
    self.lives = 6
    self.SUCCESS = False
    self.is_correct = []
    self.splitword = list(random.choice(self.potential_answers))

  def start(self, user_guess, lives, is_correct):
    self.printing(user_guess, is_correct)
    saved = False
    if lives > 0:
      a = 0 

      while a < len(self.splitword):
        letter = self.splitword[a]
        if user_guess == letter:
          is_correct.append(a)
          self.printing(user_guess, is_correct)
          saved = True
        a += 1

      if not saved:
        lives -= 1

      if len(is_correct) == len(self.splitword):
        print(" ")
        print("you win!")
        self.SUCCESS = True
        return

      print("guess a new letter")
      user_guess = input("")
      print (" ")
      print("lives: " + str(lives))
      self.start(user_guess, lives, is_correct)
    else:
      print("you failed to open the door, better luck next time!")
      print()

  def printing(self, user_guess, is_correct):
    final_print = []
    for i in range(len(self.splitword)):
      final_print.append('_')

    answer = self.splitword
    if not is_correct:
      print(' '.join(final_print))
      print(" ")
    else:
      for pos in is_correct:
        #replace final_print[pos] with correct letter
        final_print[pos] = answer[pos]
      print(' '.join(final_print))