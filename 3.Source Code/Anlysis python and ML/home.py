import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image 

df = pd.read_csv(r"C:\Users\Maydoum\Downloads\Compressed\stores_sales_forecasting.csv" , encoding = "ISO-8859-1")
#rename columns
df.rename(columns = {'Row ID':'Row_ID','Order ID':'Order_ID','Order Date':'Order_Date','Ship Date':'Ship_Date',
                     'Ship Mode':'Ship_Mode','Customer ID':'Customer_ID','Customer Name':'Customer_Name',
                     'Segment':'Segment','Country':'Country','City':'City'}, inplace = True)
#lowercase all columns
df.columns = df.columns.str.lower()

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])       
#month year day 
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['day'] = df['order_date'].dt.day

# Custom CSS for background and text colors
st.markdown("""
    <style>
        .reportview-container {
            background-color: #1f1f1f;
            color: white;
        }
        h1 {
            color: #f63366;
        }
        h2 {
            color: #f63366;
        }
        .css-1d391kg {
            background-color: #333;
        }
        .st-ae {
            color: #f0f0f0;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #f63366; font-family: Georgia, serif;'>Welcome to the Home Page 🤓</h1>", unsafe_allow_html=True)
st.image("sales_forecasting_01_10ee95f93b.jpeg", use_column_width=True)

st.markdown("<h2 style='color: #f63366; font-family: Verdana, sans-serif;'>Explore Data</h2>", unsafe_allow_html=True)
st.write("<span style='color: red; font-family: Arial, sans-serif; font-size: 20px;'>Data link <a style='text-decoration: none; color: #2a9df4;' href='https://https://www.kaggle.com/datasets/tanayatipre/store-sales-forecasting-dataset'>here</a></span>", unsafe_allow_html=True)

sample = st.checkbox("Show Sample of Data")  
if sample:
    st.write(df.sample())

# Checkbox to show the head of the data
head = st.checkbox("Show Head of Data")
if head:
    st.write(df.head())    

about = st.checkbox("Show Information About All Columns")
if about:
    st.markdown(""""
    The dataset contains the following columns:
    - **Row ID**: A unique identifier for each row.
    - **Order ID**: The unique ID for each order.
    - **Order Date**: The date when the order was placed.
    - **Ship Date**: The date when the order was shipped.
    - **Ship Mode**: The shipping mode used (e.g., Standard Class, Second Class).
    - **Customer ID**: A unique identifier for each customer.
    - **Customer Name**: The name of the customer.
    - **Segment**: The customer segment (e.g., Consumer, Corporate).
    - **Country**: The country where the order was placed.
    - **City**: The city where the order was placed.
    - **State**: The state where the order was placed.
    - **Postal Code**: The postal code for the delivery.
    - **Region**: The region where the order was placed.
    - **Product ID**: A unique identifier for each product.
    - **Category**: The category of the product (e.g., Furniture, Office Supplies).
    - **Sub-Category**: The sub-category of the product.
    - **Product Name**: The name of the product.
    - **Sales**: The sales amount for the product.
    - **Quantity**: The number of products sold.
    - **Discount**: The discount applied to the product.
    - **Profit**: The profit earned from the product.
""")
