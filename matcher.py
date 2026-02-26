import math

def calculate_match_score(user_input, candidate_scores):
    """
    Calculates the mathematical proximity between user priorities 
    and candidate scores using Euclidean Distance.
    """
    # 1. Sum of squared differences for all categories (Tech, Health, Economy)
    distance = sum((user_input[cat] - candidate_scores.get(cat, 0)) ** 2 for cat in user_input)
    
    # 2. Square root of the sum
    euclidean_dist = math.sqrt(distance)
    
    # 3. Normalize the score
    # Max distance for 3 categories (scale 0-10) is sqrt(3 * 10^2) ≈ 17.32
    max_dist = math.sqrt(3 * (10**2)) 
    
    # 4. Convert to a 0-100% match (Lower distance = Higher match)
    match_percentage = max(0, 100 * (1 - (euclidean_dist / max_dist)))
    
    return round(match_percentage, 2)