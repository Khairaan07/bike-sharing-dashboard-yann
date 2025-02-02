import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hour.csv")

df['season'] = df['season'].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
df['weather'] = df['weathersit'].map({1: "Clear", 2: "Cloudy", 3: "Light Rain", 4: "Heavy Rain"})

st.title("Bike Sharing Data Dashboard")

selected_season = st.selectbox("Pilih Musim", df['season'].unique())

st.subheader(f"Distribusi Jumlah Penyewaan Sepeda pada {selected_season}")
filtered_df = df[df['season'] == selected_season]

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=filtered_df['season'], y=filtered_df['cnt'], ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

st.subheader("Distribusi Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=df['weather'], y=df['cnt'], ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
