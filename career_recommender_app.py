import streamlit as st

st.set_page_config(page_title="Tech Career Recommender", layout="centered")

st.title("🔍 Discover Your Ideal Tech Career!")
st.markdown("Answer the 6 quick questions below and get a tech career that fits your interests and strengths.")

# Define career options and initialize scores
careers = {
    "Data Analyst": 0,
    "UI/UX Designer": 0,
    "Backend Developer": 0,
    "Product Manager": 0,
    "AI/ML Engineer": 0,
    "DevOps Engineer": 0,
    "Cybersecurity Specialist": 0
}

# Question 1
q1 = st.radio("1. What excites you the most?", [
    "Understanding how users think",
    "Solving complex logic problems",
    "Making digital experiences look beautiful and intuitive",
    "Managing timelines and team goals",
    "Finding patterns in data",
    "Preventing or detecting cyber attacks",
    "Automating and optimizing software delivery"
])

if q1 == "Understanding how users think":
    careers["UI/UX Designer"] += 2
    careers["Product Manager"] += 1
elif q1 == "Solving complex logic problems":
    careers["Backend Developer"] += 2
    careers["AI/ML Engineer"] += 1
elif q1 == "Making digital experiences look beautiful and intuitive":
    careers["UI/UX Designer"] += 3
elif q1 == "Managing timelines and team goals":
    careers["Product Manager"] += 3
elif q1 == "Finding patterns in data":
    careers["Data Analyst"] += 3
    careers["AI/ML Engineer"] += 1
elif q1 == "Preventing or detecting cyber attacks":
    careers["Cybersecurity Specialist"] += 3
elif q1 == "Automating and optimizing software delivery":
    careers["DevOps Engineer"] += 3

# Question 2
q2 = st.radio("2. You’d rather spend your day...", [
    "Designing wireframes or prototypes",
    "Writing Python or JavaScript code",
    "Reviewing data in spreadsheets or dashboards",
    "Leading a team to ship a new feature",
    "Training a machine learning model",
    "Configuring deployment pipelines",
    "Running security audits or penetration tests"
])

if q2 == "Designing wireframes or prototypes":
    careers["UI/UX Designer"] += 3
elif q2 == "Writing Python or JavaScript code":
    careers["Backend Developer"] += 3
elif q2 == "Reviewing data in spreadsheets or dashboards":
    careers["Data Analyst"] += 3
elif q2 == "Leading a team to ship a new feature":
    careers["Product Manager"] += 3
elif q2 == "Training a machine learning model":
    careers["AI/ML Engineer"] += 3
elif q2 == "Configuring deployment pipelines":
    careers["DevOps Engineer"] += 3
elif q2 == "Running security audits or penetration tests":
    careers["Cybersecurity Specialist"] += 3

# Question 3
q3 = st.radio("3. Which best describes your strength?", [
    "Organizing tasks and prioritizing",
    "Creative thinking and visual storytelling",
    "Analytical thinking and numbers",
    "Solving backend tech issues",
    "Research and experimentation",
    "Securing systems and solving vulnerabilities",
    "System monitoring and CI/CD automation"
])

if q3 == "Organizing tasks and prioritizing":
    careers["Product Manager"] += 3
elif q3 == "Creative thinking and visual storytelling":
    careers["UI/UX Designer"] += 3
elif q3 == "Analytical thinking and numbers":
    careers["Data Analyst"] += 3
elif q3 == "Solving backend tech issues":
    careers["Backend Developer"] += 3
elif q3 == "Research and experimentation":
    careers["AI/ML Engineer"] += 3
elif q3 == "Securing systems and solving vulnerabilities":
    careers["Cybersecurity Specialist"] += 3
elif q3 == "System monitoring and CI/CD automation":
    careers["DevOps Engineer"] += 3

# Question 4
q4 = st.radio("4. You prefer learning through...", [
    "Design tools like Figma, Canva, etc.",
    "Analyzing case studies and business goals",
    "Online coding tutorials and GitHub",
    "Exploring data with charts and visuals",
    "Building predictive models from datasets",
    "Simulated cyberattack scenarios",
    "Hands-on server configuration challenges"
])

