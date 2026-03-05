def analyze_news_sentiments(news_list):
    """
    Analyzes news headlines to generate a policy profile for a candidate.
    This acts as a 'Feature Extractor' for our matching algorithm.
    """
    # Initializing scores for our primary categories
    scores = {"Technology": 0, "Healthcare": 0, "Economy": 0}
    
    # Defining 'Policy Keywords' to look for in unstructured news text
    keywords = {
        "Technology": ["ai", "digital", "tech", "software", "semiconductor", "innovation", "startup"],
        "Healthcare": ["hospital", "health", "medical", "vaccine", "doctor", "ayushman", "pharma"],
        "Economy": ["gdp", "tax", "budget", "finance", "market", "trade", "investment", "inflation"]
    }
    
    # Logic: For every headline, check if it contains our target policy keywords
    for headline in news_list:
        text = headline.lower()
        for category, tags in keywords.items():
            for tag in tags:
                if tag in text:
                    # We increment the score for that policy category
                    scores[category] += 2  
    
    # Normalizing scores to a 1-10 scale so the Matcher can use them
    for cat in scores:
        # We ensure the score is at least 1 and no more than 10
        scores[cat] = min(10, max(1, scores[cat]))
        
    return scores