import random

# ------------------------------------------------------------------------------
#array:
valchars = [
  "Brimstone",
  "Viper",
  "Omen",
  "Killjoy",
  "Cypher",
  "Sova",
  "Sage",
  "Phoenix",
  "Jett",
  "Reyna",
  "Raze",
  "Breach",
  "Skye",
  "Yoru",
  "Astra",
  "KAY/O",
  "Chamber",
  "Neon",
  "Fade",
  "Harbor",
  "Gekko",
  "Deadlock",
  "Iso",
  "Clove",
  "Vyse",
  "Tejo",
  "Waylay",
  "Veto",
  "Miks"
]

# ------------------------------------------------------------------------------
#question:
def yes_no(question):
    
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print(random.choice(valchars), " (press enter to close)")
            input()
            break

        else:
            print("you're literally stupid i said type Y  (press enter to close)")
            input()
            break

# ------------------------------------------------------------------------------
#ask the user
yes_no("type Y to pick a valorant character: ")





# --- made by nate ---