import streamlit as st
import datetime
import requests
import streamlit as st
import pandas as pd
'''
# TaxiFareModel
'''
"\n"
"\n"
"\n"



"### Which date is the ride?"
d = st.date_input("",datetime.date.today())
"\n"
'### What time?'
t = st.time_input("",datetime.datetime.now())
"\n"
"### Select pickup longitude"
pickup_longitude = st.number_input('', key="pickup_longitude", value=-73.950655)
"\n"
"### Select pick up latitude"
pickup_latitude = st.number_input('', key="pickup_latitude", value=40.783282)
"\n"
"### Select dropoff longitude"
dropoff_longitude = st.number_input('', key="dropoff_longitude", value=-73.984365)
"\n"
"### Select dropoff latitude"
dropoff_latitude = st.number_input('', key="dropoff_latitude", value=40.769802)
"\n"

df = pd.Dataframe({"pickup_longitude": pickup_longitude,
                   "pickup_latitude": pickup_latitude,
                   "dropoff_longitude": dropoff_longitude,
                   "dropoff_latitude": dropoff_latitude})

st.map(df)

"### Select the number of passengers"
passengers = st.slider("", 0, 10, 10)





params = {"pickup_datetime": f"{d} {t}",
          "pickup_longitude": pickup_longitude,
          "pickup_latitude": pickup_latitude,
          "dropoff_longitude": dropoff_longitude,
          "dropoff_latitude": dropoff_latitude,
          "passenger_count": passengers}



url = "https://taxifare.lewagon.ai/predict"

response = requests.get(url, params=params).json()
prediction = response.get("fare", "I couldn't find anything")


if st.button('fare'):
    # print is visible in the server output, not in the page
    st.write(prediction)
else:
    st.write('click me If you want to know the price')
