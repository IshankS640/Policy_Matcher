import streamlit as st
from constituencies import STATE_CONSTITUENCY_MAP
from database import fetch_last_7_days_news
from nlp_engine import analyze_news_sentiments
from matcher import calculate_match_score

# --- UI Setup ---
st.set_page_config(page_title="Constituency Matcher", page_icon="📍", layout="wide")

st.title("📍 Constituency Candidate Matcher")
st.markdown("Compare candidates in your area based on your personal policy priorities.")

# --- Sidebar: User Input ---
st.sidebar.header("Your Policy Priorities")
st.sidebar.info("Rate how much you care about these sectors (1-10)")

user_priorities = {
    "Technology": st.sidebar.slider("Technology & AI", 1, 10, 5),
    "Healthcare": st.sidebar.slider("Healthcare", 1, 10, 5),
    "Economy": st.sidebar.slider("Economy & Finance", 1, 10, 5)
}

# --- Main Section: Constituency Selection ---
location = st.selectbox("Select your Constituency:", ["Kurnool", "Gurgaon", "New Delhi"])

if st.button("Run Analysis"):
    candidates = get_candidates_for_constituency(location)
    
    if candidates:
        st.subheader(f"Matching Results for {location}")
        
        # Displaying candidates side-by-side using columns
        cols = st.columns(len(candidates))
        
        for index, name in enumerate(candidates):
            with cols[index]:
                with st.spinner(f"Analyzing {name}..."):
                    # 1. Fetch live news (database.py)
                    news = fetch_last_7_days_news(name)
                    # 2. Extract policy profile (nlp_engine.py)
                    profile = analyze_news_sentiments(news)
                    # 3. Calculate Euclidean Match (matcher.py)
                    score = calculate_match_score(user_priorities, profile)
                    
                    # 4. Render Results
                    st.metric(label=name, value=f"{score}% Match")
                    st.progress(score / 100)
                    
                    with st.expander("Show Detailed Focus"):
                        st.write(f"Based on {len(news)} recent headlines.")
                        st.json(profile)
    else:
        st.warning("Data for this area is currently being updated.")