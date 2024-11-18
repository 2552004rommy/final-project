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
orders_by_year= df.groupby('year')['order_id'].count().reset_index().sort_values(by = 'year' , ascending=False)
month_group = df.groupby('month')['order_id'].count().reset_index().sort_values(by = 'month' , ascending=False)
day_group = df.groupby('day')['order_id'].count().reset_index().sort_values(by = 'day' , ascending=False)

st.markdown("<h1 style='text-align: center; color: #f63366;'>Interactive Analysis</h1>", unsafe_allow_html=True)
# image = Image.open(r"E:\depi\explore-data-with-power-bi-desktop-social.png")
# st.image(image, use_column_width=True)
st.video("E:\depi\Data Analysis Processing Animation - Free Download People Animations.mp4")
selection = st.selectbox("select column you want see visulaztion" ,
                        ['year', 'month', 'day', 'Ship Mode'
       , 'Segment',  'City', 'State'
       , 'Region', 'Sub-Category',
       'Sales', 'Quantity', 'Discount', 'Profit'])

if selection == 'year':
    st.plotly_chart(px.line(orders_by_year, x="year", y="order_id", title="year distribution"
            , color_discrete_sequence=px.colors.sequential.Electric_r , 
            template="plotly_dark"))
elif selection == 'month':
    st.plotly_chart(px.line(month_group, x="month", y="order_id", title="month distribution"
            , color_discrete_sequence=px.colors.sequential.Electric_r , 
            template="plotly_dark"))
elif selection == 'day':
   st.plotly_chart( px.line(day_group, x="day", y="order_id", title="day distribution"
            , color_discrete_sequence=px.colors.sequential.Electric_r , 
            template="plotly_dark"))
   
elif selection == 'Ship Mode':
    st.plotly_chart(px.bar(df['ship_mode'].value_counts(),
                            x=df['ship_mode'].value_counts().index,
                              y=df['ship_mode'].value_counts().values
                             , template="plotly_dark" ,
                               color_discrete_sequence=px.colors.sequential.Electric_r))
elif selection == 'Segment':
    st.plotly_chart(px.bar(df['segment'].value_counts(),
                            x=df['segment'].value_counts().index
                            , y=df['segment'].value_counts().values
                            , template="plotly_dark" ,
                               color_discrete_sequence=px.colors.sequential.Electric_r))  
elif selection == 'City':
    city_group = df.groupby('city')['order_id'].count().reset_index().sort_values(by = 'order_id' , ascending=False).head(10)

    st.plotly_chart(px.bar(city_group, x="city",
                            y="order_id", title="city distribution" ,
                              template="plotly_dark"))
elif selection == 'State':
    state_group = df.groupby('state')['order_id'].count().reset_index().sort_values(by = 'order_id' , ascending=False).head(10)

    st.plotly_chart(px.bar(state_group, x="state", y="order_id",
                            title="state distribution" , template="plotly_dark"))
elif selection == 'Region':
    st.plotly_chart(px.bar(df['region'].value_counts(), x=df['region'].value_counts().index,
                            y=df['region'].value_counts().values ,
                              template="plotly_dark" , color_discrete_sequence=px.colors.sequential.Electric_r) )      
elif selection == 'Sub-Category':
    st.plotly_chart(px.bar(df['sub-category'].value_counts(), x=df['sub-category'].value_counts().index,
        y=df['sub-category'].value_counts().values 
       , template="plotly_dark" , color_discrete_sequence=px.colors.sequential.Electric_r))
elif selection == 'Sales':
    st.plotly_chart(px.box(df , x = 'sales' , template='plotly_dark' , color_discrete_sequence=px.colors.sequential.Electric_r)
                    ) 
elif selection == 'Quantity':
    st.plotly_chart(px.histogram(df , x = 'quantity' , template='plotly_dark' ,
              color_discrete_sequence=px.colors.sequential.Electric_r)
              )
elif selection == 'Discount':
    st.plotly_chart(px.histogram(df , x = 'discount' , template='plotly_dark' ,
              color_discrete_sequence=px.colors.sequential.Electric_r)
              )    
elif selection == 'Profit':

    bins = [-81.94, -1.826, 7.7748, 1013.127]  # All values must be in increasing order
    labels = ['low', 'medium', 'high']

# Apply pd.cut to categorize the 'sales' column
    df['sales_category'] = pd.cut(df['sales'], bins=bins, labels=labels)
    st.plotly_chart(px.pie(df, names='sales_category', 
             template='plotly_dark', 
            hole=0.4, 
            title='profit distribution',color_discrete_sequence=px.colors.sequential.Electric_r))
    
# Create a pie chart using Plotly Express
    

