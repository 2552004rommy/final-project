import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image
df_machine= pd.read_csv(r"E:\depi\machine_sales.csv" , encoding = "ISO-8859-1")

df_machine.drop(columns=['row_id', 'order_id', 'order_date', 'ship_date',
                         'postal code', 'product name', 'sales_category',
                         'customer_name', 'customer_id' , 'product id'
                           , 'category' , 'country'], inplace=True)

st.title('Welcome to the  Prediction Page 📈  ')
import dill
import streamlit as st
import pathlib

dill.settings['ignore']=True

@st.cache(allow_output_mutation=True)
def load_preprocessor():
    preprocessor_file = pathlib.Path("E:/depi/preprocessor.pkl")
    with preprocessor_file.open('rb') as file:
        preprocessor = dill.load(file)
    return preprocessor

@st.cache(allow_output_mutation=True)
def load_model():
    model_file = pathlib.Path("E:/depi/rf1.pkl")
    with model_file.open('rb') as file:
        rf = dill.load(file)
    return rf

preprocessor = load_preprocessor()
rf = load_model()

ship_mode = st.selectbox('ship_mode' , df_machine['ship_mode'].unique())
segement = st.selectbox('segment' , df_machine['segment'].unique())
city  = st.selectbox('city' , df_machine['city'].unique())
state = st.selectbox('state' , df_machine['state'].unique())
region = st.selectbox('region' , df_machine['region'].unique())
sub_category = st.selectbox('sub-category' , df_machine['sub-category'].unique())
quantity = st.selectbox('quantity' , df_machine['quantity'].unique())
dis = st.selectbox('discount' , df_machine['discount'].unique())
profit = st.selectbox('discount' , df_machine['profit'].unique() )
year = st.selectbox('year' , df_machine['year'].unique())
month = st.selectbox('month' , df_machine['month'].unique())
day = st.selectbox('day' , df_machine['day'].unique())

new_data = pd.DataFrame({
    'ship_mode': [ship_mode],
    'segment': [segement],  # Corrected the spelling of 'segment'
    'city': [city],
    'state': [state],
    'region': [region],
    'sub-category': [sub_category],
    'quantity': [quantity],
    'discount': [dis],
    'profit': [profit],
    'year': [year],
    'month': [month],
    'day': [day]
})
transformed_data =  preprocessor.transform(new_data)

    # Predict using the model
prediction = rf.predict(transformed_data)
if st.button('Predict'):
    st.success(int(prediction[0]))

