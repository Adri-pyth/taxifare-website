import streamlit as st
import datetime
import requests
'''
# TaxiFareModel
'''
"\n"
"\n"
"\n"



"### Which date is the ride?"
d = st.date_input("",datetime.date.today())
st.write('Date :', d)
"\n"
'### What time?'
t = st.time_input("",datetime.datetime.now())
st.write('Time', t)
"\n"
"### Select pickup longitude"
pickup_longitude = st.number_input('', key="pickup_longitude", value=-73.950655)
st.write('The pickup longitude you chose is : ', pickup_longitude)
"\n"
"### Select pick up latitude"
pickup_latitude = st.number_input('', key="pickup_latitude", value=40.783282)
st.write('The pickup latitude you chose is : ', pickup_latitude)
"\n"
"### Select dropoff longitude"
dropoff_longitude = st.number_input('', key="dropoff_longitude", value=-73.984365)
st.write('The dropoff longitude you chose is : ', dropoff_longitude)
"\n"
"### Select dropoff latitude"
dropoff_latitude = st.number_input('', key="dropoff_latitude", value=40.769802)
st.write('The dropoff latitude you chose is : ', dropoff_latitude)
"\n"
"### Select the number of passengers"
passengers = st.slider("", 0, 10, 10)
st.write("You selected ", passengers, "passengers")



params = {"day_time": f"{d} {t}",
          "pickup_longitude": pickup_longitude,
          "pickup_latitude": pickup_latitude,
          "dropoff_longitude": dropoff_longitude,
          "dropoff_latitude": dropoff_latitude,
          "passengers": passengers}



url = "https://taxifare.lewagon.ai/predict"

response = requests.get(url, params=params)
prediction = response.json()

st.markdown(prediction)
st.markdown(params)
