import streamlit as st
from utils import logo

st.set_page_config(
    page_title="Home",
    page_icon="🏚️",
)

st.write("# Prediksi Kuallitas Udara")


st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Selamat datang di Sistem Prediksi Kualitas Udara kami! Kami menyediakan informasi terkini tentang kualitas udara dengan data yang diambil dari Firebase, termasuk parameter PM2.5, CO, dan O3. Dengan menggunakan sistem ini, Anda dapat dengan mudah memasukkan nilai PM10, SO2, dan NO2 untuk mendapatkan prediksi kualitas udara yang akurat. Dengan antarmuka yang sederhana dan jelas, kami hadir untuk membantu Anda memantau dan memahami kualitas udara di sekitar Anda. Jelajahi prediksi kami dan tingkatkan kesadaran lingkungan Anda.
    
    **👈 Select a demo from the sidebar** 
    """
)
st.image("../image/logo.jpg", caption='Prediksi Kualitas Udara')
