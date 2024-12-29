import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    file_path = '/home/shadowlast/Documents/projects/kifiya/kifiya_week2/Data/Week2_challenge_data_source.xlsx'
    data = pd.read_excel(file_path)
    return data

data = load_data()

# Title
st.title("Task 1: User Overview Analysis")

# Top 10 Handsets
st.subheader("Top 10 Handsets")
top_handsets = data['Handset Type'].value_counts().head(10)

# Plotting top handsets
fig, ax = plt.subplots()
top_handsets.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title("Top 10 Handsets")
ax.set_ylabel("Frequency")
ax.set_xlabel("Handset Type")
st.pyplot(fig)

# Top 3 Manufacturers
st.subheader("Top 3 Manufacturers")
top_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
st.write(top_manufacturers)

# Top 5 Handsets Per Manufacturer
for manufacturer in top_manufacturers.index:
    st.subheader(f"Top 5 Handsets for {manufacturer}")
    top_handsets_per_manufacturer = (
        data[data['Handset Manufacturer'] == manufacturer]['Handset Type']
        .value_counts()
        .head(5)
    )
    
    # Plot
    fig, ax = plt.subplots()
    top_handsets_per_manufacturer.plot(kind='bar', ax=ax, color='orange')
    ax.set_title(f"Top 5 Handsets for {manufacturer}")
    ax.set_ylabel("Frequency")
    ax.set_xlabel("Handset Type")
    st.pyplot(fig)

# Aggregate User Behavior
st.subheader("User Behavior Aggregation")
user_behavior = data.groupby('MSISDN/Number').agg({
    'Dur. (ms)': 'sum',            # Total session duration
    'Total DL (Bytes)': 'sum',     # Total download volume
    'Total UL (Bytes)': 'sum',     # Total upload volume
}).reset_index()

# Calculate Total Data Volume
user_behavior['Total Data Volume (Bytes)'] = user_behavior['Total DL (Bytes)'] + user_behavior['Total UL (Bytes)']
st.write(user_behavior.head())
