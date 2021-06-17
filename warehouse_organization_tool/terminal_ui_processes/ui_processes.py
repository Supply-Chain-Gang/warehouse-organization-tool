from warehouse_organization_tool.utilities.data import InventoryManagement
import pandas as pd
import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.utilities.response_class import MenuResponseMethods as x

class Menu:
  """this class contains the initial options for a user in the terminal.
  """
  def __init__(self):
    self.initial_response_dict = {function[0].upper(): getattr(x,function) for function in dir(x) if not function.startswith('_')}
    self.prompt = """
*******************************************
  
    _      __             __                   
  | | /| / /__ ________ / /  ___  __ ________ 
  | |/ |/ / _ `/ __/ -_) _ \/ _ \/ // (_-< -_)
  |__/|__/\_,_/_/  \__/_//_/\___/\_,_/___|__/ 
    __  ___                           
    /  |/  /__ ____  ___ ____ ____ ____
  / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/
  /_/  /_/\_,_/_//_/\_,_/\_, /\__/_/   
                        /___/          

  Menu:
      S = Item(s) sold
      R = Item(s) recieved
      I = Show Inventory
      A = Run Inventory Analysis
      O = Optimize placement
      H = Help
      E = Exit
  *******************************************
  """

  def get_initial_user_decisions(self, inventory_manager):
    """this method gets user input and validates their response. it then calls the appropriate method in response.

    Args:
        inventory_manager (class): the inventory manager contains all information of items in inventory.

    Returns:
        [function return]: this method returns the return of the user response method.
    """
    print(self.prompt)
    user_response = UserInput.get_and_validate_input()
    if user_response == "I":
        return self.initial_response_dict[user_response](inventory_manager)
    return self.initial_response_dict[user_response]()
    
    
    