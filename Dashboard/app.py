import streamlit as st

# Title
st.set_page_config(page_title="Telecom Insights Dashboard", layout="wide")
st.title("Telecom Insights Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Task 1: User Overview", 
                                   "Task 2: Engagement Analysis", 
                                   "Task 3: Experience Analysis", 
                                   "Task 4: Satisfaction Analysis"])

if page == "Task 1: User Overview":
    import pages.task1
elif page == "Task 2: Engagement Analysis":
    import pages.task2
elif page == "Task 3: Experience Analysis":
    import pages.task3
elif page == "Task 4: Satisfaction Analysis":
    import pages.task4
