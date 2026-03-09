import streamlit as st
# I added CANDIDATE_MAP to the import line right here:
from constituencies import STATE_CONSTITUENCY_MAP, CANDIDATE_MAP
from database import fetch_last_7_days_news
from nlp_engine import analyze_news_sentiments
from matcher import calculate_match_score

st.title("📍 Constituency Candidate Matcher")
st.write("Compare candidates in your area based on your personal policy priorities.")

# --- SIDEBAR (Sliders) ---
st.sidebar.header("Set Your Priorities")
tech = st.sidebar.slider("Technology", 0, 100, 50)
health = st.sidebar.slider("Healthcare", 0, 100, 50)
econ = st.sidebar.slider("Economy", 0, 100, 50)
user_priorities = {"Technology": tech, "Healthcare": health, "Economy": econ}

# --- MAIN SCREEN (Dropdowns) ---
st.subheader("Select Your Location")

selected_state = st.selectbox("1. Select State:", options=list(STATE_CONSTITUENCY_MAP.keys()))
constituencies_in_state = STATE_CONSTITUENCY_MAP[selected_state]
selected_constituency = st.selectbox("2. Select Constituency:", options=constituencies_in_state)

# --- RUN BUTTON ---
if st.button("Run Analysis"):
    search_query = f"{selected_constituency}, {selected_state}"
    
    with st.spinner(f"Analyzing news for {search_query}..."):
        news = fetch_last_7_days_news(search_query)
        
        if news:
            profile = analyze_news_sentiments(news)
            score = calculate_match_score(user_priorities, profile)
            
            # --- NEW: Look up the politician's name! ---
            # If the city isn't in our list yet, it just says "Local Representative"
            politician_name = CANDIDATE_MAP.get(selected_constituency, "Local Representative")
            
            # Now it prints the name AND the city!
            st.metric(label=f"Match Score for {politician_name} ({selected_constituency})", value=f"{score}%")
            st.progress(score / 100)
        else:
            st.error("No recent news found for this area. Try a different city.")