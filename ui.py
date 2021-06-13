import pandas as pd
import numpy as np

print("""
***************************************
Welcome:

    S = Item(s) sold
    R = Item(s) recieved
    I = Show Inventory
    A = Run Inventory Analysis
    O = Optimize placement.

    H = Help

***************************************
""")

class UserInput:
  def __init__(self):
    self.valid_initial_response = ["S", "R", "I", "A", "O"]

  @staticmethod
  def get_and_validate_input(self):
    response = input("> ").upper()
    while True:
      if not response in self.valid_initial_response:
        print("Response not valid")
        response = input("> ").upper()
        continue
      break
    return response


  def help():
    response = input("> ")
    if response == 'H':
      print("""
      We all need a little help sometimes
      """
      )
response = UserInput.get_and_validate_input()
if response == 'S':
  while True:
    item_sold = input("What item did you sell? > ")
    amount = input("How many sold? > ")
    print(f"{amount} {item_sold}(s) removed from inventory")
    print(f"Would you like to record another transaction?")


if response == 'R':
  pass

if response == 'I':
  inventory = pd.read_csv('./inventory.csv')
  
  print(inventory.head(50))

if response == 'A':
  pass

if response == 'O':
  pass


  