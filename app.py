import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Tech News 2026", page_icon="🔭", layout="centered")

# --- 2. PREMIUM CSS (High Contrast & Minimalist) ---
st.markdown("""
    <style>
    /* Dark Mode Base */
    .stApp {
        background-color: #050505;
        color: #E0E0E0;
    }

    /* Modern Centered Search Bar */
    .stTextInput>div>div>input {
        background-color: #111111;
        color: #00FFCC;
        border: 1px solid #333333;
        border-radius: 50px;
        padding: 20px 25px;
        font-size: 18px;
        text-align: center;
        transition: 0.4s;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00FFCC;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
    }

    /* High-Class News Cards */
    .news-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        transition: all 0.3s ease;
    }
    .news-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border-color: #00FFCC;
        transform: translateY(-5px);
    }

    .source-tag {
        color: #00FFCC;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .recommend-btn {
        background-color: transparent;
        color: #00FFCC;
        border: 1px solid #00FFCC;
        border-radius: 20px;
        padding: 5px 15px;
        font-size: 12px;
        cursor: pointer;
    }

    /* Hide Sidebar & Menus for Cleanliness */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC ---
@st.cache_data
def load_data():
    df = pd.read_csv('news_data.csv')
    df['Summary'] = df['Summary'].fillna('')
    df['combined'] = df['Title'] + " " + df['Summary']
    return df

df = load_data()
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['combined'])
sim = cosine_similarity(matrix, matrix)

# --- 4. TOP UI ---
st.markdown("<h1 style='text-align: center; font-size: 50px; letter-spacing: -2px;'>Tech News <span style='color: #00FFCC;'>2026</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.5; margin-bottom: 40px;'>Curated Intelligence for the Next Frontier</p>", unsafe_allow_html=True)

# Centered Search
query = st.text_input("", placeholder="Search for news, gadgets, or trends...")

# --- 5. RESULTS ---
if query:
    filtered = df[df['Title'].str.contains(query, case=False, na=False)]
    
    if not filtered.empty:
        # We use a selectbox but style it as a clean list
        selection = st.selectbox("I found these relevant stories. Which one interests you?", filtered['Title'].values)
        
        # Display the Main Story
        main_story = df[df['Title'] == selection].iloc[0]
        st.markdown(f"""
            <div class='news-card'>
                <span class='source-tag'>{main_story['Source']}</span>
                <h2 style='margin: 10px 0;'>{main_story['Title']}</h2>
                <p style='font-size: 16px; line-height: 1.6;'>{main_story['Summary']}</p>
                <a href="{main_story['Link']}" target="_blank" style="color:#00FFCC; text-decoration:none; font-weight:bold;">READ FULL STORY →</a>
            </div>
        """, unsafe_allow_html=True)

        if st.button("✨ PERSONALIZE MY FEED"):
            idx = df[df['Title'] == selection].index[0]
            scores = sorted(list(enumerate(sim[idx])), key=lambda x: x[1], reverse=True)[1:4]
            
            st.markdown("<h3 style='margin-top: 50px; opacity: 0.7;'>Similar Intelligence</h3>", unsafe_allow_html=True)
            
            for i, score in scores:
                st.markdown(f"""
                    <div class='news-card'>
                        <span class='source-tag'>{df['Source'].iloc[i]}</span>
                        <h3>{df['Title'].iloc[i]}</h3>
                        <p style='opacity: 0.7;'>{df['Summary'].iloc[i][:150]}...</p>
                        <a href="{df['Link'].iloc[i]}" target="_blank" style="color:#00FFCC; text-decoration:none;">OPEN STORY</a>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.write("No matching signals found in the 2026 archive.")
else:
    # Display 2 Featured Cards when search is empty
    st.markdown("<h4 style='opacity: 0.4; text-align: center;'>TRENDING NOW</h4>", unsafe_allow_html=True)
    for i in range(2):
        st.markdown(f"""
            <div class='news-card'>
                <span class='source-tag'>{df['Source'].iloc[i]}</span>
                <h3>{df['Title'].iloc[i]}</h3>
                <p style='opacity: 0.7;'>{df['Summary'].iloc[i]}</p>
            </div>
        """, unsafe_allow_html=True)