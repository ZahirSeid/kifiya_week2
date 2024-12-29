import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data
@st.cache_data
def load_data():
    file_path = "/home/shadowlast/Documents/projects/kifiya/kifiya_week2/Data/Week2_challenge_data_source.xlsx"  
    data = pd.read_excel(file_path)
    return data

data = load_data()

# Title
st.title("Task 4: Satisfaction Analysis")

# Aggregate Engagement and Experience Scores
st.subheader("Aggregating Engagement and Experience Metrics")
experience_metrics = data.groupby('MSISDN/Number').agg({
    'TCP DL Retrans. Vol (Bytes)': 'mean',
    'TCP UL Retrans. Vol (Bytes)': 'mean',
    'Avg RTT DL (ms)': 'mean',
    'Avg RTT UL (ms)': 'mean',
    'Avg Bearer TP DL (kbps)': 'mean',
    'Avg Bearer TP UL (kbps)': 'mean',
}).reset_index()

experience_metrics.fillna(experience_metrics.mean(), inplace=True)

# Engagement and experience centroids (dummy values for demonstration; replace with actual centroids)
less_engaged_centroid = [50, 100, 200, 150, 300, 250]
worst_experience_centroid = [30, 80, 150, 120, 250, 200]

# Calculate scores
st.subheader("Calculating Engagement and Experience Scores")
engagement_scores = euclidean_distances(experience_metrics.drop('MSISDN/Number', axis=1), [less_engaged_centroid]).flatten()
experience_scores = euclidean_distances(experience_metrics.drop('MSISDN/Number', axis=1), [worst_experience_centroid]).flatten()

# Add scores to DataFrame
experience_metrics['Engagement_Score'] = engagement_scores
experience_metrics['Experience_Score'] = experience_scores
experience_metrics['Satisfaction_Score'] = (experience_metrics['Engagement_Score'] + experience_metrics['Experience_Score']) / 2

st.write(experience_metrics.head())

# Top 10 Satisfied Users
st.subheader("Top 10 Satisfied Users")
top_10_satisfied = experience_metrics.nlargest(10, 'Satisfaction_Score')
st.write(top_10_satisfied[['MSISDN/Number', 'Satisfaction_Score']])

# Clustering on Satisfaction
st.subheader("Clustering Based on Satisfaction Scores")
kmeans = KMeans(n_clusters=2, random_state=42)
experience_metrics['Cluster'] = kmeans.fit_predict(experience_metrics[['Engagement_Score', 'Experience_Score']])

# Cluster Visualization
fig, ax = plt.subplots()
sns.scatterplot(
    x=experience_metrics['Engagement_Score'],
    y=experience_metrics['Experience_Score'],
    hue=experience_metrics['Cluster'],
    palette="viridis", ax=ax
)
ax.set_title("Satisfaction Clusters")
ax.set_xlabel("Engagement Score")
ax.set_ylabel("Experience Score")
st.pyplot(fig)

# Regression Model
st.subheader("Regression Model for Satisfaction Score")
X = experience_metrics[['Engagement_Score', 'Experience_Score']]
y = experience_metrics['Satisfaction_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.write(f"Mean Squared Error: {mse}")
st.write(f"R-Squared: {r2}")
