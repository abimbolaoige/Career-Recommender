import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Career Recommender", layout="centered")

# --- Title ---
st.title("🤖 AI-Powered Tech Career Recommender 💼")
st.write("#### Answer a few questions and get matched to your ideal tech career!")

st.markdown("### ⚠️ Important!")
st.markdown("Please *do not leave any field blank*. All questions are required to give you the most accurate career match.")
st.markdown("---")

# --- User Inputs ---
name = st.text_input("Your Name")
age_range = st.selectbox("Select Your Age Range", ["Under 18", "18–24", "25–34", "35–44", "45–54", "55–64", "65+"])
gender = st.selectbox("Gender", ["Male", "Female", "Prefer not to say"])
education = st.selectbox("Education Level", ["High School", "SSCE", "OND", "HND", "BSc", "MSc"])
interest = st.selectbox("Which area interests you most?", ["AI", "Communication", "Cybersecurity", "Data", "Design", "DevOps", "Leadership"])
strengths = st.multiselect("Choose your strengths (you can pick more than one):",
    ["Problem-solving", "Creativity", "Empathy", "Leadership", "Analytical Thinking"],
    help="Hold Ctrl (or Command on Mac) to select multiple options.")
learning_style = st.radio("Preferred Learning Style", ["Visual", "Hands-on/Practical Learning", "Self-paced"])
career_goal = st.selectbox("What is your primary motivation for pursuing a tech career?",
    ["Competitive salary and growth potential", "Flexibility and remote work opportunities", 
     "Opportunities to be creative and innovative", "Desire to solve real-world problems", 
     "Interest in managing or leading teams"])
tech_level = st.selectbox("Tech Exposure Level", ["Beginner", "Intermediate", "Advanced"])


# --- Career Scoring ---
careers = {"Data Analyst": 0,
    "Decision Intelligence Specialist": 0,
    "Product Designer": 0,
    "UI/UX Designer": 0,
    "Virtual Assistant Professional": 0,
    "Project Manager": 0,
    "AI Engineer": 0,
    "AI System Operator/LLM Operator": 0,
    "AI Tool Specialist/Prompt Engineer": 0,
    "Cybersecurity Specialist": 0,
    "Information Security Analyst": 0,
    "Threat Intelligence Analyst": 0,
    "DevOps Engineer": 0}

interest_map = {"Data": ["Data Analyst", "Decision Intelligence Specialist"],
    "Design": ["Product Designer", "UI/UX Designer"],
    "Communication": ["Virtual Assistant Professional"],
    "Leadership": ["Project Manager"],
    "AI": ["AI Engineer", "AI System Operator/LLM Operator", "AI Tool Specialist/Prompt Engineer"],
    "Cybersecurity": ["Cybersecurity Specialist", "Information Security Analyst", "Threat Intelligence Analyst"],
    "DevOps": ["DevOps Engineer"]}

for career in interest_map.get(interest, []):
    careers[career] += 2

for s in strengths:
    if s == "Problem-solving":
        careers["Data Analyst"] += 1
        careers["Cybersecurity Specialist"] += 1
        careers["DevOps Engineer"] += 1
    elif s == "Creativity":
        careers["Product Designer"] += 2
        careers["UI/UX Designer"] += 2
    elif s == "Empathy":
        careers["UI/UX Designer"] += 1
        careers["Virtual Assistant Professional"] += 2
    elif s == "Leadership":
        careers["Project Manager"] += 2
        careers["DevOps Engineer"] += 1
    elif s == "Analytical Thinking":
        careers["Data Analyst"] += 1
        careers["AI Engineer"] += 2
        careers["Cybersecurity Specialist"] += 1

if tech_level == "Intermediate":
    careers["AI Engineer"] += 1
    careers["DevOps Engineer"] += 1
    careers["Cybersecurity Specialist"] += 1
    careers["UI/UX Designer"] += 1
elif tech_level == "Advanced":
    careers["AI Engineer"] += 2
    careers["DevOps Engineer"] += 2
    careers["Cybersecurity Specialist"] += 2
    careers["UI/UX Designer"] += 2

