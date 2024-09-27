import streamlit as st
import pandas as pd

st.title("Sales Data Preview")

# Load sales data locally for preview (or from BigQuery via bigquery_connector.py)
data = pd.read_csv('data/sales_data.csv')
st.write(data.head())

st.line_chart(data[['Order Date', 'Sales']].set_index('Order Date'))

