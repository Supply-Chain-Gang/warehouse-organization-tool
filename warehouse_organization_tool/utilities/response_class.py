import pandas as pd
import numpy as np
import sys
from warehouse_organization_tool.utilities.user_input import UserInput


class MenuResponseMethods:
  def __init__(self):
    pass
  
  @staticmethod
  def s_get_items_sold():
    items_sold = {}
    while True:
      item_sold = input("What item did you sell? > ")
      amount = input("How many sold? > ")
      items_sold[item_sold] = amount
      print(f"{amount} {item_sold}(s) removed from inventory")
      print(f"Would you like to record another transaction?")
      user_response = UserInput.get_and_validate_input()
      if user_response == 'Y':
        continue
      if (user_response == 'N'):
        print('Do you want to go to the main menu?')
        user_response = UserInput.get_and_validate_input()
        if user_response == 'N':
          sys.exit()
        return items_sold
  
  @staticmethod
  def r_get_recieved_items():
    items_recieved = {}
    while True:
      item_recieved = input("What item did you recieve? > ")
      amount = input("How many recieved? > ")
      items_recieved[item_recieved] = amount
      print(f"{items_recieved[item_recieved]} {item_recieved}(s) added to inventory")
      print(f"Would you like to record another transaction?")
      user_response = UserInput.get_and_validate_input()
      if user_response == 'Y':
        continue
      if (user_response == 'N'):
        print('Do you want to go to the main menu?')
        user_response = UserInput.get_and_validate_input()
        if user_response == 'N':
          sys.exit()
        return items_recieved
  
  @staticmethod
  def i_show_inventory():
    inventory = pd.read_csv('warehouse_organization_tool/notebooks/inventory.csv')  
    print(inventory)
  
  @staticmethod
  def a_show_fancy_stats():
    pass
  
  
  @staticmethod
  def o_optimize_warehouse_placement():
    # we need some statistic for velocity or movement of each item in inventory. 
    pass
  
  @staticmethod
  def h_show_help():
    print("""
          give more in depth explainations of what each choice does
          """)
  
  @staticmethod
  def e_exit():
    print('See you next time!')
    sys.exit()