import requests
from bs4 import BeautifulSoup

# --- Constituency Mapping ---
CONSTITUENCY_DATA = {
    "Kurnool": ["Byreddy Shabari", "P. G. Rampullaiah Yadav"],
    "Gurgaon": ["Naveen Jindal", "Raj Babbar"],
    "New Delhi": ["Bansuri Swaraj", "Somnath Bharti"]
}

def get_candidates_for_constituency(location):
    """Returns the list of candidates for a given constituency."""
    return CONSTITUENCY_DATA.get(location, [])

# --- Live News Scraper ---
def fetch_last_7_days_news(candidate_name):
    """Scrapes live headlines from Google News RSS for the last 7 days."""
    try:
        # Query format: [Name] when:7d (specific to Google News RSS)
        url = f"https://news.google.com/rss/search?q={candidate_name}+when:7d&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="xml")
        headlines = [item.title.text for item in soup.find_all("item")]
        return headlines
    except Exception as e:
        print(f"Error fetching news for {candidate_name}: {e}")
        return []