import streamlit as st
import numpy as np
import pandas as pd
import joblib
import time

# Load the model
model = joblib.load('linear_regression_model_financial.pkl')

# App Title
st.image("2.jpg",width=200,use_column_width=20)
st.title('Financial Portfolio Returns Predictor')

Historical_Volatility = st.slider('Historical Volatility (%)')
Interest_Rate = st.slider('Interest Rate (%)')
Inflation_Rate = st.slider('Inflation Rate (%)')
GDP_Growth = st.slider('GDP Growth (%)')
Unemployment_Rate = st.slider('Unemployment Rate (%)')
Asset_Class = st.selectbox('Asset Class',["Bonds","Cash","Commodities","Equities","Real Estate"])

#dataframe
input_data = pd.DataFrame({
    'Historical_Volatility' : [Historical_Volatility],
    'Interest_Rate' : [Interest_Rate],
    'Inflation_Rate' :[Inflation_Rate],
    'GDP_Growth' : [GDP_Growth],
    'Unemployment_Rate' : [Unemployment_Rate],
    'Asset_Class_Bonds' : [1 if Asset_Class == 'Bonds' else 0],
    'Asset_Class_Cash' : [1 if Asset_Class == 'Cash' else 0],
    'Asset_Class_Commodities' : [1 if Asset_Class == 'Commodities' else 0],
    'Asset_Class_Equities' : [1 if Asset_Class == 'Equities' else 0],
    'Asset_Class_Real Estate' : [1 if Asset_Class == 'Real Estate' else 0]
})

# Prediction
if st.button('Predict'):
    
    financial = model.predict(input_data)
    print(financial)
    st.balloons()
    st.snow()
    st.write("Financial Portfolio Return :",financial)
    st.success("Financial Portfolio Return Prediction Successfully !")
    
