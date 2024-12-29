import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    file_path = '/home/shadowlast/Documents/projects/kifiya/kifiya_week2/Data/Week2_challenge_data_source.xlsx'
    data = pd.read_excel(file_path)
    return data

data = load_data()

# Title
st.title("Task 2: User Engagement Analysis")

# Aggregate Engagement Metrics
st.subheader("Aggregated Engagement Metrics per User")
engagement_metrics = data.groupby('MSISDN/Number').agg({
    'Dur. (ms)': 'sum',           # Total session duration
    'Total DL (Bytes)': 'sum',    # Total download volume
    'Total UL (Bytes)': 'sum',    # Total upload volume
}).reset_index()

# Add Total Traffic
engagement_metrics['Total Data (Bytes)'] = engagement_metrics['Total DL (Bytes)'] + engagement_metrics['Total UL (Bytes)']

# Display aggregated metrics
st.write(engagement_metrics.head())

# Top 10 Users per Engagement Metric
st.subheader("Top 10 Users by Engagement Metric")
for metric in ['Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)', 'Total Data (Bytes)']:
    st.write(f"Top 10 Users by {metric}")
    top_users = engagement_metrics[['MSISDN/Number', metric]].sort_values(by=metric, ascending=False).head(10)
    st.write(top_users)

# Normalize Engagement Metrics for Clustering
st.subheader("User Clustering Based on Engagement")
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# Normalize the metrics
scaler = MinMaxScaler()
scaled_metrics = scaler.fit_transform(engagement_metrics[['Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']])

# Perform k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
engagement_metrics['Cluster'] = kmeans.fit_predict(scaled_metrics)

# Display cluster counts
st.write("Cluster Distribution:")
st.bar_chart(engagement_metrics['Cluster'].value_counts())

# Visualize Clusters
st.subheader("Cluster Visualization")
fig, ax = plt.subplots()
sns.scatterplot(
    x=engagement_metrics['Dur. (ms)'], 
    y=engagement_metrics['Total Data (Bytes)'], 
    hue=engagement_metrics['Cluster'], 
    palette="viridis", ax=ax
)
ax.set_title("User Engagement Clusters")
ax.set_xlabel("Session Duration (ms)")
ax.set_ylabel("Total Data (Bytes)")
st.pyplot(fig)
