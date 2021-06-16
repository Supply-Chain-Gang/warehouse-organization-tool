# %%
from warehouse_organization_tool.utilities.warehouse import Warehouse
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# %%
class Warehouse_Visualization(Warehouse):
  def __init__(self,**kwargs):
      super().__init__(**kwargs)
      
  def calculate_x_pos(self):
    scaling_factor = self.shelves.length
    xpos = []

    for i in range(self.y_grid_space+1):
      counter = 0
      for j in range(1,self.x_grid_space+1):
        
        if (i == self.y_grid_space) and (j == ((self.x_grid_space // 2)+1)):
          xpos.append(counter+scaling_factor)
          counter += scaling_factor
        
        if j == (self.x_grid_space // 2)+1:
          xpos.append((self.width-counter))
          counter += (scaling_factor*2)
          continue

        if j == 1:
          xpos.append(0)
          counter += scaling_factor
          continue
        
        if (i == 5) and (j==4):
          counter-=scaling_factor

        xpos.append(counter)
        counter += scaling_factor

    return xpos
  
  def calculate_y_pos(self):
    
    ypos = []
    counter = 0
    scaling_factor = (self.shelves.depth + self.lane_width_size)

    for _ in range(self.y_grid_space+1):
      for _ in range(self.x_grid_space):
        ypos.append(1+counter)
      counter += scaling_factor
    ypos.append(1+counter-scaling_factor)
    
    return ypos
  
  def calculate_z_pos(self):
    zpos = (self.x_grid_space*(self.y_grid_space+1)) + 1
    return zpos

  def plot_grid(self):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")

    ax.set_xlabel("Width of room in inches")
    ax.set_ylabel("Length of room in inches") 
    ax.set_zlabel("height of room in inches")
    ax.set_xlim3d(0,self.width)
    ax.set_ylim3d(0,self.length)
    ax.set_zlim3d(0,self.height) 

    ypos = self.calculate_y_pos()
    zpos = np.zeros(self.calculate_z_pos())
    xpos = self.calculate_x_pos()

    dx = [self.shelves.length-20]
    dy = [self.shelves.depth]
    dz = [self.shelves.height for _ in range(2)]

    _zpos = zpos   # the starting zpos for each bar
    colors = ['b','r']
    for i in range(2):
        ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i], alpha=0.6)
        _zpos += dz[i]    # add the height of each bar to know where to start the next

    plt.gca().invert_xaxis()
    plt.show()

if __name__ == "__main__":
  warehouse = Warehouse_Visualization()
  place_shelves = warehouse.place_shelves()
  warehouse.plot_grid()

# %%
