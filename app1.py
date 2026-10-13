import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import pickle
#import base64


st.set_page_config(page_title='Swiggy EDT Prediction',
                   page_icon="🛵",
                   layout='wide'
                   )

with st.sidebar:

    st.markdown("""
        <h1 style="color:#ff5a00; text-align:center;">
             SWIGGY
        </h1>
        <hr>
    """, unsafe_allow_html=True)

    st.subheader("Business Overview")

    # Business Problem
    with st.expander(" Business Problem", expanded=True):
        st.write("""
        Swiggy needs to predict the delivery time for food orders
        accurately to improve customer experience, optimize operations,
        and reduce cancellations.

        The goal is to provide reliable and timely deliveries using
        historical data and machine learning techniques.
        """)

    # Sources of Uncertainty
    with st.expander("Sources of Uncertainty"):
        st.markdown("""
        - Highly variable traffic patterns
        - Weather events (Rain, Storms, Fog)
        - Restaurant preparation variability
        - Rider behaviour and skill
        - Order batching (Multiple deliveries)
        """)

    # Impact of inaccurate ETA
    with st.expander("Impact of Inaccurate ETAs"):
        st.markdown("""
        - Reduced customer trust and lower repeat orders
        - Increased cancellations and refund costs
        - Higher support volume and operational interventions
        """)

    with st.expander('Problem Statement'):
        st.write('''
                Swiggy’s objective is to predict the delivery time (minutes) per order at the moment of order placement 
                with **business-grade accuracy**. This allows the platform to:
                    - **(a)** Show reliable ETAs to customers.
                    - **(b)** Optimize rider allocation and reduce idle costs.
                ''')

    

st.title('Swiggy Delivery Time Prediction')



st.image(r"C:\Users\shrut\Downloads\swiggy_delivery_extra_wide (1).png",width=700)



df = pd.read_csv(r"C:\\Users\shrut\\OneDrive\\504\\ML\Dataset\swiggy_demographic.csv")
df.dropna(inplace=True)

with open(r'swiggy_dtp.pkl', mode='rb') as file:
    Model = pickle.load(file)



    st.subheader(" Estimated Delivery Time")
    st.write("Enter the required details to predict the delivery time.")


    col1,col2,col3=st.columns(3)
    with col1:
        age = st.number_input('**Enter the age**',min_value=0, max_value=100, value=18)
        ratings = st.number_input('**What is the rider ratings**',min_value=0, max_value=5,value=3)
        multiple_deliveries = st.number_input('**Multiple deliveries (0,1,2,3)**', min_value=0, max_value=3,value=0)
        weekend = st.number_input('**Is there a weekend (Yes-0/No-1)**', min_value=0, max_value=1,value=0)
        pickup_time = st.number_input('**Pickup time minutes (in minute)**',min_value=0, max_value=60,value=10)
        distance = st.number_input('**Order distance**',min_value=0, max_value=25,value=15)
    
    with col2:
        order_day = st.number_input('**Enter the day**', min_value=1, max_value=31)
        weather = st.selectbox("**Weather Condition**",df['weather'].unique())
        traffic = st.selectbox("**Traffic Status**",df['traffic'].unique())
        festival = st.selectbox("**Festival season**", df['festival'].unique())
        city_type = st.selectbox("**What is your city location/ type of city**",df['city_type'].unique())
        order_day_of_week = st.selectbox("**Order day of week**", df['order_day_of_week'].unique())


    with col3:
        order_time_hour = st.number_input('**What is the order time (in hour)**',min_value=0, max_value=24,value=1)
        vehicle_condition = st.selectbox('**Condition of the rider vehicle**', df['vehicle_condition'].unique())
        type_of_order = st.selectbox("**Food type**", df['type_of_order'].unique())
        vehicle_type = st.selectbox('**Vehicle Type**', df['type_of_vehicle'].unique())
        order_time_of_day=st.selectbox('**Order_time_of_day**',df['order_time_of_day'])
        city_name = st.selectbox("**Choose your city**", df['city_name'].unique())
        



    input_data = pd.DataFrame({'age': [age],'ratings': [ratings],'multiple_deliveries': [multiple_deliveries],
                                'is_weekend':[weekend],'pickup_time_minutes':[pickup_time], 
                                'distance': [distance], 'order_time_hour': [order_time_hour], 
                                'vehicle_condition' : [vehicle_condition], 'order_day':[order_day],
                'weather':[weather], 'traffic': [traffic], 'festival':[festival], 'city_type':[city_type],
                'order_day_of_week': [order_day_of_week],'city_name': [city_name], 'type_of_order': [type_of_order],
                'type_of_vehicle': [vehicle_type],'order_time_of_day':[order_time_of_day]})

    if st.button('**Predict**',width='stretch',type='secondary'):

        if None in [age, ratings, distance, pickup_time, order_time_hour]:
            st.warning("**First give some input to get result**")
        else:
            result = float(Model.predict(input_data)[0])
            st.success(f"**Your order will be delivered in {round(result)} min.**",width='stretch')

    