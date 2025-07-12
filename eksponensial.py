# app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Kalkulator Eksponensial dengan Grafik")
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

# Buat grafik eksponensial
st.subheader("Grafik Fungsi Eksponensial")
x_values = np.linspace(-5, 5, 200)
y_values = np.exp(x_values)

fig, ax = plt.subplots()
ax.plot(x_values, y_values, label="e^x", color="blue")
ax.scatter(x, result, color="red", label=f"e^{x} = {result:.2f}")
ax.set_xlabel("x")
ax.set_ylabel("e^x")
ax.set_title("Kurva Eksponensial")
ax.legend()
ax.grid(True)

st.pyplot(fig)
