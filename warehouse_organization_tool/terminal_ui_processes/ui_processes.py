import pandas as pd
import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.utilities.response_class import MenuResponseMethods as x

class Menu:
  def __init__(self):
    self.initial_response_dict = {function[0].upper(): getattr(x,function) for function in dir(x) if not function.startswith('_')}
    self.prompt = """
  ***************************************
  Menu:

      S = Item(s) sold
      R = Item(s) recieved
      I = Show Inventory
      A = Run Inventory Analysis
      O = Optimize placement.

      H = Help
      E = Exit

  ***************************************
  """

  def get_initial_user_decisions(self):
    print(self.prompt)

    user_response = UserInput.get_and_validate_input()
    return self.initial_response_dict[user_response]()
    
    
    