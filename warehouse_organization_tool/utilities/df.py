import pandas as pd

class DataAnalytics:
  def __init__(self, df = None):
      if df is None:
        self.df = pd.read_csv('warehouse_organization_tool/notebooks/historical.csv')
      else:
        self.df = df

  def get_stats(self):
    sales_data = self.df.groupby(self.df["item"]).sales.agg(["std","mean","max"]).to_dict()

    inv_data = self.df.groupby(self.df["item"]).inventory.agg(["std","mean","max"]).to_dict()

    turnover_data = self.df.groupby(self.df["item"]).turnover.agg(["std","mean","max"]).to_dict()
    
    mean = sales_data['mean']
    items = list(mean.keys())

    item_sales_data = {item: {stat: sales_data[stat][item] for stat in sales_data  } for item in items}

    item_inv_data = {item: {stat: inv_data[stat][item] for stat in inv_data  } for item in items}

    item_turnover_data = {item: {stat: turnover_data[stat][item] for stat in turnover_data  } for item in items}
    return (item_sales_data, item_inv_data, item_turnover_data)
  
  def get_sorted_max(self):
    return self.df["turnover"].groupby(self.df['item']).max().sort_values(ascending=False).to_dict()
