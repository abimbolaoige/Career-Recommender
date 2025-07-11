import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Career Recommender", layout="centered")

# Page title
st.title("🎯 AI-Powered Career Path Recommender")
st.write("Answer a few questions and get matched to your ideal tech career!")

# User inputs
name = st.text_input("Your Name")
education = st.selectbox("Education Level", ["SSCE", "OND", "HND", "BSc", "MSc"])
interest = st.selectbox("Which area interests you most?", ["Data", "Design", "Communication", "Leadership", "AI"])
strengths = st.multiselect("What are your top strengths?", ["Problem-solving", "Creativity", "Empathy", "Leadership", "Analytical Thinking"])
learning_style = st.radio("Preferred Learning Style", ["Visual", "Hands-on", "Self-paced"])
tech_level = st.selectbox("Tech Exposure Level", ["Beginner", "Intermediate", "Advanced"])

# Rule-based logic with explanation
def recommend_career(interest, strengths, tech_level):
    if interest == "Data" and "Problem-solving" in strengths:
        return "Data Analyst", "You enjoy working with data and solving problems — this role matches your logical mindset and curiosity."
    elif interest == "Design" and "Creativity" in strengths:
        return "Product Designer", "Your creative flair and design interest are ideal for crafting digital products and user experiences."
    elif interest == "Communication" and "Empathy" in strengths:
        return "Technical Writer", "Your communication skills and empathy are valuable for explaining complex topics clearly."
    elif interest == "Leadership" and "Leadership" in strengths:
        return "Project Manager", "Your leadership traits suggest you’d excel at coordinating teams and driving results."
    elif interest == "AI" and tech_level in ["Intermediate", "Advanced"]:
        return "AI Engineer", "You have the tech background and interest in AI — this field is future-ready and innovative."
    else:
        return "Career Exploration Needed", "You may still be exploring your strengths — consider internships or learning programs in different tech areas."

# Save user input to CSV
def log_user_data(data, filename="user_logs.csv"):
    df = pd.DataFrame([data])
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)

# Button to generate result
if st.button("🔍 Recommend Career"):
    if name:
        result, explanation = recommend_career(interest, strengths, tech_level)

        # Display result
        st.success(f"Hi **{name}**, you’d make a great **{result}**!")
        st.info(f"💡 **Why?** {explanation}")

        # Log data
        user_data = {
            "Name": name,
            "Education Level": education,
            "Interest Area": interest,
            "Key Strengths": ', '.join(strengths),
            "Learning Style": learning_style,
            "Tech Exposure": tech_level,
            "Recommended Career": result
        }
        log_user_data(user_data)
    else:
        st.warning("Please enter your name to proceed.")

# Footer
st.markdown("---")
st.caption("Built for 3MTT Knowledge Showcase | Powered by Data + AI 🔬")
