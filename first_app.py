import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# Custom CSS for Dark Theme
st.markdown(
    """
    <style>
    .stApp {
        max-width: 1200px;
        margin: auto;
        padding: 20px;
        background-color: #1E1E1E;
        color: white;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stFileUploader div {
        border: 2px dashed #4CAF50;
        border-radius: 5px;
        padding: 20px;
        text-align: center;
    }
    .stSlider div {
        color: #4CAF50;
    }
    .stTextArea textarea {
        background-color: #2E2E2E;
        color: white;
    }
    .stTextInput input {
        background-color: #2E2E2E;
        color: white;
    }
    .stSelectbox select {
        background-color: #2E2E2E;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to Load Data from Excel
def load_data(file):
    try:
        df = pd.read_excel(file, engine='openpyxl')
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None

# Function to Save Progress Report
def save_progress_report(data, filename="progress_report.csv"):
    if not os.path.exists(filename):
        data.to_csv(filename, index=False)
    else:
        existing_data = pd.read_csv(filename)
        updated_data = pd.concat([existing_data, data], ignore_index=True)
        updated_data.to_csv(filename, index=False)

# Main App
def main():
    st.title("Growth Mindset Progress Tracker 🌱")

    # Upload Excel File for Progress Tracking
    st.header("Upload Your Excel File")
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            st.success("File uploaded successfully!")
            st.write("Preview of your data:")
            st.dataframe(df)

            # Automatic Column Detection
            st.header("Graph Plotting")
            columns = df.columns.tolist()
            x_axis = st.selectbox("Select X-axis column:", columns)
            y_axis = st.selectbox("Select Y-axis column:", columns)

            if st.button("Plot Graph"):
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
                st.plotly_chart(fig)

    # Feature 1: Monthly and Weekly Goals
    st.header("Set Your Goals")
    weekly_goal = st.text_input("Weekly Goal (e.g., Complete 5 chapters)")
    monthly_goal = st.text_input("Monthly Goal (e.g., Finish a book)")

    # Feature 2: Daily Journaling
    st.header("Daily Journaling")
    journal_entry = st.text_area("Write your reflections for today:")

    # Feature 3: Habit Tracker
    st.header("Habit Tracker")
    habits = ["Exercise", "Read", "Meditate", "Learn Something New"]
    selected_habits = st.multiselect("Select habits to track:", habits)

    # Feature 4: Mood Tracker
    st.header("Mood Tracker")
    mood = st.slider("How are you feeling today? (1 = Sad, 10 = Happy)", 1, 10)

    # Feature 5: Achievements Section
    st.header("Achievements")
    achievement = st.text_input("Add your achievement for today:")

    # Feature 6: Reminders
    st.header("Reminders")
    reminder = st.text_input("Set a reminder for tomorrow:")

    # Feature 7: Submit Button
    if st.button("Submit Progress"):
        # Create a progress report
        progress_report = pd.DataFrame({
            "Date": [datetime.now().strftime("%Y-%m-%d")],
            "Weekly Goal": [weekly_goal],
            "Monthly Goal": [monthly_goal],
            "Journal Entry": [journal_entry],
            "Habits Tracked": [", ".join(selected_habits)],
            "Mood": [mood],
            "Achievement": [achievement],
            "Reminder": [reminder]
        })

        # Save progress report to CSV
        save_progress_report(progress_report, "progress_report.csv")
        st.success("Progress report saved successfully!")

    # Feature 8: View History
    st.header("Progress History")
    if os.path.exists("progress_report.csv"):
        history_df = pd.read_csv("progress_report.csv")
        st.write(history_df)
    else:
        st.write("No history available yet.")

# Run the App
if __name__ == "__main__":
    main()