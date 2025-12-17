import streamlit as st
import pandas as pd
import os
import json
import hashlib
from dotenv import load_dotenv

# --- Init & Config ---
load_dotenv()

st.set_page_config(page_title="PakAutos", page_icon="🇵🇰", layout="wide")

# --- File Paths ---
USER_DB_FILE = 'users.json'
CAR_DATA_FILE = 'cars.json'

# --- CSS Theme ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&display=swap');

    /* Main Background - Clean Light Theme */
    .stApp {
        background: #ffffff; /* Fallback */
        background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
        color: #1f1f1f;
        font-family: 'Inter', sans-serif;
    }
    
    /* Input Fields - Clean & Crisp */
    .stTextInput input, .stSelectbox select, .stNumberInput input {
        background-color: #ffffff !important;
        color: #1f1f1f !important;
        border: 1px solid #ced4da !important;
        border-radius: 8px;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
    }
    .stTextInput input:focus, .stSelectbox:focus {
        border-color: #008000 !important; /* PakAutos Green */
        box-shadow: 0 0 0 3px rgba(0, 128, 0, 0.2) !important;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(to right, #004d00, #00b300); /* Dark Green to Light Green */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
        letter-spacing: 2px;
        text-transform: uppercase;
        filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
        animation: fadeInUp 1s ease-out;
    }
    
    .hero-subtitle {
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #555555;
        margin-bottom: 40px;
        font-weight: 400;
        letter-spacing: 1px;
    }
    
    /* Headings */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        color: #004d00 !important;
    }

    /* Cards - Modern Light Card */
    .car-card {
        background: #ffffff;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 25px;
        transition: all 0.3s ease;
    }
    .car-card:hover {
        transform: translateY(-5px);
        border-color: #00b300;
        box-shadow: 0 10px 30px rgba(0, 128, 0, 0.15);
    }

    /* Primary Buttons */
    .stButton button {
        background: linear-gradient(45deg, #006400, #004d00);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 30px;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 77, 0, 0.2);
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 15px rgba(0, 77, 0, 0.3);
        background: linear-gradient(45deg, #008000, #006400);
        color: white;
    }

    /* Metrics & Sidebar */
    div[data-testid="stMetricValue"] {
        color: #006400 !important;
        font-family: 'Orbitron', sans-serif;
    }
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #e9ecef;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        background: #f1f1f1;
    }
    ::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 5px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }
