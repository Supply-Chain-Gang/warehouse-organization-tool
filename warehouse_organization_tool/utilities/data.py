import pandas as pd
import numpy as np


class InventoryManagement:
  """this class is an interface between the csv and user input.
  """
  def __init__(self):
    self.df = None
  

  def load_inventory(self):
    """this method loads the data into a dataframe.
    """
    self.df = pd.read_csv('warehouse_organization_tool/notebooks/inventory.csv', dtype={"Inventory": int, "Sales": int, "Recieved": int})

  def update_inventory(self, values_to_update = None):
    """this method takes user input and writes to the csv.

    Args:
        values_to_update ([dictionary], optional): contains the names and values of inventory items to update. Defaults to None.

    Returns:
        [dataframe]: returns a dataframe that contains inventory after update.
    """
    if values_to_update:
      for item in values_to_update:
        named_item = (self.df['Item'] == item)
        self.df.loc[named_item, "Inventory"] += values_to_update[item]
    return self.df


  def update_csv(self):
    """this method actually does the overwriting of the csv with the data in the dataframe.
    """
    self.df.to_csv('warehouse_organization_tool/notebooks/inventory.csv', index=False)