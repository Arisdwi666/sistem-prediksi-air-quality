import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
)
st.write("# Tentang Saya")

st.sidebar.success("Hai Salam Kenal.")

st.markdown(
    """
    Perkenalkan, nama saya Aris Dwi Wahyudi, mahasiswa dari Universitas Dian Nuswantoro, sedang aktif mengejar skripsi dalam pengembangan Sistem Prediksi Kualitas Udara. Dalam rangka mencapai tujuan ini, saya menggunakan data terkini dari Firebase untuk parameter PM2.5, CO, dan O3. Sistem ini dirancang agar pengguna dapat dengan mudah memberikan input nilai PM10, SO2, dan NO2 guna mendapatkan prediksi kualitas udara yang lebih lengkap. Proyek ini merupakan upaya saya untuk menyediakan alat yang sederhana namun efektif dalam pemantauan lingkungan.
    
    ### Want to see more?
    - Check out [Github](https://github.com/Arisdwi666)
    - My Profile [LinkedIn](https://www.linkedin.com/in/aris-dwi-wahyudi)
    - Ask a question in my [Instagram](https://www.instagram.com/_arisdwi666/)
    ### Terimakasih atas kunjungannya
    
"""
)