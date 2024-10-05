#!/usr/bin/env python
# coding: utf-8

# ## Import Semua Packages/Library yang Digunakan

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# ## Function to load data

@st.cache
def load_data():
    try:
        bike_df = pd.read_csv("day.csv")
        return bike_df
    except FileNotFoundError:
        st.error("File 'day.csv' not found. Please ensure it's in the correct directory.")
        return None

# ## Function to clean data
def clean_data(bike_df):
    if bike_df is not None:
        # Mengubah tipe data object pada dteday menjadi datetime
        bike_df['dteday'] = pd.to_datetime(bike_df['dteday'])
    return bike_df

# ## Function for EDA
def analyze_data(bike_df):
    avg_casual = bike_df['casual'].mean()
    avg_registered = bike_df['registered'].mean()
    
    # Group by year and month for visualization
    monthly_usage = bike_df.groupby(['yr', 'mnth'])['cnt'].mean().unstack()
    
    return avg_casual, avg_registered, monthly_usage

# ## Function for visualizations
def plot_user_comparison(avg_casual, avg_registered):
    categories = ['Casual', 'Registered']
    avg_counts = [avg_casual, avg_registered]
    
    plt.figure(figsize=(8, 5))
    plt.bar(categories, avg_counts, color=['blue', 'green'])
    plt.xlabel('Kategori Pengguna Sepeda')
    plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
    plt.title('Rata-rata Jumlah Pengguna Sepeda Acak dan Terdaftar')
    plt.grid(axis='y')
    st.pyplot(plt)

def plot_monthly_usage(monthly_usage):
    plt.figure(figsize=(12, 6))
    monthly_usage.T.plot(kind='line', marker='o')
    plt.title('Penggunaan Sepeda Selama Tahun')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.xticks(range(1, 13))
    plt.legend(['Tahun 0', 'Tahun 1'])
    plt.grid(True)
    st.pyplot(plt)

# ## Main function to run the app
def main():
    st.title("Analisis Data Bike Sharing")

    bike_df = load_data()
    if bike_df is None:
        return  # Exit if data loading fails

    bike_df = clean_data(bike_df)

    avg_casual, avg_registered, monthly_usage = analyze_data(bike_df)

    # Display average users
    st.subheader("Rata-rata Pengguna Sepeda")
    st.write(f"Rata-rata pengguna sepeda acak: {avg_casual:.2f}")
    st.write(f"Rata-rata pengguna sepeda terdaftar: {avg_registered:.2f}")

    # Visualizations
    st.subheader("Perbandingan Rata-rata Pengguna")
    plot_user_comparison(avg_casual, avg_registered)

    st.subheader("Pola Penggunaan Sepeda Selama Tahun")
    plot_monthly_usage(monthly_usage)

# Run the app
if __name__ == "__main__":  # Corrected the typo here
    main()
