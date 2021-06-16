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
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    # fake data
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1

    ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
    ax1.set_title('Shaded')

    ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
    ax2.set_title('Not Shaded')

    plt.show()
    
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
