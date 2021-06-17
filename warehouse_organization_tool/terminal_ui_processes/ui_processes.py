from warehouse_organization_tool.utilities.welcome_screen.welcome_screen import WelcomeScreen
from warehouse_organization_tool.utilities.data import InventoryManagement
import pandas as pd
import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.utilities.response_class import MenuResponseMethods as x

class Menu:
  def __init__(self):
    self.initial_response_dict = {function[0].upper(): getattr(x,function) for function in dir(x) if not function.startswith('_')}

  def get_initial_user_decisions(self, inventory_manager):
    WelcomeScreen.print_prompt()
    user_response = UserInput.get_and_validate_input()
    if user_response == "I":
        return self.initial_response_dict[user_response](inventory_manager)
    return self.initial_response_dict[user_response]()
    
    
    