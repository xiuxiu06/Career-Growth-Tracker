from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from scraper import scrape_jobs
from ai import get_skill_recommendations
from salary import get_salary_estimate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to SkillSync API"}

@app.get("/jobs/{job_title}")
def get_jobs(job_title: str):
    return {"jobs": scrape_jobs(job_title)}

@app.get("/skills/{job_title}")
def get_skills(job_title: str):
    return {"skills": get_skill_recommendations(job_title)}

@app.get("/salary/{job_title}")
def get_salary(job_title: str):
    return {"salary": get_salary_estimate(job_title)}