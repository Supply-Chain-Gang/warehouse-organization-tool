# %%
from warehouse_organization_tool.utilities.warehouse import Warehouse
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# %%
class Warehouse_Visualization(Warehouse):
  def __init__(self,**kwargs):
      super().__init__(**kwargs)

  def plot_grid(self):
    # fig = plt.figure(figsize=(8, 3))
    # ax1 = fig.add_subplot(121, projection='3d')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")

    ax.set_xlabel("x")
    ax.set_ylabel("y") 
    ax.set_zlabel("z")
    ax.set_xlim3d(0,11)
    ax.set_ylim3d(0,21) 

    xpos = [1,3,7,9,1,3,7,9,1,3,7,9,1,3,7,9,1,3,7,9,1,3,5,7,9]
    ypos = [1,1,1,1,5,5,5,5,9,9,9,9,13,13,13,13,17,17,17,17,21,21,21,21,21]
    zpos = np.zeros(25)

    # xpos = [1,2]
    # ypos = [1,2]
    # zpos = [1,2] 

    # xpos = [2,5,8,2,5,8,2,5,8]
    # ypos = [1,1,1,5,5,5,9,9,9]
    # zpos = np.zeros(9)

    # dx = np.ones(self.x_grid_space * self.y_grid_space)
    # dy = np.ones(self.x_grid_space * self.y_grid_space)
    # dz = [1 for _ in range(self.x_grid_space * self.y_grid_space)]  # the heights of the 4 bar sets

    dx = [1]
    dy = [1]
    dz = [1 for _ in range(2)]

    _zpos = zpos   # the starting zpos for each bar
    colors = ['b','r']
    for i in range(2):
        ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i], alpha=0.6)
        _zpos += dz[i]    # add the height of each bar to know where to start the next

    plt.gca().invert_xaxis()
    plt.show()


    # # fake data
    # _x = np.arange(4)
    # _y = np.arange(5)
    # _xx, _yy = np.meshgrid(_x, _y)
    # x, y = _xx.ravel(), _yy.ravel()

    # top = x + y
    # bottom = np.zeros_like(top)
    # width = depth = 1

    # ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
    # ax1.set_title('Shaded')

    # plt.show()
    
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111, projection='3d')

    # xpos = [x for x in range(self.x_grid_space)]
    # ypos = [y for y in range(self.y_grid_space)]
    # zpos = [0 for _ in range(self.z_grid_space)]

    # dx = np.ones(len(xpos))
    # dy = np.ones(len(ypos))
    # dz = [self.z_grid_space for _ in range(self.x_grid_space)]

    # ax1.bar3d(xpos,ypos,zpos,dx,dy,dz)

    # # plt.get_current_fig_manager().show()
    # plt.show()

if __name__ == "__main__":
  warehouse = Warehouse_Visualization()
  place_shelves = warehouse.place_shelves()
  warehouse.plot_grid()

# %%
