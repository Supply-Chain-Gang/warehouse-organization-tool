import numpy as np
from numpy.core import machar
import pandas as pd
from warehouse_organization_tool.utilities.df import DataAnalytics

class Warehouse:
  #all dimensions in inches
  def __init__(self, length=50, width=50, height=10, **kwargs):
    self.length = length*12
    self.width = width*12
    self.height = height*12
    self.area = length*width
    self.volume = self.area*height
    self.lane_width_size = 48
    self.x_grid_space = 0
    self.y_grid_space = 0
    self.z_grid_space = 0
    self.grid = None
    self.locations_of_items = {}
    self.data_analyzer = DataAnalytics()

    if 'lane_size' in kwargs:
      self.lane_width_size = kwargs['lane_size']*12

  def calculate_num_of_shelves(self):
    shelf = Shelves()
    num_shelves_back_wall = (self.width//shelf.length)*(self.height//shelf.height)
    x_shelves = (self.width - self.lane_width_size)//(shelf.length)
    y_shelves = (self.length - shelf.depth - self.lane_width_size)//(shelf.depth + self.lane_width_size)
    # z_shelves = (x_shelves + y_shelves + num_shelves_back_wall)*(self.height//shelf.height)
    z_shelves = (self.height//shelf.height)
    self.x_grid_space,self.y_grid_space,self.z_grid_space = x_shelves,y_shelves,z_shelves
    return x_shelves,y_shelves,z_shelves,num_shelves_back_wall

  def place_shelves(self):
    x,y,z,backwall = self.calculate_num_of_shelves()
    self.grid = np.zeros((self.x_grid_space,self.y_grid_space+1,self.z_grid_space), 'U32')
    # print(x,y,z,backwall)
    # print(self.grid)
    
  def place_items(self):
    #places items from left to right, front to back, bottom to top in order of highest to lowest item turnover
    max_turnover = self.data_analyzer.get_sorted_max()
    items = max_turnover.keys()
    # entry_point = self.x_grid_space // 2
    
    # self.grid[entry_point][self.y_grid_space][0] = 'babies'
    # print(self.grid)
    
    for item in items:
      x,y,z = 0,self.y_grid_space,0
      while True:
        shelf_has_item = self.grid[x][y][z]
        #if there is nothing on the shelf, the if statement will evaluate to True
        if not shelf_has_item:
          self.grid[x][y][z] = item
          print(f'placed {item}')
          self.locations_of_items[item] = (x,y,z)
          break
        
        if x < self.x_grid_space-1:
          x += 1
          continue
        
        if y > 0:
          x = 0
          y -= 1
          continue
        
        if z < self.z_grid_space-1:
          x = 0
          y = self.y_grid_space
          z += 1
          continue
        
    print(self.grid)
    print(self.locations_of_items['Coolers'])
    # for item in items:
    #   for p_item in placed_items:
    #     if not item in p_item:
    #       x = entry_point
          # while some_condition:
          #   #incriment x or y or z until you find an empty position
          # placed_items.append(item)
          # occupied_loc.append((x,y,z))
    

class Shelves:
  def __init__(self, length=10,depth=4,height=5):
    self.length = length*12
    self.depth = depth*12
    self.height = height*12
    self.footprint = self.length*self.depth