import streamlit as st
# (Assuming you imported your fetcher and NLP functions here)

st.title("🎯 Live Policy Matcher")

# 1. The User Input Box
st.write("### Step 1: Who do you want to analyze?")
# We provide a default suggestion, but they can delete it and type anyone!
politician_input = st.text_input(
    "Enter politician names separated by commas:", 
    "Nitin Gadkari, Ashwini Vaishnaw, Rajnath Singh"
)

# 2. The Sliders
st.write("### Step 2: Set your priorities")
edu = st.slider("Education", 1, 10, 5)
tech = st.slider("Technology", 1, 10, 5)
# ... (other sliders)

user_needs = {"education": edu, "technology": tech} # simplified for example

# 3. The Action Button
if st.button("Analyze & Find My Match", type="primary"):
    
    # Clean up the names the user typed (removes extra spaces)
    politician_names = [name.strip() for name in politician_input.split(",")]
    
    live_candidates = []
    
    # 4. The Loading Spinner (Crucial for UX!)
    with st.spinner('Scraping the last 7 days of news... Please wait.'):
        
        for name in politician_names:
            # Go fetch the news for this specific person
            news_text = fetch_last_7_days_news(name)
            
            # Run the NLP engine on the news
            scores = get_scores_from_text(news_text)
            scores["name"] = name
            
            live_candidates.append(scores)
            
    st.success("Analysis Complete!")
    
    # ... (Run your matching math here and print the winner)