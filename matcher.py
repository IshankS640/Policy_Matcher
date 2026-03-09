import math

def calculate_match_score(user_priorities, city_profile):
    distance = 0

    # Find the difference between what the user wants and what the city has
    for category in ["Technology", "Healthcare", "Economy"]:
        diff = user_priorities[category] - city_profile[category]
        distance += diff * diff

    # Basic Euclidean distance math
    euclidean_distance = math.sqrt(distance)

    # 173.2 is the absolute maximum distance possible. 
    # We use it to turn the number into a clean percentage (0 to 100%)
    match_percentage = 100 - ((euclidean_distance / 173.2) * 100)

    # Return a whole number so it looks clean on the screen (e.g., 75 instead of 75.432)
    return int(match_percentage)