</style>
""", unsafe_allow_html=True)

# --- State Management ---
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'searched' not in st.session_state:
    st.session_state.searched = False

# --- Helper Functions ---
def load_data():
    if not os.path.exists(CAR_DATA_FILE):
        return [] 
    with open(CAR_DATA_FILE, 'r') as f:
        data = json.load(f)
        for car in data:
            if 'price' in car:
                car['price'] = car['price'] * 278
        return data

CAR_DATA = load_data()

def load_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, 'r') as f:
        return json.load(f)

def save_user(username, password):
    users = load_users()
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_pw
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users, f)

def authenticate(username, password):
    users = load_users()
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    return username in users and users[username] == hashed_pw

# --- Auto-Login Check ---
def check_persistent_login():
    if not st.session_state.logged_in:
        users = load_users()
        # get_all returns a list, standard [] returns string or throws
        qp = st.query_params
        if "user" in qp:
            user_param = qp["user"]
            if user_param in users:
                st.session_state.logged_in = True
                st.session_state.username = user_param
                st.session_state.page = 'main'

check_persistent_login()

def recommend_cars(budget, condition, fuel_pref, main_usage):
    candidates = []
    for car in CAR_DATA:
        if car['price'] > budget: continue
        if condition != "Any" and car['condition'] != condition: continue
        if fuel_pref != "Any" and car['fuel'] != fuel_pref: continue
            
        score = car['usage_scores'].get(main_usage, 0)
        candidates.append({"car": car, "score": score})
    
    candidates.sort(key=lambda x: (-x['score'], x['car']['price']))
    return candidates[:3]

# --- Page Functions ---

def login_page():
    st.markdown('<p class="hero-title">LOGIN</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Welcome back to PakAutos</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Log In", use_container_width=True)
            
            if submitted:
                if authenticate(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.page = 'main'
                    st.query_params["user"] = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        st.markdown("---")
        if st.button("New here? Create Account", use_container_width=True):
            st.session_state.page = 'signup'
            st.rerun()

def signup_page():
    st.markdown('<p class="hero-title">SIGN UP</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Join the Fast Lane</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        with st.form("signup_form"):
            new_user = st.text_input("Choose a Username")
            new_pass = st.text_input("Choose a Password", type="password")
            confirm_pass = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Sign Up", use_container_width=True)
            
            if submitted:
                users = load_users()
                if new_user in users:
                    st.error("Username already exists!")
                elif new_pass != confirm_pass:
                    st.error("Passwords do not match!")
                elif len(new_pass) < 4:
                    st.error("Password must be at least 4 characters")
                else:
                    save_user(new_user, new_pass)
                    st.success("Account created! Please log in.")
                    st.session_state.page = 'login'
                    st.rerun()
        
        st.markdown("---")
        if st.button("Already have an account? Log In", use_container_width=True):
            st.session_state.page = 'login'
            st.rerun()


def main_app_page():
    # Sidebar
    with st.sidebar:
        st.title(f"Hi, {st.session_state.username}!")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.page = 'login'
            st.query_params.clear()
            st.rerun()
        st.markdown("---")
        
        # Search Filters
        st.header("Configure Search")
        usage = st.selectbox("🎯 Primary Usage", ["City", "Family", "Performance"], key='usage_select')
        budget = st.slider("💰 Max Budget (PKR)", min_value=1000000, max_value=40000000, value=12500000, step=500000, key='budget_slider')
        condition = st.radio("🆕 Condition", ["New", "Used", "Any"], horizontal=True, index=2, key='condition_radio')
        fuel = st.selectbox("⛽ Fuel Type", ["Any", "Petrol", "Diesel", "Hybrid", "Electric"], key='fuel_select')
        
        st.markdown("---")
        if st.button("🚀 Find My Ride", type="primary", use_container_width=True):
            st.session_state.searched = True

    # Hero
    st.markdown('<p class="hero-title">🌙 PakAutos</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Premium Cars. Local Prices. Smart Decisions.</p>', unsafe_allow_html=True)

    # Dashboard / Results
    if not st.session_state.searched:
        st.info("👈 **Start by setting your preferences in the sidebar.**")
        st.markdown("### 📊 Database Insights")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Cars", len(CAR_DATA))
        avg_price = sum(c['price'] for c in CAR_DATA) / len(CAR_DATA) if CAR_DATA else 0
        c2.metric("Avg Price", f"Rs. {avg_price:,.0f}")
        c3.metric("Electric Options", sum(1 for c in CAR_DATA if c['fuel'] == 'Electric'))
        c4.metric("Performance Cars", sum(1 for c in CAR_DATA if c.get('usage_scores', {}).get('Performance', 0) >= 8))
        
        if CAR_DATA:
            df_preview = pd.DataFrame(CAR_DATA)
            st.bar_chart(df_preview['make'].value_counts(), color="#00b300")
            
    else:
        results = recommend_cars(st.session_state.budget_slider, st.session_state.condition_radio, st.session_state.fuel_select, st.session_state.usage_select)
        
        st.markdown(f"### 🔍 Top Recommendations for **{st.session_state.usage_select}**")
        
        if not results:
            st.warning("😕 No matches found.")
        else:
            for idx, item in enumerate(results):
                c = item['car']
                s = item['score']
                with st.container():
                    st.markdown(f"""
                    <div class="car-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <h2 style="margin:0; color: #004d00; font-family: 'Montserrat', sans-serif;">#{idx+1} {c['make']} {c['model']}</h2>
                                <p style="color: #555; margin:0;">{c['condition']} &bull; {c['fuel']} &bull; {c['type']}</p>
                            </div>
                            <h2 style="color: #008000;">Rs. {c['price']:,}</h2>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.progress(min(s/10, 1.0), text=f"🔥 Match Score: {s}/10")
                    sc1, sc2, sc3 = st.columns(3)
                    sc1.metric("City", f"{c['usage_scores']['City']}/10")
                    sc2.metric("Family", f"{c['usage_scores']['Family']}/10")
                    sc3.metric("Performance", f"{c['usage_scores']['Performance']}/10")

# --- App Router ---
if st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'signup':
    signup_page()
elif st.session_state.page == 'main':
    if st.session_state.logged_in:
        main_app_page()
    else:
        st.session_state.page = 'login'
        st.rerun()