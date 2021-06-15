import pandas as pd
import numpy as np


class InventoryManagement:
  def __init__(self):
    self.df = None
  

  def load_inventory(self):
    self.df = pd.read_csv('warehouse_organization_tool/notebooks/inventory.csv', dtype={"Current Inv": int, "Sales": int, "Recieved": int})

  def update_inventory(self, values_to_update = None):
    if values_to_update:
      for item in values_to_update:
        named_item = (self.df['Item'] == item)
        self.df.loc[named_item, "Current Inv"] += values_to_update[item]
    return self.df


  def update_csv(self):
    self.df.to_csv('warehouse_organization_tool/notebooks/inventory.csv', index=False)