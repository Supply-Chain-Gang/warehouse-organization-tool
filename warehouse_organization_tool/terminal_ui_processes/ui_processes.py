import pandas as pd
import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.utilities.response_class import ResponseMethods

class InitialUserDecisions:
  def __init__(self):
    self.initial_response_dict = {
      'S': ResponseMethods.s_get_items_sold, 
      'R': ResponseMethods.r_get_recieved_items,
      'I': ResponseMethods.i_show_inventory,
      'A': ResponseMethods.a_show_fancy_stats,
      'O': ResponseMethods.o_optimize_warehouse_placement,
      'E': ResponseMethods.e_exit
      }
    self.prompt = """
  ***************************************
  Welcome:

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
    
    for response in self.initial_response_dict:
      if response == user_response:
        # call the method at the dictionary location
        self.initial_response_dict[response]()
    
    
    