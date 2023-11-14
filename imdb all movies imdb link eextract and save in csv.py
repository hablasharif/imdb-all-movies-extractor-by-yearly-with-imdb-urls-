import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def generate_urls(base_url, increment, total_results, results_per_page):
    num_links = total_results // results_per_page
    urls = []

    for i in range(increment + 1, num_links * increment + 1, increment):
        url = f"{base_url}&start={i}&ref_=adv_nxt"
        urls.append(url)

    return urls

def scrape_data(current_url):
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract your desired information here
    # For example, you might want to extract movie titles, ratings, etc.

    # Find the "Next" link if it exists
    next_link = soup.find("a", {"class": "lister-page-next"})

    if next_link:
        next_url = urljoin(base_url, next_link["href"])
        return next_url
    else:
        return None

# Streamlit app
st.title("IMDb Scraper App")

# Set initial parameters
base_url = "https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31"
increment = 50
total_results = 10000
results_per_page = 50

# Generate URLs
urls = generate_urls(base_url, increment, total_results, results_per_page)

# Display the URLs
st.sidebar.title("Generated URLs")
st.sidebar.text("\n".join(urls))

# Scrape and display data
for url in urls:
    st.write(f"Scraping data from {url}")
    current_url = url
    while current_url:
        current_url = scrape_data(current_url)
        if current_url:
            st.write(f"Next URL: {current_url}")


# Normal Code of this streamlit codes 

base_url = "https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31"
# increment = 50  # Increment by 50 to get the desired page numbers
# results_per_page = 50  # Number of results per page
# total_results = 10000  # Total number of results
# num_links = total_results // results_per_page  # Calculate the number of links based on total results

# for i in range(increment + 1, num_links * increment + 1, increment):
#     url = f"{base_url}&start={i}&ref_=adv_nxt"
#     print(url)


# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# base_url = "https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&start=9951&ref_=adv_nxt"
# current_url = base_url

# while current_url:
#     response = requests.get(current_url)
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Extract your desired information here
#     # For example, you might want to extract movie titles, ratings, etc.

#     # Find the "Next" link if it exists
#     next_link = soup.find("a", {"class": "lister-page-next"})

#     if next_link:
#         next_url = urljoin(base_url, next_link["href"])
#         current_url = next_url
#         print(current_url)
#     else:
#         current_url = None
