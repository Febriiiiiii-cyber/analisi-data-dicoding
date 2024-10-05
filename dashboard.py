# app.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set judul aplikasi
st.title("Analisis Penggunaan Sepeda")

# Mengumpulkan data
day_df = pd.read_csv("day.csv")  # Pastikan path ini benar
hour_df = pd.read_csv("hour.csv")  # Pastikan path ini benar

# Menampilkan data
if st.checkbox("Tampilkan Data Hour"):
    st.subheader("Data Hour")
    st.write(hour_df.head())

if st.checkbox("Tampilkan Data Day"):
    st.subheader("Data Day")
    st.write(day_df.head())

# Mengubah tipe data
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Pertanyaan 1: Rata-rata pengguna sepeda berdasarkan kategori waktu
avg_holiday = hour_df[hour_df['holiday'] == 1]['registered'].mean()
avg_weekday = hour_df[hour_df['weekday'] == 1]['registered'].mean()
avg_workingday = hour_df[hour_df['workingday'] == 1]['registered'].mean()

categories = ['holiday', 'weekday', 'workingday']
avg_counts = [avg_holiday, avg_weekday, avg_workingday]

# Plot untuk pertanyaan 1
st.subheader('Rata-Rata Pengguna Sepeda Berdasarkan Kategori Waktu')
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_counts, color=['blue', 'green', 'orange'])
plt.xlabel('Kategori Waktu')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
plt.title('Rata-Rata Pengguna Sepeda Dalam Waktu Holiday, Weekday, Workingday')
plt.grid(axis='y')
st.pyplot(plt)

# Pertanyaan 2: Penggunaan sepeda selama beberapa bulan
day_df['month'] = day_df['dteday'].dt.month
month = day_df.groupby('month')[['casual', 'registered']].mean()

# Plot untuk pertanyaan 2
st.subheader('Penggunaan Sepeda Selama Beberapa Bulan')
plt.figure(figsize=(12, 6))
month.plot(kind='line', marker='o')
plt.title('Penggunaan Sepeda Selama Beberapa Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.xticks(range(1, 13))
plt.legend(['Casual', 'Registered'])
plt.grid(True)
st.pyplot(plt)

# Pertanyaan 3: Rata-rata pengguna sepeda casual dan registered
avg_casual = avg_counts[0]  # Ambil dari pertanyaan 1
avg_registered = avg_counts[1]  # Ambil dari pertanyaan 1
categories = ['Casual', 'Registered']
avg_counts = [avg_casual, avg_registered]

# Plot untuk pertanyaan 3
st.subheader('Rata-rata Jumlah Pengguna Sepeda Acak dan Terdaftar')
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_counts, color=['blue', 'green'])
plt.xlabel('Kategori Pengguna Sepeda')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
plt.title('Rata-rata Jumlah Pengguna Sepeda Acak dan Terdaftar')
plt.grid(axis='y')
st.pyplot(plt)
