import requests
from bs4 import BeautifulSoup


def scrape_jobs(job_title):
    url = f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job in soup.select(".job_seen_beacon"):
        title = job.select_one(".jobTitle").text.strip()
        company = job.select_one(".companyName").text.strip()
        location = job.select_one(".companyLocation").text.strip()
        jobs.append({"title": title, "company": company, "location": location})

    return jobs
