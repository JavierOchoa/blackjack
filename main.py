import random
from art import logo

def add(n1, n2):
  return n1 + n2

def randomp2():
  return random.choice(deck)

def pcDeck():
  total = 0
  for number in pcHand:
    total += number
    if total < 21:
      pcHand.append(random.choice(deck))
  return total

print(logo)
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

pc1 = random.choice(deck)
print(f"PC card is {pc1}\n\n")

p1 = random.choice(deck)
p2 = random.choice(deck)

pcHand = [pc1,]

isFinished = False
userElegible = True
pcElegible = True

while not isFinished:

  userScore = add(p1, p2)

  print(f"Your cards are [{p1}, {p2}] with a score of {userScore} ")

  if userScore > 21:
    userElegible = False
    isFinished = True
    print("PC Win D:")
  else:
    again = input("Wanna keep playin? Y/N: ").lower()

    if again == "y":
      isFinished = False
      p1 = userScore
      p2 = randomp2()
    elif again == "n":
      isFinished = True
      pcFinalDeck = pcDeck()
      pcFinalHand = print(f"PC final deck is {pcHand}, with a score of {pcFinalDeck}")

      if userScore > 21:
        userElegible = False

      if pcFinalDeck > 21:
        pcElegible = False  

      if userElegible and pcElegible:
        if userScore > pcFinalDeck:
          print("You WIN :D")
        elif pcFinalDeck > userScore:
          print("PC Win D:")
        elif userScore == pcFinalDeck:
          print("DRAAAWW")
      elif userElegible and not pcElegible:
        print("You WIN :D")
      elif pcElegible and not userElegible:
        print("PC Win D:")