# --- Career Descriptions ---
explanations = {"Data Analyst": "You enjoy analyzing and interpreting complex data to inform strategic decisions.",
    "Decision Intelligence Specialist": "You combine data, AI, and analytics to support smarter organizational decisions.",
    "Product Designer": "You thrive on creativity and creating intuitive product experiences.",
    "UI/UX Designer": "You love designing user-friendly and aesthetic digital experiences.",
    "Virtual Assistant Professional": "You're organized, tech-savvy, and love helping people remotely.",
    "Project Manager": "You lead with vision and help teams deliver projects successfully.",
    "AI Engineer": "You design intelligent systems that learn and adapt.",
    "AI System Operator/LLM Operator": "You help configure and manage large language models in real-world systems.",
    "AI Tool Specialist/Prompt Engineer": "You specialize in crafting effective prompts and using AI tools smartly.",
    "Cybersecurity Specialist": "You protect systems by identifying vulnerabilities and stopping threats.",
    "Information Security Analyst": "You monitor and protect data and IT infrastructure.",
    "Threat Intelligence Analyst": "You analyze and predict cyber threats to keep systems safe.",
    "DevOps Engineer": "You automate and maintain robust development and deployment systems."}

# --- Recommender Function ---
def recommend_career():
    top_3 = sorted(careers.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_3

# --- Logging Prevention ---
log_file = "user_logs.csv"
existing_names = []
if os.path.exists(log_file):
    try:
        existing_logs = pd.read_csv(log_file)
        existing_names = existing_logs["Name"].str.lower().tolist()
    except pd.errors.ParserError:
        st.warning("The log file is corrupted or unreadable. Please fix or delete `user_logs.csv`.")

# --- Career Recommendation ---
if st.button("Click for Career Recommendation"):
    if not name:
        st.warning("Please enter your name to continue.")
    elif name.lower() in existing_names:
        st.error("You've already submitted your details. Only one entry per person is allowed.")
    else:
        top_matches = recommend_career()
        st.success(f"Hi {name}, here are your top tech career matches:")

        for i, (career, score) in enumerate(top_matches):
            st.markdown(f"### {i+1}. {career}")
            st.markdown(f"- **Score**: {score}")
            st.markdown(f"- **Why?** {explanations.get(career, 'No explanation available.')}")
            st.markdown("---")

        # Save top match only for logging
        log_data = {
            "Name": name,
            "Age": age_range,
            "Gender": gender,
            "Education": education,
            "Interest": interest,
            "Strengths": ", ".join(strengths),
            "Learning_Style": learning_style,
            "Tech_Level": tech_level,
            "Recommended_Career": top_matches[0][0],
            "Timestamp": pd.Timestamp.now()}

        log_df = pd.DataFrame([log_data])
        if os.path.exists(log_file):
            log_df.to_csv(log_file, mode='a', header=False, index=False)
        else:
            log_df.to_csv(log_file, mode='w', header=True, index=False)

# --- Stop Here Divider ---
st.markdown("---")
st.markdown("Please Note: This suggestion is based on the input received from you")
st.markdown("### ✅ Now that you have your Recommendation, you've reached the end of the Career Recommender.")


# --- Admin Section ---
st.markdown("---")
admin_key = st.text_input("Admin Access Key", type="password")
if admin_key == st.secrets["admin"]["key"]:
    st.success("Admin access granted.")
    if os.path.exists(log_file):
        df_logs = pd.read_csv(log_file)
        st.subheader("All Submissions")
        st.dataframe(df_logs, use_container_width=True)
        csv = df_logs.to_csv(index=False).encode('utf-8')
        st.download_button("Download Full CSV Log", csv, "user_logs.csv", "text/csv")
    else:
        st.info("No user data logged yet.")
elif admin_key != "":
    st.error("Invalid admin key.")

# --- Footer ---
st.markdown("---")
st.caption("Built for 3MTT Knowledge Showcase | Abimbola O. Ige")
