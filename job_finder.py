import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def extract_job_info(job_element):
    title = job_element.find("h2", class_="title").a["title"]
    company = job_element.find("span", class_="company").get_text(strip=True)
    location = job_element.find("span", class_="location").get_text(strip=True)
    summary = job_element.find("div", class_="summary").get_text(strip=True)

    return [title, company, location, summary]

def scrape_indeed_jobs(search_query, num_pages=1, location=""):
    base_url = "https://www.indeed.com/jobs"
    jobs = []

    for page in range(num_pages):
        params = {
            "q": search_query,
            "l": location,
            "start": page * 10
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            job_elements = soup.find_all("div", class_="jobsearch-SerpJobCard")

            for job_element in job_elements:
                job_info = extract_job_info(job_element)
                jobs.append(job_info)
        else:
            print(f"Failed to fetch jobs with status code: {response.status_code}")
            break

    return jobs

def display_jobs(jobs):
    headers = ["Title", "Company", "Location", "Summary"]
    print(tabulate(jobs, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    search_query = input("Enter the job title or keywords: ")
    location = input("Enter the job location (city, state or country): ")
    num_pages = int(input("Enter the number of pages to search (default is 1): ") or 1)

    jobs = scrape_indeed_jobs(search_query, num_pages, location)
    if jobs:
        display_jobs(jobs)
    else:
        print("No jobs found.")
