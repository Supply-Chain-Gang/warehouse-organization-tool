import pandas as pd
import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.terminal_ui_processes.ui_processes import InitialUserDecisions

def main():
  user_decisions = InitialUserDecisions()
  while True:
    user_decisions.get_initial_user_decisions()
    break
    

if __name__ == '__main__':
  main()
  