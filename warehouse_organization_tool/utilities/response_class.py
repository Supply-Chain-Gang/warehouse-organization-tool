import pandas as pd
import numpy as np
import sys
import time
from warehouse_organization_tool.utilities.data import InventoryManagement
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.utilities.warehouse import Warehouse, Shelves


class MenuResponseMethods:
  def __init__(self):
    pass
  
  @staticmethod
  def s_get_items_sold():
    items_sold = {}
    while True:
      item_sold = input("What item did you sell? > ")
      amount = -int(input("How many sold? > "))
      items_sold[item_sold] = amount
      print(f"{-amount} {item_sold}(s) removed from inventory")
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
  def r_get_received_items():
    items_received = {}
    while True:
      item_received = input("What item did you receive? > ")
      amount = int(input("How many received? > "))
      items_received[item_received] = amount
      print(f"{items_received[item_received]} {item_received}(s) added to inventory")
      print(f"Would you like to record another transaction?")
      user_response = UserInput.get_and_validate_input()
      if user_response == 'Y':
        continue
      if (user_response == 'N'):
        print('Do you want to go to the main menu?')
        user_response = UserInput.get_and_validate_input()
        if user_response == 'N':
          sys.exit()
        return items_received
      
  
  @staticmethod
  def i_show_inventory(inventory_manager):
    print(inventory_manager.df.to_string(index=False))
  
  @staticmethod
  def a_show_fancy_stats():
    df = pd.read_csv('warehouse_organization_tool/notebooks/historical.csv')
    print("""
    
    
    ****INVENTORY STATS PER ITEM****
    
    
    """)
    print(df.groupby(df["item"]).inventory.agg(["mean","max"]).round())
    print("""
    
    
    ****SALES STATS PER ITEM****
    
    
    """)
    print(df.groupby(df["item"]).sales.agg(["mean","max"]).round())
    print("""
    
    
    ****BEST MONTH FOR EACH ITEM****
    
    
    """)
    print(df.loc[df.groupby("item")["sales"].idxmax()])
  
  
  @staticmethod
  def o_optimize_warehouse_placement():
    warehouse = Warehouse() 
    warehouse.place_shelves()
    warehouse.place_items()
    # we need some statistic for velocity or movement of each item in inventory. 

  
  @staticmethod
  def h_show_help():
    print("""
          Valid Commands
          --------------
          S = Amount of item(s) that have been sold in this session
          R = Amount of item(s) that have been received in this session
          I = Shows a list of your current inventory
          A = More in depth stats based on your inventory
          O = Optimizes placement of your inventory for best work flow
          """)
    time.sleep(2)
  
  @staticmethod
  def e_exit():
    print('See you next time!')
    sys.exit()