import requests
from bs4 import BeautifulSoup

def fetch_last_7_days_news(search_query):
    """Scrapes live headlines from Google News RSS."""
    try:
        # We use the search query (like "Kurnool, Andhra Pradesh") to find local news
        url = f"https://news.google.com/rss/search?q={search_query}+when:7d&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="xml")
        
        # Grab all the headlines
        headlines = [item.title.text for item in soup.find_all("item")]
        return headlines
        
    except Exception as e:
        print(f"Error finding news: {e}")
        return []