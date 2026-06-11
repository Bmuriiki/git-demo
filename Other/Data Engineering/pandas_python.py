# %%
import pandas as pd
#orders data analysis

# %%
orders= pd.read_excel(r'/Users/muriiki/Downloads/part-00000.txt', names= orders_columns)

# %%
orders_columns= ['orders_id', 'orders_date', 'customer_id', 'order_status']

# %%
orders

# %%
orders.columns

# %%
#Reading data from order_status columns
orders['order_status']

# %%
#Getting unique order status
orders['order_status'].unique()

# %%
#Getting data with Complete order status
orders_complete= df.query('order_status == "COMPLETE"')
orders_complete

# %%
#Getting complete orders for January 2014
orders.query('order_status == "COMPLETE" and order_date== "2014-01-01 00:00:00.0" ')

# %%
#Getting data with Complete/Closed order status
df.query('order_status == "COMPLETE" or order_status == "CLOSED"')

# %%
#Optimized query
orders.query('order_status == ("COMPLETE", "CLOSED")')

# %%
#Counting the orders by status
orders.groupby(by= 'order_status')['order_id'].agg('count')

# %%
#Get count by order month and then by order status
#First create a new column order month
orders['order_month']= orders.apply(lambda order: order['order_date'][:7], axis= 1)
#df['order_month'] = df.apply(lambda order: order['order_date'][:7], axis=1)
orders.groupby(['order_month', 'order_status'])['order_id'].agg('count')

# %%
customers= pd.read_csv(r'/Users/muriiki/Downloads/customer_data.txt', names= customer_columns)
customers

# %%
customer_columns= ['customer_id','customer_fname','customer_lname', 'customer_email','customer_password',
 'customer_street','customer_city','customer_state','customer_zipcode']

# %%
orders= orders.set_index('customer_id')
orders

# %%
#customers.set_index('customer_id')
#customers= customers.set_index('customer_id')
customers

# %%
orders.columns

# %%
#Joining tables
customer_orders= customers.join(orders, how= 'inner')
customer_orders

# %%
#Grouping and calculating number of orders per customer
customer_no_orders= customer_orders.reset_index('customer_id').groupby('customer_id')['customer_id'].agg(order_count='count').reset_index()
customer_no_orders

# %%
#Customers with orders greater than 10
customer_no_orders.query('order_count>10')

# %%
#Sorting orders
orders.sort_values('order_month', ascending= False)

# %%
# Import Operating system. os.makedirs creates a directory
import os
os.makedirs('/Users/muriiki/Desktop', exist_ok= True)

# %%
orders.to_json('/Users/muriiki/Desktop/orders-json', orient='records')

# %%



