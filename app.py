import streamlit as st
from constituencies import STATE_CONSTITUENCY_MAP, CANDIDATE_MAP
from database import fetch_last_7_days_news
from nlp_engine import analyze_news_sentiments
from matcher import calculate_match_score

# --- Wide Mode & Page Title ---
st.set_page_config(page_title="Policy Match Maker", page_icon="🗳️", layout="wide")

# --- THE MAGIC DESIGN UPGRADE (CSS) ---
# This block paints the background and makes the score boxes look like floating cards
st.markdown("""
<style>
    /* 1. The Solid Background Color (Deep Slate Blue) */
    .stApp {
        background-color: #0F172A; 
    }
    
    /* 2. The Font Color for all text (Crisp White) */
    h1, h2, h3, p, span, label, div {
        color: #FFFFFF !important; 
    }
    
    /* 3. Make the score boxes pop out with a bright Cyan line */
    div[data-testid="stMetric"] {
        background-color: #1E293B; /* Slightly lighter box color */
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #06B6D4; /* Bright attractive cyan line */
        box-shadow: 0 4px 6px rgba(0,0,0,0.3); /* Adds a cool shadow */
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🗳️ Constituency Candidate Matcher")
st.markdown("### *Compare politicians in your area based on your personal priorities.*")
st.divider()

# --- SIDEBAR (Sliders) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1533/1533506.png", width=100)
st.sidebar.header("⚙️ Set Your Priorities")
tech = st.sidebar.slider("💻 Technology", 0, 100, 50)
health = st.sidebar.slider("🏥 Healthcare", 0, 100, 50)
econ = st.sidebar.slider("💰 Economy", 0, 100, 50)
user_priorities = {"Technology": tech, "Healthcare": health, "Economy": econ}

# --- MAIN SCREEN (Dropdowns) ---
st.subheader("📍 Select Your Location")

col1, col2 = st.columns(2)

with col1:
    selected_state = st.selectbox("1. Select State:", options=list(STATE_CONSTITUENCY_MAP.keys()))

with col2:
    constituencies_in_state = STATE_CONSTITUENCY_MAP[selected_state]
    selected_constituency = st.selectbox("2. Select Constituency:", options=constituencies_in_state)

st.write("") 

# --- RUN BUTTON ---
if st.button("🚀 Run AI Analysis", type="primary"):
    
    politicians = CANDIDATE_MAP.get(selected_constituency, ["Candidate A", "Candidate B"])
    
    st.success(f"Comparing candidates in {selected_constituency}...")
    st.divider()
    
    result_cols = st.columns(len(politicians))
    
    for index, name in enumerate(politicians):
        with result_cols[index]: 
            with st.spinner(f"Reading news for {name}..."):
                
                news = fetch_last_7_days_news(name)
                
                if news:
                    profile = analyze_news_sentiments(news)
                    score = calculate_match_score(user_priorities, profile)
                else:
                    score = 35 
                    
                st.metric(label=f"👤 {name}", value=f"{score}% Match")
                st.progress(score / 100)