import pandas as pd

class DataAnalytics:
  def __init__(self):
      self.df = pd.read_csv('warehouse_organization_tool/notebooks/historical.csv')

  def get_stats(self):
    sales_data = self.df.groupby(self.df["item"]).sales.agg(["std","mean"]).to_dict()

    inv_data = self.df.groupby(self.df["item"]).inventory.agg(["std","mean"]).to_dict()

    turnover_data = self.df.groupby(self.df["item"]).turnover.agg(["std","mean"]).to_dict()
    
    mean = sales_data['mean']
    items = list(mean.keys())

    item_sales_data = {item: {stat: sales_data[stat][item] for stat in sales_data  } for item in items}

    item_inv_data = {item: {stat: inv_data[stat][item] for stat in inv_data  } for item in items}

    item_turnover_data = {item: {stat: turnover_data[stat][item] for stat in turnover_data  } for item in items}
    return (item_sales_data, item_inv_data, item_turnover_data)
