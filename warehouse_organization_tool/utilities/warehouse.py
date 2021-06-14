import numpy as np
import pandas as pd

class Warehouse:
  #all dimensions in inches
  def __init__(self, length=50, width=50, height=50, **kwargs):
    self.length = length*12
    self.width = width*12
    self.height = height*12
    self.area = length*width
    self.volume = self.area*height
    self.lane_width_size = 48
    self.x_grid_space = 0
    self.y_grid_space = 0
    self.z_grid_space = 0
    self.grid = np.zeros((self.x_grid_space,self.y_grid_space+1,self.z_grid_space))

    if 'lane_size' in kwargs:
      self.lane_width_size = kwargs['lane_size']*12

  def calculate_num_of_shelves(self):
    shelf = Shelves()
    num_shelves_back_wall = (self.width//shelf.length)*(self.height//shelf.height)
    x_shelves = (self.width - self.lane_width_size)//(shelf.length)
    y_shelves = (self.length - shelf.depth - self.lane_width_size)//(shelf.depth + self.lane_width_size)
    z_shelves = (x_shelves + y_shelves + num_shelves_back_wall)*(self.height//shelf.height)
    self.x_grid_space,self.y_grid_space,self.z_grid_space = x_shelves,y_shelves,z_shelves
    return x_shelves,y_shelves,z_shelves,num_shelves_back_wall

  # TODO
  def place_shelves(self):
    x,y,z,backwall = self.calculate_num_of_shelves()
    print("Warehouse Grid",self.grid)
    print(x,y,z,backwall)
    # Need a dictionary of the total num of items, total quantity of each item, and the total sales volume of each item

class Shelves:
  def __init__(self, length=10,depth=4,height=5):
    self.length = length*12
    self.depth = depth*12
    self.height = height*12
    self.footprint = self.length*self.depth
      