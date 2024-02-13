import pickle
import time
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import joblib
import pandas as pd
import requests as req
import firebase_admin
from firebase_admin import credentials, db


st.set_page_config(
    page_title="App",
    page_icon="📝",
)

filename = '../models/SVM_Model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
# Inisialisasi Firebase
cred = credentials.Certificate("../js/esp32-try-5fddb-firebase-adminsdk-bj5sn-931fb2b72d.json")
# Check if the app is not already initialized
if not firebase_admin._apps:
    # Initialize the Firebase app
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://esp32-try-5fddb-default-rtdb.firebaseio.com'})
else:
    # If the app is already initialized, get the default app
    default_app = firebase_admin.get_app()
# Mendapatkan referensi ke Realtime Database
ref_co = db.reference('/sensor_data/CO')
ref_o3 = db.reference('/sensor_data/O3')
ref_pm25 = db.reference('/sensor_data/PM25')
# Mengambil data dari Firebase
data_co = ref_co.get()
data_o3 = ref_o3.get()
data_pm25 = ref_pm25.get()


st.sidebar.header("Predict Air Quality")
st.title('Prediksi Kualitas Udara')
st.write('Masukkan nilai parameter untuk diprediksi')
st.write("")



pm_10 = st.number_input("Masukkan nilai PM10")
st.write(f":orange[Min] value: :orange[**{0}**], :red[Max] value: :red[**{1000}**]")

pm_25 = st.number_input("Masukkan nilai PM2.5", value=float(data_pm25))
st.write(f":orange[Min] value: :orange[**{0}**], :red[Max] value: :red[**{1000}**]")

so2 = st.number_input("Masukkan nilai SO2")
st.write(f":orange[Min] value: :orange[**{0}**], :red[Max] value: :red[**{1000}**]")

co = st.number_input("Masukkan nilai CO", value=float(data_co))
st.write(f":orange[Min] value: :orange[**{0}**], :red[Max] value: :red[**{1000}**]")

o3 = st.number_input("Masukkan nilai O3", value=float(data_o3))
st.write(f":orange[Min] value: :orange[**{0}**], :red[Max] value: :red[**{1000}**]")

no2 = st.number_input("Masukkan nilai NO2")
st.write(f":orange[Min] value: :orange[**{0}**], :red[Max] value: :red[**{1000}**]")



predict_btn = st.button("Predict", type=("primary"))
result = ":violet[-]"
st.write("")

load_scaler = joblib.load('../models/MinMaxScaler.pkl')


inputs = [[pm_10, pm_25, so2, co, o3, no2]]

if predict_btn:
    data = pd.DataFrame(inputs, columns=['pm10', 'pm25', 'so2', 'co', 'o3', 'no2'])
    st.write("Data yang diinputkan:")
    st.write(data)
    print(data)
    
    
    # Normalisasi semua kolom
    data_normalized = load_scaler.transform(data)
    print(data_normalized)
    
    # Prediksi
    predicted_class = loaded_model.predict(data_normalized)

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 101):
        status_text.text(f"{i}% complete")
        bar.progress(i)
        time.sleep(0.01)
        if i == 100:
            time.sleep(1)
            status_text.empty()
            bar.empty()
            
            
    if predicted_class == 0:
        result = "BAIK"
    elif predicted_class == 1:
        result = "SEDANG"
    else:
        result = "TIDAK SEHAT"    
       
    st.write("")
    st.write("")
    st.subheader("Prediction:")
    st.subheader(result)
# %%
