def get_salary_estimate(job_title, location="United States"):
    salary_data = {
        "Software Developer": {"avg_salary": 85000, "range": "65k-110k"},
        "Data Scientist": {"avg_salary": 100000, "range": "80k-130k"},
        "UX Designer": {"avg_salary": 75000, "range": "55k-100k"},
    }
    return salary_data.get(job_title, {"avg_salary": "Unknown", "range": "N/A"})
