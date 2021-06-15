# import pandas as pd
# import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.terminal_ui_processes.ui_processes import Menu
from warehouse_organization_tool.utilities.data import InventoryManagement

class UpdateInformation:
  def __init__(self):
    self.item_for_update = {}

def main():
  menu = Menu()
  update_info = UpdateInformation()
  inventory_manager = InventoryManagement()
  inventory_manager.load_inventory()
  
  while True:
    csv_count_update = menu.get_initial_user_decisions(inventory_manager)
    # print(csv_count_update)
    if csv_count_update:
      for item in csv_count_update:
        if item in update_info.item_for_update:
          update_info.item_for_update[item] += csv_count_update[item]
          continue
        update_info.item_for_update[item] = csv_count_update[item]
    print(csv_count_update)
    print(update_info.item_for_update)
    inventory_manager.update_inventory(csv_count_update)

if __name__ == '__main__':
  main()
  
#   update_csv()
#     pass 