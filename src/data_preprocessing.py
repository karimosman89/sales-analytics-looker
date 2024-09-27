import pandas as pd

def preprocess_sales_data(data):
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    data['Year'] = data['Order Date'].dt.year
    data['Month'] = data['Order Date'].dt.month
    data['Sales'] = data['Sales'].apply(lambda x: max(x, 0))  # Clean negative sales
    return data

