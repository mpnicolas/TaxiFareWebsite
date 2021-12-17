import streamlit as st

st.markdown('''# TaxiFare Web Site''')

## select the parameters of the ride

import datetime
import pandas as pd

d = st.date_input("Quand partez-vous ?", datetime.date(2021, 12, 17))
t = st.time_input('A quelle heure ?', datetime.time(8, 0))
#adate = pd.to_datetime(str(d) + " " + str(t), utc=True)

lon1 = st.text_input('pickup longitude', '')
lat1 = st.text_input('pickup latitude', '')
lon2 = st.text_input('dropoff longitude', '')
lat2 = st.text_input('dropoff latitude', '')
#lon1 = float(lon1)
#lat1 = float(lat1)
#lon2 = float(lon2)
#lat2 = float(lat2)
nb_pass = st.text_input('passenger count', '1')
#nb_pass = int(nb_pass)

import requests
url = 'https://taxifare.lewagon.ai/predict'
#if url == 'https://taxifare.lewagon.ai/predict'

#2. Let's build a dictionary containing the parameters for our API...
if st.button('Calcul tarif:'):

    params = dict(pickup_datetime=str(d) + " " + str(t),
              pickup_longitude=lon1,
              pickup_latitude=lat1,
              dropoff_longitude=lon2,
              dropoff_latitude=lat2,
              passenger_count=nb_pass)
    #3. Let's call our API using the `requests` package...

    response = requests.get(url, params=params)

#4. Let's retrieve the prediction from the **JSON** returned by the API...
    if response.status_code != 200:
        st.write("Erreur : " + str(response.status_code))
    else :
        ## Finally, we can display the prediction to the user
        rep = response.json().get("prediction", "no prediction")
        rep = round(rep,2)
        st.write("Montant minimum à prévoir : "+str(rep))
