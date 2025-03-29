import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    """Scrapes a website and extracts titles, links, and descriptions."""
    try:
        # Send HTTP request
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extracting all articles (Modify based on website structure)
        articles = soup.find_all("article")  # Change this for other websites

        scraped_data = []
        for article in articles:
            title = article.find("h2").text.strip() if article.find("h2") else "No Title"
            link = article.find("a")["href"] if article.find("a") else "No Link"
            description = article.find("p").text.strip() if article.find("p") else "No Description"
            scraped_data.append([title, link, description])

        return scraped_data

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return []

def save_to_csv(data, filename="scraped_data.csv"):
    """Saves extracted data to a CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Link", "Description"])  # Column headers
            writer.writerows(data)
        print(f"✅ Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving CSV: {e}")

def main():
    """Main function to initiate web scraping."""
    url = input("🌍 Enter website URL to scrape: ").strip()

    print("\n🔎 Scraping data, please wait...\n")
    scraped_data = scrape_website(url)

    if scraped_data:
        for item in scraped_data:
            print(f"📌 Title: {item[0]}")
            print(f"🔗 Link: {item[1]}")
            print(f"📄 Description: {item[2]}\n")
        
        save_to_csv(scraped_data)
    else:
        print("⚠️ No data extracted. Try a different website.")

if __name__ == "__main__":
    main()
