#Define the base class Player
class Player:
  def play(self):
      print("The player is playing cricket.")
      
#Define the derived class Batsman
class Batsman(Player):
  def play(self):
      print("The batsman is bating.")

#Define the derived class Bowler
class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

#Create object of Batsman and Bowler classes
batsman = Batsman()
bowler =Bowler()

batsman.play()
bowler.play()