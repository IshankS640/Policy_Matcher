# database.py

# The dictionary of keywords the AI will look for
topics = {
    "education": ["school", "college", "university", "student", "teacher", "degree", "education"],
    "healthcare": ["hospital", "doctor", "health", "medicine", "clinic", "patient", "care"],
    "technology": ["ai", "digital", "internet", "software", "tech", "startup", "innovation", "data"],
    "agriculture": ["farmer", "crop", "land", "irrigation", "village", "seeds", "agriculture"]
}

# Base Toy Data (So the app always has someone to compare against)
baseline_candidates = [
    {"name": "Minister Alpha (Baseline)", "education": 9, "healthcare": 4, "technology": 8, "agriculture": 3},
    {"name": "Minister Beta (Baseline)", "education": 3, "healthcare": 9, "technology": 4, "agriculture": 7}
]