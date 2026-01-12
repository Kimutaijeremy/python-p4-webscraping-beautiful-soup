from turtle import ht
from bs4 import BeautifulSoup
import requests


def scrape_flatiron():
    headers = {'user-agent': 'my-app/0.0.1'}
    
    # Get the main page
    html = requests.get("https://flatironschool.com/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Example 1: Get the main heading
    heading = doc.select('.heading-financier')
    if heading:
        print("Main Heading:", heading[0].get_text(strip=True))
    
    # Example 2: Get course titles from courses page
    html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    courses = doc.select('.heading-60-black.color-black.mb-20')
    print("\nCourses found:")
    for course in courses:
        print(course.get_text(strip=True))

if __name__ == "__main__":
    scrape_flatiron()