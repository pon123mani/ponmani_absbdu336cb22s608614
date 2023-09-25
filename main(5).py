
class player:
  def play(self):
    print("the player is playing circket")
class Batsman(player):
  def play(self):
    print("the batsman is batting")
class Blower(player):
  def play(self):
    print("the blower is blowing")
batsman=Batsman()
blower=Blower()
    
    