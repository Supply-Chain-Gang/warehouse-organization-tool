import pandas as pd
import numpy as np
from warehouse_organization_tool.utilities.user_input import UserInput
from warehouse_organization_tool.terminal_ui_processes.ui_processes import Menu

def main():
  menu = Menu()
  while True:
    csv_count_update = menu.get_initial_user_decisions()
    if csv_count_update:
      pass
      #do csv update stuff here

if __name__ == '__main__':
  main()
  