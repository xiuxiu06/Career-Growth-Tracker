import streamlit as st
import requests

st.title("SkillSync - AI-Powered Career Growth Tracker")

job_title = st.text_input("Enter your job title:", "Software Developer")

if st.button("Get Career Insights"):
    jobs = requests.get(f"http://127.0.0.1:8000/jobs/{job_title}").json()["jobs"]
    skills = requests.get(f"http://127.0.0.1:8000/skills/{job_title}").json()["skills"]
    salary = requests.get(f"http://127.0.0.1:8000/salary/{job_title}").json()["salary"]

    st.subheader("💼 Job Listings")
    for job in jobs[:5]:
        st.write(f"- **{job['title']}** at {job['company']} ({job['location']})")

    st.subheader("📚 Recommended Skills")
    st.write(skills)

    st.subheader("💰 Salary Estimate")
    st.write(f"Average Salary: ${salary['avg_salary']} ({salary['range']})")
