import streamlit as st
import pandas as pd
import os
import datetime

st.set_page_config(page_title="AI Career Recommender", layout="centered")

# Page title
st.title("🎯 AI-Powered Tech Career Recommender")
st.write("Answer a few questions and get matched to your ideal tech career!")

name = st.text_input("Your Name")
age = st.number_input("Your Age", min_value=10, max_value=100, value=25, format="%d")
gender = st.selectbox("Gender", ["Male", "Female"])

education = st.selectbox("Education Level", ["SSCE", "OND", "HND", "BSc", "MSc"])
interest = st.selectbox("Which area interests you most?", ["Data", "Design", "Communication", "Leadership", "AI", "Cybersecurity", "DevOps"])
strengths = st.multiselect("What are your top strengths?", ["Problem-solving", "Creativity", "Empathy", "Leadership", "Analytical Thinking"])
learning_style = st.radio("Preferred Learning Style", ["Visual", "Hands-on", "Self-paced"])
tech_level = st.selectbox("Tech Exposure Level", ["Beginner", "Intermediate", "Advanced"])

# Initialize career scores
careers = {
    "Data Analyst": 0,
    "Product Designer": 0,
    "Technical Writer": 0,
    "Project Manager": 0,
    "AI Engineer": 0,
    "Cybersecurity Specialist": 0,
    "DevOps Engineer": 0
}

# Add scores based on interest
interest_map = {
    "Data": ["Data Analyst"],
    "Design": ["Product Designer"],
    "Communication": ["Technical Writer"],
    "Leadership": ["Project Manager"],
    "AI": ["AI Engineer"],
    "Cybersecurity": ["Cybersecurity Specialist"],
    "DevOps": ["DevOps Engineer"]
}

for career in interest_map.get(interest, []):
    careers[career] += 2  # base score for interest

# Add scores based on strengths
for s in strengths:
    if s == "Problem-solving":
        careers["Data Analyst"] += 1
        careers["Cybersecurity Specialist"] += 1
        careers["DevOps Engineer"] += 1
    elif s == "Creativity":
        careers["Product Designer"] += 2
        careers["Technical Writer"] += 1
    elif s == "Empathy":
        careers["Technical Writer"] += 2
    elif s == "Leadership":
        careers["Project Manager"] += 2
        careers["DevOps Engineer"] += 1
    elif s == "Analytical Thinking":
        careers["Data Analyst"] += 1
        careers["AI Engineer"] += 2
        careers["Cybersecurity Specialist"] += 1

# Add scores based on tech level
if tech_level == "Intermediate":
    careers["AI Engineer"] += 1
    careers["DevOps Engineer"] += 1
    careers["Cybersecurity Specialist"] += 1
elif tech_level == "Advanced":
    careers["AI Engineer"] += 2
    careers["DevOps Engineer"] += 2
    careers["Cybersecurity Specialist"] += 2

# Career descriptions
explanations = {
    "Data Analyst": "You love working with data to find insights that drive decisions.",
    "Product Designer": "You thrive on creativity, design thinking, and crafting great user experiences.",
    "Technical Writer": "You're great at making complex topics easy to understand.",
    "Project Manager": "You have leadership skills and enjoy organizing teams to hit goals.",
    "AI Engineer": "You're analytical and excited about machine learning and automation.",
    "Cybersecurity Specialist": "You enjoy securing systems and thinking like a hacker to prevent breaches.",
    "DevOps Engineer": "You love automation, infrastructure, and keeping systems running smoothly."
}

log_file = "user_logs.csv"
existing_names = []

if os.path.exists(log_file):
    try:
        existing_logs = pd.read_csv(log_file)
        existing_names = existing_logs["Name"].str.lower().tolist()
    except pd.errors.ParserError:
        st.warning("⚠️ The log file is corrupted or unreadable. Please fix or delete `user_logs.csv`.")

if st.button("🔍 Recommend Career"):
    if name:
        result = recommend_career(interest, strengths, tech_level)
        st.success(f"Hi **{name}**, based on your profile, you’d make a great **{result}**!")

        # Logging the result
        log_file = "user_logs.csv"
        log_data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Education": education,
            "Interest": interest,
            "Strengths": ", ".join(strengths),
            "Learning_Style": learning_style,
            "Tech_Level": tech_level,
            "Recommended_Career": result,
            "Timestamp": pd.Timestamp.now()
        }

        log_df = pd.DataFrame([log_data])

        if os.path.exists(log_file):
            log_df.to_csv(log_file, mode='a', header=False, index=False)
        else:
            log_df.to_csv(log_file, mode='w', header=True, index=False)

    else:
        st.warning("Please enter your name to proceed.")

# --- Admin Section 
st.markdown("---")
admin_key = st.text_input("🔐 Admin Access Key", type="password")

if admin_key == st.secrets["admin"]["key"]:
    st.success("✅ Admin access granted.")
    
    if os.path.exists("user_logs.csv"):
        df_logs = pd.read_csv("user_logs.csv")
        st.subheader("📋 Recent Submissions")
        st.dataframe(df_logs.tail(10), use_container_width=True)

        csv = df_logs.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Full CSV Log",
            data=csv,
            file_name='user_logs.csv',
            mime='text/csv'
        )
    else:
        st.info("No user data logged yet.")
elif admin_key != "":
    st.error("❌ Invalid admin key.")

# Footer
st.markdown("---")
st.caption("Built for 3MTT Knowledge Showcase | Powered by Data + AI 🔬")
