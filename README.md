# Career-Recommender

## AI-Powered Tech Career Recommender App by Abimbola Odunola Ige - FE/24/8023274694 (3MTT Cohort 3 Fellow)
## Data Analysis and Visualization 

### Introduction
The AI Career Recommender App is a personalized recommendation tool designed to help individuals especially beginners or career switcher—identify their most suitable career paths in the technology ecosystem. Built for the 3MTT Knowledge Showcase, the app leverages user inputs such as interests, strengths, education, and learning preferences to suggest relevant tech careers.

The app is developed by Abimbola Odunola Ige using Streamlit, a Python-based open-source app framework, and is hosted here on GitHub for easy access, maintenance, and collaboration. 

[Click here to view the App](https://career-recommender-tefeyugyzyezhgzuvipbc6.streamlit.app)

The app uses rule-based logic to assign scores and recommend careers. These recommendations are logged and later visualized in Power BI

### Background to the App Creation
Let's just say I am a Tech Advocate, one question I always ask when I meet someone is:
"Which area of tech are you in?" And if the answer is "None", my next question is — Why not?

The Federal Government of Nigeria, through the 3MTT (3 Million Technical Talents) program by the Ministry of Communications, Innovation & Digital Economy, has made it possible for every Nigerian to access free tech training.

Still, I noticed a recurring challenge: “I don’t even know which area of tech to go into.”

That became the inspiration behind this July Knowledge Showcase project.

#### How It Works

Users fill a simple form with:
1. Personal Info
* Name (for logging purposes)
* Age Range
* Gender
* Education Level

2. Career Input Factors : Career Interest & Strengths 
* Area of Interest (e.g., AI, Cybersecurity, Design, etc.)
* Key Strengths (e.g., problem-solving, empathy, leadership)
* Preferred Learning Style - Visual, Hands-on/Practical Learning, Self-paced
* Tech Exposure Level (Beginner to Advanced)
* Career Motivation (e.g., flexibility, desire to solve real-world problems, leading teams...etc)

3. AI-Powered Matching:  Based on rule-based logic and weighted scoring, the app evaluates all responses and recommends Top 2 tech career roles most aligned with the user’s profile. Each role comes with:
* A match score
* A tailored explanation for the recommendation

4. Data Logging
Each submission is logged into a CSV file for monitoring patterns and performing insights analysis.

Career Roles Covered - The section uses; Flexibility, Innovation, Problem-solving

#### The app currently supports intelligent matching across multiple tech roles including:
* Data Analyst
* Product Designer
* Cybersecurity Specialist
* AI Engineer
* DevOps Engineer
* Project Manager
* Virtual Assistant Professional
* UI/UX Designer
* Information Security Analyst
* Decision Intelligence Specialist

#### How It Helps Users
* Area  - Value   
* Career Discovery - Helps users explore roles they may not have considered.
* Clarity - Simplifies decision-making for learners unsure where to begin. 
* Confidence Boost - Offers a personalized recommendation backed by a logic-based system.               
* Accessibility - Fast, user-friendly, and does not require technical knowledge to use.
* Planning - Users can use the result to plan specific courses, certifications, or mentorships. 
* It is useful for Stakeholders & Educators

#### Stakeholder - Benefits
* Training Providers - Identify the most in-demand career paths and tailor training programs. 
* Policy Makers - Gather real-life interest data to support digital skill development.
* Career Coaches - Use as a conversation starter or baseline for deeper guidance.
* 3MTT Mentors & Fellows - Track learner interest patterns and align cohorts accordingly.

#### Challenges Faced
When I checked the progress of user’s input and see some blank fields, I had to use a markdown to amplify (“Please do not leave any field blank. All questions are required to give you the most accurate career match."), yet users still skipped some sections, and it will affect my analysis. I used elif to prevent user from skipping any field, without which it will not give you your recommendation. I had to keep committing to changes until the information are well captured using attractive interface with simple understanding by the users.

#### The Section of Career Recommendation Code:
``` 
if st.button("Click for Career Recommendation"):
    name = name.strip()
    required_fields = [age_range, gender, education, interest, career_goal, tech_level]

    if not name:
        st.warning("Please enter your name to continue.")
    elif name.lower() in existing_names:
        st.error("You've already submitted your details. Only one entry per person is allowed.")
    elif any(field == "Choose an option" for field in required_fields):
        st.warning("Please select valid options for all fields.")
    elif not strengths:
        st.warning("Please select at least one strength.")
    else:
        top_matches = recommend_career()
        st.success(f"Hi {name}, here are your top tech career matches:")
```

Committing to app code modification/update changes is a maintenance and edit made easy on GitHub hosting with Streamlit. 

##### App still under development and open to work with product designers, product managers and techies for upgrade.

### How the App works: Example Scenario
```
Full python code in main Career-Recommendation /career_recommender_app.py
```
A 24-year-old female user with a BSc in Social Science selects "Communication" as her interest, "Empathy" and "Leadership" as strengths, and prefers hands-on learning. The app recommends:

1. Virtual Assistant Professional
2. Project Manager; with justifications that these roles align with her empathy, communication strength, and preferred leadership path.

This was arrived at through the strength section using the code below:
```
def recommend_career():
    top_2 = sorted(careers.items(), key=lambda x: x[1], reverse=True)[:2]
    return top_2
```
In the AI Tech career recommender app, the idea of adding scores in the code is part of a rule-based AI logic system. It helps determine which career best matches the user's profile based on their answers. Each time the user selects an option (like their interest, strength, or learning style), the code adds a score to one or more of those careers, depending on how relevant the answer is to that career. The list of career tuples is sorted based on the value (i.e., the score).

This allows the app to:
* Rank career options based on relevance to the user's inputs.
* Personalize the recommendation to the top 2 (the ones with the highest score is shown in desc; reverse=True, showing highest score first).
* Simulate “thinking” like a human adviser who weighs different factors.

```
top_2 = sorted(
    careers.items(),       # Get all career-score pairs
    key=lambda x: x[1],    # Sort by score (value)
    reverse=True           # In descending order
)[:2]                      # Take top 2
```

#### List of Careers
```
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
```

Example of score features: Let’s say someone selects "Creativity" as a strength: possible career will be:
```
if s == "Creativity":
    careers["Product Designer"] += 2
    careers["Technical Writer"] += 1
    careers["UI/UX Designer"] += 2
```

#### What The Scoring Code Does:

The code is trying to match people to the best tech careers based on two things:
1. Their personal strengths (like creativity, leadership, empathy, etc.)
2. Their current tech skill level (Beginner, Intermediate, or Advanced)

##### Each career gets points when someone’s strength or skill level matches what’s important for that career. The careers with the most points are likely to be the best fit.

###### 1. Checking Personal Strengths

The first part goes through each strength the user selects. For example:

```python
for s in strengths:
```

This means: “For every strength the person picked, let’s check what careers it fits.”

Then, for each strength:

* Problem-solving gives 1 point each to:
  * Data Analyst
  * Cybersecurity Specialist
  * DevOps Engineer
Because those jobs need strong problem-solvers.

* Creativity gives 2 points each to:
  * Product Designer
  * UI/UX Designer
Because these roles involve coming up with creative ideas and designs.

* Empathy gives:
  * 1 point to UI/UX Designer (to understand user needs)
  * 2 points to Virtual Assistant Professional (to support people effectively)

* Leadership gives:
  * 2 points to Project Manager (they lead teams)
  * 1 point to DevOps Engineer (often work across teams)

* Analytical Thinking gives:
  * 1 point to Data Analyst (analyzing data is their job)
  * 2 points to AI Engineer (AI needs strong logic and analysis)
  * 1 point to Cybersecurity Specialist (to analyze threats)

#### 2. Checking Tech Skill Level

This part checks if the person is at a beginner, Intermediate or Advanced tech level:

```python
if tech_level == "Intermediate":
```

If yes, it gives 1 point each to these jobs:

* AI Engineer
* DevOps Engineer
* Cybersecurity Specialist
* UI/UX Designer

Because these roles need some experience in tech tools and concepts.

If the person is Advanced, it gives 2 points each to those same roles:

```python
elif tech_level == "Advanced":
```
Because these jobs become more fitting if you have deep tech knowledge.

How the Final Recommendation Works: At the end of all the questions, the code “Find the first two careers that has the highest scores, and recommend that one.”:
```
best_match = max(careers, key=careers.get)
```
Each career is like a bucket. Every time a user's answer relates to a career, the user drops a point into that bucket. At the end, the bucket with the most points is the recommended career.

### The Power BI Dashboard
This dashboard presents insights derived from real user data collected via a custom-built AI Career Recommender App. Developed using Streamlit (Python) and hosted on GitHub, the app recommends ideal tech careers based on user input such as interest, education, strengths, and preferred learning style.

Please find the user.log.csv file attached below.
[Open the CSV Dataset](https://drive.google.com/file/d/1yUmtciaGwFzkk2uQSeMFg87Y9DBlGgwh/view?usp=drive_link)
[Power BI Analysis](https://drive.google.com/file/d/1oQb2Vg738JAliv7ge6vVIdZDaFKtWn9W/view?usp=drive_link)
[PDF Link](https://drive.google.com/file/d/1rjTNYnEwWoii6BkfxCf1uNSxBjeeltpw/view?usp=drive_link)

### The dashboard aims to:
* Help users understand how their attributes align with career roles
* Provide stakeholders with visibility into career trends and user demographics
* Demonstrate how data can drive career decisions in tech
* Data Cleaning Process and Dax Functions Used

#### Key Visual Insights

1. Top Interest Area - Data and Design tied as the most common areas of interest (22 counts each) Users are gravitating toward data-centric and creative roles.
2. Most Recommended Career - Data Analyst emerged as the top recommended career - This reinforces the strong match between user attributes and analytical roles.
3. Submissions by Age Group - Dominant age brackets: Under 18, 18-24, and 25–34 - This shows interest mostly among early- to mid-career individuals.
4. Learning Style Preference - Majority (48%) prefer Visual Learning, this indicates a strong need for visually rich content or platforms (videos, infographics, UI tools).
5. Tech Exposure Level - Most users identified as Beginners, emphasizing that the app is valuable for entry-level tech aspirants.
6. Strengths-to-Career Breakdown - "Problem-solving" aligns with Data Analyst, Cybersecurity Specialist, and DevOps Engineer "Empathy" strongly maps to Virtual Assistant and UI/UX Designer
   
#### Loading the Data
* I loaded the data by Opening Power BI Desktop
* Click “Home”,  “Get Data”, “Text/CSV”
* Select the Tech Recommendation Data.csv file and “Load”

#### Open Power Query Editor
From Home, open Transform Data , This automatically opens the Power Query Editor

Clean & Prepare the Data
1. Removal of Blank Rows - I look through the table preview and filter out any blank rows using the drop-down filters on each column.
   
2. Split Strengths Column into Multiple Values
I selected the Strengths column
Clicked “Split Column”, “By Delimiter”
Choose Comma ( , ) and Split into Columns

3. Trim Whitespace
Selected Name Column since it is the only manual entry space
Clicked “Transform”, “Format” and “Trim” to remove leading/trailing spaces in Names

4. Confirmed the Data Types
I ensure proper data types:
Name: Text
Age, Gender, Tech Level, Education, Interest, Recommended Career: Text
Timestamp: Date/Time

5. Handle Missing Values
Strengths - Users picked as applicable, hence some were blank. I replaced "null" value with "None" and also splitted the columns to 5; Strength.1, Strength.2, Strength.3, Strength.4, Strength.5

6. Rename Columns:
I renamed Learning_Style - Learning Style, Timestamp - Time Stamp etc. for better readability
I clicked “Close & Apply” to return to the main Power BI workspace

#### Conclusion

This AI-powered tool serves as a smart, simple decision assistant for aspiring tech professionals. Whether used independently or embedded in digital literacy campaigns like 3MTT, it empowers users to start their tech journey with purpose and direction. Built with Streamlit & Python, hosted on GitHub by

#### Abimbola Odunola Ige
[Let's Connect on LinkedIn](https://www.linkedin.com/in/abimbola-ige-6a7377287)

