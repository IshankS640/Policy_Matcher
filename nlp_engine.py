def analyze_news_sentiments(news_headlines):
    # Give a base score of 20 so it never starts at zero!
    scores = {"Technology": 20, "Healthcare": 20, "Economy": 20}

    for headline in news_headlines:
        text = headline.lower()
        
        # Look for simple, common words
        if "tech" in text or "digital" in text or "online" in text or "app" in text:
            scores["Technology"] += 15
        if "health" in text or "hospital" in text or "doctor" in text or "medical" in text:
            scores["Healthcare"] += 15
        if "economy" in text or "money" in text or "tax" in text or "jobs" in text:
            scores["Economy"] += 15

    # Make sure no score goes over 100
    for key in scores:
        if scores[key] > 100:
            scores[key] = 100

    return scores