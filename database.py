import requests
from bs4 import BeautifulSoup

# --- New Logic: Constituency Mapping ---
# This dictionary simulates a database of candidates per region
CONSTITUENCY_DATA = {
    "Kurnool": ["Byreddy Shabari", "P. G. Rampullaiah Yadav"],
    "Gurgaon": ["Naveen Jindal", "Raj Babbar"],
    "New Delhi": ["Bansuri Swaraj", "Somnath Bharti"]
}

def get_candidates_for_constituency(location):
    """
    Returns a list of candidates for a specific area.
    If the area is not found, it returns an empty list.
    """
    return CONSTITUENCY_DATA.get(location, [])

# --- Existing News Scraper ---
def fetch_last_7_days_news(candidate_name):
    """Scrapes live headlines from Google News RSS."""
    try:
        url = f"https://news.google.com/rss/search?q={candidate_name}+when:7d&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="xml")
        headlines = [item.title.text for item in soup.find_all("item")]
        return headlines
    except Exception as e:
        print(f"Error: {e}")
        return []