import streamlit as st
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
    
    # 1. Look up the list of names for the city we selected
    politicians = CANDIDATE_MAP.get(selected_constituency, ["Candidate A", "Candidate B"])
    
    st.write(f"### Comparing candidates in {selected_constituency}:")
    
    # 2. Go through the list one by one
    for name in politicians:
        with st.spinner(f"Reading news for {name}..."):
            
            # Fetch news specifically for this person
            news = fetch_last_7_days_news(name)
            
            if news:
                profile = analyze_news_sentiments(news)
                score = calculate_match_score(user_priorities, profile)
            else:
                # If they are not in the news this week, give them a backup score of 35
                score = 35 
                
            # 3. Put their name and their score on the screen
            st.metric(label=f"{name}", value=f"{score}% Match")
            st.progress(score / 100)
            st.divider() # Draw a line under them so it looks neat