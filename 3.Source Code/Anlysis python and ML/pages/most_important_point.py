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


# Create columns layout
c1, c33, c2 = st.columns([5, 1, 4]) 

with c1: 
    
    # Define bins and labels
    bins = [1.892, 47.7748, 182.22, 1000.127]  # Ensure values are in increasing order
    labels = ['low', 'medium', 'high']

    # Apply pd.cut to categorize the 'sales' column
    df['sales_category'] = pd.cut(df['sales'], bins=bins, labels=labels)

    # Create a pie chart using Plotly Express with custom size
    pie_chart = px.pie(df, names='sales_category', 
                        template='plotly_dark', 
                        hole=0.4, 
                        title='Sales Distribution',
                        color_discrete_sequence=px.colors.sequential.Electric_r,
                        width=550, height=550)  # Adjust width and height for smaller size
    st.plotly_chart(pie_chart)
    st.markdown(
        "<h3 style='text-align: left; color: white; font-family: Verdana, sans-serif;'>Sales Distribution</h3>",
        unsafe_allow_html=True
    )


with c2:
    # Create a bar chart for 'ship_mode' vs 'sales' with custom size
    bar_chart = px.bar(df.groupby('ship_mode')['sales'].mean().reset_index(), 
                        x="ship_mode", 
                        y="sales", 
                        title="Ship Mode vs Sales", 
                        color_discrete_sequence=px.colors.sequential.Electric_r, 
                        template="plotly_dark",
                        width=550, height=550)  # Adjust width and height for smaller size
    st.plotly_chart(bar_chart)

    # Add a centered markdown for additional insights
    st.markdown(
        "<h3 style='text-align: center; color: white; font-family: Arial, sans-serif; font-weight: bold;'>The best ship mode sales Second Class</h3>",
        unsafe_allow_html=True
    )



c1, c33, c2 = st.columns([5, 1, 4])

# First chart: Top 5 cities with the most amenities
with c1:
    

    city_profit_group = df.groupby('city')['sales'].mean().reset_index()

    top_cities = city_profit_group.sort_values(by='sales', ascending=False).head(10)
    fig = px.bar(top_cities, 
                x='city', 
                y='sales', 
                title='Top 10 Cities by mean sales', 
                labels={'sales': ' sales', 'city': 'City'},
                template='plotly_dark',
                color='sales',  
                color_discrete_sequence=px.colors.sequential.Electric_r , width=550, height=550) 

    st.plotly_chart(fig) 
    st.markdown(
        "<h3 style='text-align: left; color: white; font-family: Verdana, sans-serif;'>the best city for sales is nobelselvia </h3>",
        unsafe_allow_html=True
    )
    

with c2:
    st.plotly_chart(#profit vs region 
px.bar(df.groupby('region')['sales'].sum().reset_index(), x="sales", y="region", title=
       "region vs sales", color_discrete_sequence=px.colors.sequential.Electric_r , template="plotly_dark"
       , width=550, height=550))    

    st.markdown(
            "<h3 style='text-align: center; color: white; font-family: Arial, sans-serif; font-weight: bold;'>The best region sales is west</h3>",

            unsafe_allow_html=True
        )

c1, c33, c2 = st.columns([5, 1, 4])

with c1:
    st.plotly_chart(#profit vs sub_category
px.bar(df.groupby('sub-category')['sales'].mean().reset_index(), x="sub-category", y="sales", title=
       "sub_category vs sales", color_discrete_sequence=px.colors.sequential.Electric_r , template="plotly_dark")
       , width=550, height=550)

    st.markdown(
            "<h3 style='text-align: left; color: white; font-family: Verdana, sans-serif;'>the best saler is tables and chairs</h3>",

            unsafe_allow_html=True
        )
    
with c2:
    st.plotly_chart(px.line(df.groupby('year')['sales'].mean().reset_index().sort_values(by='year'), x="year", y="sales", title=
       "sales vs year", color_discrete_sequence=px.colors.sequential.Electric_r , template="plotly_dark")
       , width=550, height=550)

    st.markdown(
            "<h3 style='text-align: center; color: white; font-family: Arial, sans-serif; font-weight: bold;'>The best year sales is 2017</h3>",

            unsafe_allow_html=True
        )


# c1, c2, c3 = st.columns([1, 3, 1])  # c2 is wider, to center the content

# with c2:
#     # Line chart for sales vs quantity centered
#     st.plotly_chart(
#         px.line(df.groupby('quantity')['sales'].sum().reset_index().sort_values(by='quantity'), 
#                 x="quantity", 
#                 y="sales", 
#                 title="Sales vs Quantity", 
#                 color_discrete_sequence=px.colors.sequential.Electric_r, 
#                 template="plotly_dark",
#                 width=550, height=550)
#     )

#     # Centered markdown text below the chart
#     st.markdown(
#         """
#         <div style='text-align: center;'>
#             <h3 style='color: white; font-family: Verdana, sans-serif;'>The most quantity sales is 3</h3>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


