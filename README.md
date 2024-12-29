# kifiya_week2

## Project Description
### Tak 1 and 2
This project focuses on analyzing user traffic and behavior patterns from network data. The goal is to extract actionable insights that can help improve user experience, optimize service delivery, and inform business decisions. The analysis is based on a dataset that contains user session details, including traffic volume, session duration, and the applications used during the sessions.
Project Goals:

    Identify Key Traffic Trends: Understand how users engage with different applications and the overall traffic patterns across multiple sessions.
    Segmentation of User Behavior: Use clustering techniques to categorize users based on their traffic behavior and session characteristics.
    Application Contribution Analysis: Analyze how various applications contribute to the total network traffic and user engagement.

# Approach:

    Data Preprocessing:
        Clean and preprocess the dataset to handle missing values, outliers, and ensure that data is in a usable format.
        Create new columns to categorize traffic based on application types (e.g., Social Media, Google, Email, YouTube).

    Univariate and Bivariate Analysis:
        Conduct univariate analysis to explore individual variables like session duration, total upload/download traffic, and their distributions.
        Perform bivariate analysis to investigate relationships between different variables, such as how session duration correlates with data usage.

    Clustering:
        Apply clustering techniques like K-Means to segment users into groups based on their traffic patterns.
        Use methods like the Elbow Method to determine the optimal number of clusters and analyze the distribution of users within these clusters.

    Application Analysis:
        Categorize the traffic into different application types and analyze their contributions to total traffic.
        Assess how different user groups (based on clustering) engage with specific applications and their respective traffic usage.

# Key Insights:

    Top Applications: Social Media, Google, and YouTube emerge as the most heavily used applications, accounting for the largest portion of the network traffic.
    User Segmentation: Through clustering, users are categorized into distinct groups with differing usage patterns, which could be useful for personalized services or targeted marketing.
    Traffic Distribution: A large variance exists in how different applications contribute to total traffic, providing opportunities to optimize network resources or offer differentiated services.

# Future Directions:

    Further analysis of temporal patterns, such as peak usage times or day-of-week traffic variations, to identify additional optimization opportunities.
    Study the impact of specific user demographics or behaviors on their traffic patterns for more targeted service offerings.

This project combines exploratory data analysis, clustering techniques, and application-specific insights to provide a deeper understanding of user behavior in network traffic, offering valuable information for both technical optimization and business decision-making.

# Task 3: Network Performance Analysis
## Overview

Task 3 involved analyzing various network performance metrics extracted from a dataset. The goal was to understand throughput, retransmission volumes, and round-trip time (RTT) across different dimensions, such as handset types. The analysis focused on identifying patterns, top and bottom-performing values, and frequently occurring metrics.
### Key Metrics Analyzed

    TCP Downlink Retransmission Volume (Bytes):
        Examined the top 5 and bottom 5 values.
        Determined the most frequent retransmission volume observed.

    TCP Uplink Retransmission Volume (Bytes):
        Identified devices with the highest and lowest retransmission volumes.
        Analyzed the most frequent uplink retransmission volume.

    Average Round-Trip Time (RTT) Downlink (ms):
        Focused on devices with the highest and lowest average RTT.
        Extracted the most common downlink RTT.

    Average Round-Trip Time (RTT) Uplink (ms):
        Reviewed the extremes in RTT uplink performance.
        Noted the most frequently occurring RTT for uplink.

    Average Bearer Throughput Downlink (kbps):
        Visualized throughput distribution across handset types.
        Highlighted the best and worst-performing values.

    Average Bearer Throughput Uplink (kbps):
        Investigated the distribution and outliers.
        Determined the most frequent throughput values.

### Insights Gained

    Visualization: A scatter plot was generated to visualize throughput distribution by handset type. The plot highlighted variations across devices but also revealed crowding in labels due to the large number of handset types.
    Performance Extremes:
        The analysis revealed extreme values for retransmissions, RTT, and throughput that indicate potential performance bottlenecks or anomalies.
        Most frequent values provided insight into typical network performance.

### Key Outcomes

    The task successfully computed and analyzed key network performance metrics.
    Data visualizations and top/bottom performers were identified for each metric.
    Results from this task will serve as valuable references when compiling the final report.

### Notes

This task demonstrated the ability to extract meaningful insights from raw network performance data. The outputs will help in understanding network reliability, identifying optimization opportunities, and benchmarking device performance.

# Task 4: Satisfaction Analysis
## Overview

This task focused on analyzing customer satisfaction by combining insights from user engagement (Task 2) and user experience (Task 3). The goal was to calculate scores for engagement, experience, and overall satisfaction, followed by clustering and predictive modeling.
Steps Completed
### 4.1 Engagement and Experience Scores

    Engagement Score:
        Calculated as the Euclidean distance between each user's engagement metrics and the less engaged cluster centroid.
    Experience Score:
        Calculated as the Euclidean distance between each user's experience metrics and the worst experience cluster centroid.

### 4.2 Satisfaction Score

    Computed as the average of the engagement and experience scores.
    Identified the top 10 satisfied users based on satisfaction scores.

### 4.3 Regression Model

    Built a regression model to predict satisfaction scores.
        Features: Engagement and experience scores.
        Target: Satisfaction score.
    Evaluated the model with Mean Squared Error (MSE) and R-squared metrics.

### 4.4 Clustering

    Applied k-means clustering (k=2) on the engagement and experience scores to group users into satisfaction-based clusters.

### 4.5 Cluster Analysis

    Aggregated the average satisfaction and experience scores for each cluster.

### 4.6 Export to PostgreSQL

    Exported the final results to a PostgreSQL database, including:
        User ID
        Engagement Score
        Experience Score
        Satisfaction Score

## Key Outputs

    Top 10 Satisfied Users:
        Users with the highest satisfaction scores, representing the most engaged and best-experienced customers.
    Satisfaction Clusters:
        Segmented users into two clusters for better targeting and optimization.
    Database Export:
        Results saved in a PostgreSQL table (user_satisfaction) for further use.

## Files

    notebooks/eda-task4.ipynb: Jupyter Notebook containing all Python code for Task 4.
    PostgreSQL Database:
        Exported data table: user_satisfaction.