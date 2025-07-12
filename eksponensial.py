# app.py

import streamlit as st
import numpy as np

st.title("Kalkulator Eksponensial")
st.write("""
Aplikasi ini menghitung nilai eksponensial dari suatu bilangan.
Rumus:  
$$ e^x $$
""")

# Input angka
x = st.number_input("Masukkan nilai x", value=0.0)

# Hitung eksponensial
result = np.exp(x)

# Tampilkan hasil
st.write(f"Nilai eksponensial (e^{x}) = **{result}**")
