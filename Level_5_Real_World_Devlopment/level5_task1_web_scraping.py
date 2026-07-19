# Basic Web Scraping using BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        print("\nPage Title:")
        print(soup.title.string)

        print("\nHeadings (H1 Tags):")
        headings = soup.find_all("h1")

        if len(headings) == 0:
            print("No H1 tags found.")
        else:
            for heading in headings:
                print("-", heading.text.strip())

    else:
        print("Unable to access website.")

except Exception as e:
    print("Error:", e)
input("\nPress Enter to exit...")