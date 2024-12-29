import streamlit as st

# Set page configuration
st.set_page_config(page_title="Telecom Insights Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Task:",
    [
        "Task 1: User Overview Analysis",
        "Task 2: Engagement Analysis",
        "Task 3: Experience Analytics",
        "Task 4: Satisfaction Analysis",
    ],
)

# Load appropriate page based on selection
if page == "Task 1: User Overview Analysis":
    import pages.task1
elif page == "Task 2: Engagement Analysis":
    import pages.task2
elif page == "Task 3: Experience Analytics":
    import pages.task3
elif page == "Task 4: Satisfaction Analysis":
    import pages.task4