if q4 == "Design tools like Figma, Canva, etc.":
    careers["UI/UX Designer"] += 3
elif q4 == "Analyzing case studies and business goals":
    careers["Product Manager"] += 3
elif q4 == "Online coding tutorials and GitHub":
    careers["Backend Developer"] += 3
elif q4 == "Exploring data with charts and visuals":
    careers["Data Analyst"] += 3
elif q4 == "Building predictive models from datasets":
    careers["AI/ML Engineer"] += 3
elif q4 == "Simulated cyberattack scenarios":
    careers["Cybersecurity Specialist"] += 3
elif q4 == "Hands-on server configuration challenges":
    careers["DevOps Engineer"] += 3

# Question 5
q5 = st.radio("5. If you had to lead a project, you'd choose to...", [
    "Create an app that predicts user behavior using AI",
    "Design a sleek mobile banking interface",
    "Develop the server-side logic of a booking system",
    "Build an interactive dashboard for business insights",
    "Coordinate teams to launch a product in 3 weeks",
    "Create a secure login/authentication system",
    "Automate deployment for a multi-region app"
])

if q5 == "Create an app that predicts user behavior using AI":
    careers["AI/ML Engineer"] += 3
elif q5 == "Design a sleek mobile banking interface":
    careers["UI/UX Designer"] += 3
elif q5 == "Develop the server-side logic of a booking system":
    careers["Backend Developer"] += 3
elif q5 == "Build an interactive dashboard for business insights":
    careers["Data Analyst"] += 3
elif q5 == "Coordinate teams to launch a product in 3 weeks":
    careers["Product Manager"] += 3
elif q5 == "Create a secure login/authentication system":
    careers["Cybersecurity Specialist"] += 3
elif q5 == "Automate deployment for a multi-region app":
    careers["DevOps Engineer"] += 3

# Question 6
q6 = st.radio("6. What’s your ideal work environment?", [
    "Working closely with designers and developers",
    "Tackling technical tasks independently",
    "Collaborating on business strategy",
    "Being given data and asked to explain what it means",
    "Solving visual layout and design problems",
    "Protecting systems in a fast-paced environment",
    "Ensuring smooth and reliable software releases"
])

if q6 == "Working closely with designers and developers":
    careers["Product Manager"] += 2
    careers["UI/UX Designer"] += 1
elif q6 == "Tackling technical tasks independently":
    careers["Backend Developer"] += 3
elif q6 == "Collaborating on business strategy":
    careers["Product Manager"] += 3
elif q6 == "Being given data and asked to explain what it means":
    careers["Data Analyst"] += 3
elif q6 == "Solving visual layout and design problems":
    careers["UI/UX Designer"] += 3
elif q6 == "Protecting systems in a fast-paced environment":
    careers["Cybersecurity Specialist"] += 3
elif q6 == "Ensuring smooth and reliable software releases":
    careers["DevOps Engineer"] += 3

# Submit Button
if st.button("🚀 Show My Career Match"):
    best_match = max(careers, key=careers.get)
    st.success(f"🎯 Your Ideal Tech Career Path is: **{best_match}**")

    # Career Descriptions
    descriptions = {
        "Data Analyst": "You love digging into data, spotting trends, and presenting insights that drive decisions.",
        "UI/UX Designer": "You’re creative, user-focused, and passionate about building visually appealing and intuitive experiences.",
        "Backend Developer": "You enjoy solving deep technical problems and building the logic that powers applications.",
        "Product Manager": "You thrive on strategy, collaboration, and bringing people and ideas together to ship products.",
        "AI/ML Engineer": "You’re curious, experimental, and love creating smart systems that learn from data.",
        "DevOps Engineer": "You’re process-driven and love ensuring applications are fast, scalable, and always available.",
        "Cybersecurity Specialist": "You're vigilant and technical, passionate about defending systems and preventing security breaches."
    }

    st.markdown(f"**Why?** {descriptions[best_match]}")
    st.markdown("🔗 Learn more with free resources on [Coursera](https://coursera.org), [freeCodeCamp](https://freecodecamp.org), or [YouTube](https://youtube.com).")
