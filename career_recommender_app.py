import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Career Recommender", layout="centered")

# Page title
st.title("🤖 AI-Powered Tech Career Recommender 🤖")
st.write("Answer a few questions and get matched to your ideal tech career!")

# User Inputs
name = st.text_input("Your Name")
age_range = st.selectbox("Select Your Age Range", [
    "Under 18", "18–24", "25–34", "35–44", "45–54", "55–64", "65+"])
gender = st.selectbox("Gender", ["Male", "Female", "Prefer not to say"])
education = st.selectbox("Education Level", ["SSCE", "OND", "HND", "BSc", "MSc"])
interest = st.selectbox("Which area interests you most?", [
    "Data", "Design", "Communication", "Leadership", "AI", "Cybersecurity", "DevOps"])
strengths = st.multiselect("What are your top strengths?", [
    "Problem-solving", "Creativity", "Empathy", "Leadership", "Analytical Thinking"])
learning_style = st.radio("Preferred Learning Style", ["Visual", "Hands-on", "Self-paced"])
tech_level = st.selectbox("Tech Exposure Level", ["Beginner", "Intermediate", "Advanced"])

# Define career scores dictionary
careers = 
   {"Data Analyst": 0,
    "Decision Intelligence Specialist": 0,
    "Product Designer": 0,
    "UI/UX Designer": 0,
    "Technical Writer": 0,
    "Virtual Assistant": 0,
    "Project Manager": 0,
    "AI Engineer": 0,
    "AI Tool Specialist/Prompt Engineer": 0,
    "LLM Operator": 0,
    "Cybersecurity Specialist": 0,
    "Information Security Analyst": 0,
    "Threat Intelligence Analyst": 0,
    "DevOps Engineer": 0}

# Mapping interests to career paths
interest_map = {"Data": ["Data Analyst", "Decision Intelligence Specialist"],
    "Design": ["Product Designer", "UI/UX Designer"],
    "Communication": ["Technical Writer", "Virtual Assistant"],
    "Leadership": ["Project Manager"],
    "AI": ["AI Engineer", "AI Tool Specialist/Prompt Engineer", "LLM Operator"],
    "Cybersecurity": ["Cybersecurity Specialist", "Information Security Analyst", "Threat Intelligence Analyst"],
    "DevOps": ["DevOps Engineer"]}

for career in interest_map.get(interest, []):
    careers[career] += 2

# Score based on strengths
for s in strengths:
    if s == "Problem-solving":
        careers["Data Analyst"] += 1
        careers["Cybersecurity Specialist"] += 1
        careers["Threat Intelligence Analyst"] += 1
        careers["DevOps Engineer"] += 1
    elif s == "Creativity":
        careers["Product Designer"] += 2
        careers["Technical Writer"] += 1
        careers["UI/UX Designer"] += 2
        careers["AI Tool Specialist/Prompt Engineer"] += 1
    elif s == "Empathy":
        careers["Technical Writer"] += 2
        careers["UI/UX Designer"] += 1
        careers["Virtual Assistant"] += 1
    elif s == "Leadership":
        careers["Project Manager"] += 2
        careers["DevOps Engineer"] += 1
    elif s == "Analytical Thinking":
        careers["Data Analyst"] += 1
        careers["AI Engineer"] += 2
        careers["Cybersecurity Specialist"] += 1
        careers["Information Security Analyst"] += 1
        careers["Decision Intelligence Specialist"] += 1

# Score based on tech level
if tech_level == "Intermediate":
    careers["AI Engineer"] += 1
    careers["DevOps Engineer"] += 1
    careers["Cybersecurity Specialist"] += 1
    careers["UI/UX Designer"] += 1
    careers["AI Tool Specialist/Prompt Engineer"] += 1
    careers["LLM Operator"] += 1
    careers["Information Security Analyst"] += 1
elif tech_level == "Advanced":
    careers["AI Engineer"] += 2
    careers["DevOps Engineer"] += 2
    careers["Cybersecurity Specialist"] += 2
    careers["UI/UX Designer"] += 2
    careers["AI Tool Specialist/Prompt Engineer"] += 2
    careers["LLM Operator"] += 2
    careers["Information Security Analyst"] += 2

# Career explanations
explanations = {"Data Analyst": "You enjoy working with data to uncover insights and support decisions.",
    "Decision Intelligence Specialist": "You blend analytics, AI, and business to help organizations make smarter choices.",
    "Product Designer": "You thrive on creativity and enjoy turning ideas into functional products.",
    "UI/UX Designer": "You design user-friendly interfaces with beauty and function.",
    "Technical Writer": "You’re great at explaining complex ideas clearly and simply.",
    "Virtual Assistant": "You're organized, communicative, and thrive in helping roles using tech tools.",
    "Project Manager": "You lead teams and deliver results with planning, strategy, and execution.",
    "AI Engineer": "You enjoy solving problems using data, algorithms, and intelligent systems.",
    "AI Tool Specialist/Prompt Engineer": "You master the art of prompting and shaping outputs from AI tools.",
    "LLM Operator": "You operate large AI systems, managing data flow, performance, and integrity.",
    "Cybersecurity Specialist": "You’re detail-oriented and love protecting systems from threats.",
    "Information Security Analyst": "You specialize in protecting sensitive data from breaches and monitoring risk.",
    "Threat Intelligence Analyst": "You detect, research, and prevent security threats using data and foresight.",
    "DevOps Engineer": "You build automation, deployment systems, and ensure software runs reliably."}

# Recommendation logic
def recommend_career():
    return max(careers, key=careers.get)

# Prevent duplicate logging
log_file = "user_logs.csv"
existing_names = []

if os.path.exists(log_file):
    try:
        existing_logs = pd.read_csv(log_file)
        existing_names = existing_logs["Name"].str.lower().tolist()
    except pd.errors.ParserError:
        st.warning("⚠️ Log file unreadable. Please delete or fix `user_logs.csv`.")

# --- Main Interaction ---
if st.button("🔍 Recommend Career"):
    if not name:
        st.warning("Please enter your name.")
    elif name.lower() in existing_names:
        st.error("You've already submitted. Only one entry is allowed.")
    else:
        result = recommend_career()
        st.success(f"Hi **{name}**, based on your profile, you’d make a great **{result}**!")
        st.markdown(f"**Why?** {explanations[result]}")

        # Log data
        log_data = 
           {"Name": name,
            "Age": age_range,
            "Gender": gender,
            "Education": education,
            "Interest": interest,
            "Strengths": ", ".join(strengths),
            "Learning_Style": learning_style,
            "Tech_Level": tech_level,
            "Recommended_Career": result,
            "Timestamp": pd.Timestamp.now()}

        log_df = pd.DataFrame([log_data])
        if os.path.exists(log_file):
            log_df.to_csv(log_file, mode='a', header=False, index=False)
        else:
            log_df.to_csv(log_file, mode='w', header=True, index=False)

# --- Admin Section ---
st.markdown("---")
admin_key = st.text_input("Admin Access Key", type="password")
if admin_key == st.secrets["admin"]["key"]:
    st.success("Admin access granted.")
    if os.path.exists(log_file):
        df_logs = pd.read_csv(log_file)
        st.subheader("Recent Submissions")
        st.dataframe(df_logs.tail(10), use_container_width=True)

        csv = df_logs.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Full CSV Log",
            data=csv,
            file_name='user_logs.csv',
            mime='text/csv')
    else:
        st.info("No user data found yet.")
elif admin_key != "":
    st.error("Invalid admin key.")

# Footer
st.markdown("---")
st.caption("Built for 3MTT Knowledge Showcase | Abimbola O. Ige")
