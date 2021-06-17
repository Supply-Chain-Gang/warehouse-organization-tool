import pandas as pd
import numpy as np
import sys
import time
from warehouse_organization_tool.utilities.data import InventoryManagement
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.utilities.warehouse import Warehouse, Shelves


class MenuResponseMethods:
  """this class holds the methods for each thing that the user may want to do from the menu.
  """
  def __init__(self):
    pass
  
  @staticmethod
  def s_get_items_sold():
    """this method takes in the name of the item sold, and takes the given number of those items out of inventory.

    Returns:
        [dictionary]: returns a dictionary where the keys are the items sold and the values is the amount of that item that was sold.
    """
    items_sold = {}
    df = pd.read_csv('warehouse_organization_tool/notebooks/inventory.csv')
    sales_data = df.groupby(df["Item"]).Inventory.agg(["mean"]).to_dict()
    mean = sales_data['mean']
    items = list(mean.keys())
    while True:
      item_sold = input("What item did you sell? > ")
      if item_sold not in items:
        print("Item not in inventory")
        continue
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
    """this method takes in the name of the item recieved, and adds the given number of those items to inventory.

    Returns:
        [dictionary]: returns a dictionary where the keys are the items recieved and the values are the amount of that item that was recieved.
    """
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
    """this method prints the current inventory

    Args:
        inventory_manager (class): the inventory manager has all of the information about warehouse inventory.
    """
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
    """this method instantiates the warehouse, palces the shelves in the warehosue, and places all items in inventory on the optimal shelf.
    """
    warehouse = Warehouse() 
    warehouse.place_shelves()
    warehouse.place_items()

  
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