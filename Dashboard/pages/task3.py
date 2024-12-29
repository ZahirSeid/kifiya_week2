import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
@st.cache
def load_data():
    file_path = '/home/shadowlast/Documents/projects/kifiya/kifiya_week2/Data/Week2_challenge_data_source.xlsx'
    data = pd.read_excel(file_path)
    return data

data = load_data()

# Title
st.title("Task 3: Experience Analytics")

# Aggregate Experience Metrics
st.subheader("Aggregated Experience Metrics per User")
experience_metrics = data.groupby('MSISDN/Number').agg({
    'TCP DL Retrans. Vol (Bytes)': 'mean',
    'TCP UL Retrans. Vol (Bytes)': 'mean',
    'Avg RTT DL (ms)': 'mean',
    'Avg RTT UL (ms)': 'mean',
    'Avg Bearer TP DL (kbps)': 'mean',
    'Avg Bearer TP UL (kbps)': 'mean',
}).reset_index()

# Handle missing values
experience_metrics.fillna(experience_metrics.mean(), inplace=True)

# Display metrics
st.write(experience_metrics.head())

# Top, Bottom, and Most Frequent Metrics
st.subheader("Top, Bottom, and Most Frequent Experience Metrics")
metrics = [
    'TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)', 
    'Avg RTT DL (ms)', 'Avg RTT UL (ms)', 
    'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)'
]

for metric in metrics:
    st.write(f"**{metric}**")
    st.write(f"Top 5: \n{experience_metrics[metric].nlargest(5).values}")
    st.write(f"Bottom 5: \n{experience_metrics[metric].nsmallest(5).values}")
    st.write(f"Most Frequent: \n{experience_metrics[metric].mode().values[0]}")

# Clustering Based on Experience Metrics
st.subheader("User Clustering Based on Experience")
clustering_data = experience_metrics.drop('MSISDN/Number', axis=1)

# Standardize data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)

# Perform k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
experience_metrics['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize cluster distribution
st.write("Cluster Distribution:")
st.bar_chart(experience_metrics['Cluster'].value_counts())

# Cluster Visualization
st.subheader("Cluster Visualization")
fig, ax = plt.subplots()
sns.scatterplot(
    x=experience_metrics['Avg Bearer TP DL (kbps)'], 
    y=experience_metrics['Avg Bearer TP UL (kbps)'], 
    hue=experience_metrics['Cluster'], 
    palette="viridis", ax=ax
)
ax.set_title("User Experience Clusters")
ax.set_xlabel("Avg Bearer TP DL (kbps)")
ax.set_ylabel("Avg Bearer TP UL (kbps)")
st.pyplot(fig)
