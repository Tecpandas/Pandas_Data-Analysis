from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

from bs4 import BeautifulSoup
import time

def fetch_reviews_selenium(url, num_pages=5):
    reviews = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}...")
        driver.get(f"{url}page/{page}/")
        time.sleep(3)  # Allow time for JavaScript to load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        review_blocks = soup.find_all("article", class_="comp_review")

        for block in review_blocks:
            airline_name = block.find("h2").text.strip() if block.find("h2") else "N/A"
            rating_tag = block.find("span", class_="rating-score")
            rating = rating_tag.text.strip() if rating_tag else "N/A"
            review_text = block.find("div", class_="text_content").text.strip() if block.find("div", class_="text_content") else "N/A"
            date = block.find("time").text.strip() if block.find("time") else "N/A"

            reviews.append({
                "Airline": airline_name,
                "Rating": rating,
                "Review": review_text,
                "Date": date
            })
    
    driver.quit()
    return reviews

# Example usage
skytrax_url = "https://www.airlinequality.com/airline-reviews/emirates/"
reviews_data = fetch_reviews_selenium(skytrax_url, num_pages=5)

# Save to CSV
df = pd.DataFrame(reviews_data)
df.to_csv("data/airline_reviews.csv", index=False)

print("Scraping completed.")
