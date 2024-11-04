import random

def main():
  opening()
  pc = int(input("Choose between 1-3: "))
  bc = random.randint(1, 3)
  choiceDisplay(pc, bc)
  process(pc, bc)

def opening():
  print("***ROCK PAPER SCISSORS***")
  print("1 = Rock")
  print("2 = Paper")
  print("3 = Scissors")

def choiceDisplay(pc, bc):
  print("Player Choice: " + str(pc))
  print("Computer Choice: " + str(bc))

def process(pc, bc):
  if pc == bc:
    print("TIE")
  elif pc == 1 and bc == 2 or pc == 2 and bc == 3 or pc == 3 and bc == 1:
    print("COMPUTER WINS")
  elif pc == 1 and bc == 3 or pc == 2 and bc == 1 or pc == 3 and bc == 2:
    print("PLAYER WINS")

main()