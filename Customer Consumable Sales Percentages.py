'''
Customer Consumable Sales Percentages

Following a recent advertising campaign, you have been asked to compare the sales of consumable products across all brands.

Compare the brands by finding the percentage of unique customers (among all customers in the dataset) who purchased consumable products from each brand.

Your output should contain the brand_name and percentage_of_customers rounded to the nearest whole number and ordered in descending order.
DataFrames: online_orders, online_products
Expected Output Type: pandas.DataFrame




online_orders
product_id:intpromotion_id:intcost_in_dollars:intcustomer_id:intdate:datetimeunits_sold:

online_products
product_id:intproduct_class:varcharbrand_name:varcharis_low_fat:varcharis_recyclable:varcharproduct_category:intproduct_family:varchar



'''

# Import your libraries
import pandas as pd

# Start writing code
online_orders.head()

dfo = online_orders
dfp = online_products

dfo = online_orders
dfp = online_products

dfpc = dfp[dfp['product_family'] == 'CONSUMABLE']

merg = pd.merge(dfo , dfpc, on='product_id').dropna()

gr = merg.groupby('brand_name')['customer_id'].nunique().to_frame('cnt').reset_index()


gr['percent'] = (gr['cnt'] / (merg['customer_id'].nunique()) *100) 
