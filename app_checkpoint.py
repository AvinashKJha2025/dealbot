import streamlit as st
import json
import os
from pathlib import Path
from datetime import datetime

# Page configuration for mobile-like appearance
st.set_page_config(
    page_title="DealsBot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional Wells Fargo-style mobile banking app
st.markdown("""
<style>
    /* Reset and base styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .main {
        padding: 0 !important;
        max-width: 375px !important;
        margin: 0 auto !important;
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eaff 100%) !important;
        min-height: 100vh;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eaff 100%);
        min-height: 100vh;
        padding: 0 !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile container with border */
    .block-container {
        padding: 0 !important;
        max-width: 375px !important;
        margin: 0 auto !important;
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eaff 100%);
        min-height: 100vh;
        border: 2px solid #d1d5db;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        overflow: hidden;
    }
    
    /* Status bar styling */
    .status-bar {
        background: #000;
        color: white;
        padding: 8px 20px;
        font-size: 14px;
        font-weight: 600;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    /* App header styling - Professional Wells Fargo style */
    .app-header {
        background: transparent;
        padding: 25px 20px 15px;
        text-align: center;
        color: #1f2937;
    }
    
    .app-title {
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #1f2937;
        text-transform: uppercase;
        letter-spacing: 1px;
        line-height: 1.2;
        text-align: center;
    }
    
    .app-subtitle {
        font-size: 20px;
        color: #6b7280;
        font-weight: 400;
        margin-bottom: 35px;
        line-height: 1.3;
        text-align: center;
    }
    
    /* Login form styling - Professional Wells Fargo style */
    .login-form {
        background: white;
        margin: 0 20px;
        padding: 35px 25px;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
    }
    
    .form-title {
        font-size: 20px;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Input styling - Professional Wells Fargo style */
    .input-container {
        margin-bottom: 25px;
    }
    
    .input-label {
        font-size: 14px;
        font-weight: 600;
        color: #374151;
        margin-bottom: 8px;
        display: block;
        text-align: left;
    }
    
    .stTextInput > div > div > input {
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        padding: 16px 18px;
        font-size: 16px;
        background: #fafafa;
        transition: all 0.3s ease;
        box-shadow: none;
        width: 100%;
        box-sizing: border-box;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3b82f6;
        background: white;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        outline: none;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #9ca3af;
        font-weight: 400;
    }
    
    /* Button styling - Professional Wells Fargo style */
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border: none;
        padding: 18px 32px;
        font-size: 16px;
        font-weight: 700;
        width: auto;
        margin-top: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        float: right;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    /* Error message styling */
    .stAlert {
        border-radius: 10px;
        border: none;
        background: #fef2f2;
        color: #dc2626;
        padding: 14px 18px;
        margin-top: 15px;
        border-left: 4px solid #dc2626;
        font-size: 14px;
        font-weight: 500;
    }
    
    /* Success message styling */
    .success-message {
        background: #f0fdf4;
        color: #16a34a;
        padding: 14px 18px;
        border-radius: 10px;
        margin-top: 15px;
        border-left: 4px solid #16a34a;
        font-size: 14px;
        font-weight: 500;
    }
    
    /* Chat page styles */
    .chat-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 15px 20px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .welcome-message {
        background: white;
        padding: 20px;
        border-radius: 12px;
        margin: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #e5e7eb;
    }
    
    .qrb-button {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 16px 20px;
        margin: 8px 0;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .qrb-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
    
    .logout-button {
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
        padding: 8px;
        border-radius: 50%;
        transition: all 0.2s ease;
    }
    
    .logout-button:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    /* Mobile responsive */
    @media (max-width: 480px) {
        .main, .block-container {
            max-width: 100% !important;
            border-radius: 0;
            border: none;
        }
    }
</style>
""", unsafe_allow_html=True)

def get_greeting():
    """Get appropriate greeting based on current time"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning,"
    elif 12 <= hour < 17:
        return "Good afternoon,"
    elif 17 <= hour < 21:
        return "Good evening,"
    else:
        return "Good night,"

def get_current_time():
    """Get current time in HH:MM format"""
    return datetime.now().strftime("%H:%M")

def load_user_data():
    """Load user data from JSON file"""
    try:
        with open('data/user_details.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("User data file not found!")
        return []

def authenticate_user(user_id, users):
    """Authenticate user by user_id"""
    for user in users:
        if user['user_id'] == user_id:
            return user
    return None

def login_page():
    """Display login page using professional Wells Fargo style design"""
    
    # Get dynamic greeting and current time
    greeting = get_greeting()
    current_time = get_current_time()
    
    # Status bar with current time and proper icons (HTML-based)
    st.markdown(f"""
    <div style="background: #000; color: white; padding: 8px 20px; font-size: 14px; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
        <span>{current_time}</span>
        <span>📶 🔋</span>
    </div>
    """, unsafe_allow_html=True)
    
    # App header - Professional Wells Fargo style (centered)
    st.markdown("""
    <div style="text-align: center; padding: 25px 20px 15px;">
        <h1 style="font-size: 26px; font-weight: 700; margin-bottom: 8px; color: #1f2937; text-transform: uppercase; letter-spacing: 1px; line-height: 1.2;">DEALSBOT</h1>
        <p style="font-size: 20px; color: #6b7280; font-weight: 400; margin-bottom: 35px; line-height: 1.3;">""" + greeting + """</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a small vertical space
    st.markdown("<br>", unsafe_allow_html=True)
    
    # User ID label (Streamlit only, no HTML container)
    st.markdown('<span style="font-size: 14px; font-weight: 600; color: #374151;">User ID</span>', unsafe_allow_html=True)
    
    # User ID input field (Streamlit only)
    user_id = st.text_input("User ID", placeholder="Enter your User ID", key="user_id_input")
    
    # Professional Sign On button (right-aligned, smaller)
    col1, col2, col3 = st.columns([1, 1, 2])
    with col3:
        if st.button("SIGN ON", key="login_btn"):
            if user_id and user_id.strip():
                users = load_user_data()
                user = authenticate_user(user_id.strip(), users)
                if user:
                    st.session_state.user = user
                    st.session_state.logged_in = True
                    st.success("Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("Invalid User ID. Please try again.")
            else:
                st.error("Please enter a User ID.")

def chat_page():
    """Display chat page using only Streamlit components"""
    user = st.session_state.user
    
    # Get current time for status bar
    current_time = get_current_time()
    
    # Status bar with current time and proper icons
    st.markdown(f"""
    <div style="background: #000; color: white; padding: 8px 20px; font-size: 14px; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
        <span>{current_time}</span>
        <span>📶 🔋</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Header with title and logout
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("""
        <div style="max-width: 150px; background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); padding: 6px 15px; color: white; border-radius: 8px;">
            <h6 style="margin: 0; color: white; font-size: 14px;">DealsBot</h6>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("⏻", key="logout_btn", help="Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()
    
    # Welcome message - much smaller
    st.markdown(f"""
    <div style="background: white; padding: 8px 15px; border-radius: 8px; margin: 10px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border: 1px solid #e5e7eb;">
        <h5 style="margin: 0; color: #1f2937; font-size: 14px;">Welcome {user['user_name']}! 👋</h5>
        <p style="margin: 3px 0 0 0; color: #6b7280; font-size: 12px;">How can I assist you with deals today?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # QRB Buttons - Single column, vertical stack, reduced height by 20%, left-aligned
    st.markdown("""
    <style>
    .stButton > button {
        height: 48px !important;
        padding: 12px 20px !important;
        margin: 6px 0 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if st.button("🎯 Deals by Category", key="category_btn"):
        st.session_state.selected_action = "category"
        st.rerun()
    
    if st.button("🏪 Deals by Vendor", key="vendor_btn"):
        st.session_state.selected_action = "vendor"
        st.rerun()
    
    if st.button("💰 Deals by Amount", key="amount_btn"):
        st.session_state.selected_action = "amount"
        st.rerun()
    
    if st.button("📍 Deals by Location", key="location_btn"):
        st.session_state.selected_action = "location"
        st.rerun()
    
    # Chat input with integrated send button (ChatGPT style)
    st.markdown("""
    <style>
    .chatgpt-input-container {
        display: flex;
        align-items: center;
        margin: 24px 20px 16px 20px;
        padding: 0;
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 1px solid #e5e7eb;
        min-height: 80px;
        position: relative;
    }
    .chatgpt-input-box {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        padding: 20px 60px 20px 20px !important;
        font-size: 16px !important;
        flex: 1;
        min-height: 80px;
        resize: none;
        font-family: inherit;
    }
    .chatgpt-input-box:focus {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }
    .send-btn-gpt {
        position: absolute !important;
        right: 12px !important;
        bottom: 12px !important;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        width: 44px !important;
        height: 44px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 20px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        z-index: 10;
    }
    .send-btn-gpt:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4) !important;
    }
    .send-btn-gpt:active {
        transform: scale(0.95) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Single chat input area with integrated send button (ChatGPT style)
    col1, col2 = st.columns([6, 1])
    with col1:
        user_input = st.text_area("", placeholder="Type your message here...", key="chat_input", label_visibility="collapsed", height=80)
    with col2:
        if st.button("➤", key="send_btn", help="Send message"):
            if user_input and user_input.strip():
                # Handle chat input here
                st.success(f"You said: {user_input}")
                st.session_state.chat_input = ""
                st.rerun()
    
    # Add custom CSS to position send button inside text area
    st.markdown("""
    <script>
    // Position send button inside text area
    const textArea = document.querySelector('textarea[data-testid="stTextArea"]');
    const sendBtn = document.querySelector('button[data-testid="stButton"]');
    if (textArea && sendBtn) {
        textArea.style.position = 'relative';
        sendBtn.style.position = 'absolute';
        sendBtn.style.right = '12px';
        sendBtn.style.bottom = '12px';
        sendBtn.style.zIndex = '10';
    }
    </script>
    """, unsafe_allow_html=True)

def main():
    """Main application function"""
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'selected_action' not in st.session_state:
        st.session_state.selected_action = None
    
    # Show appropriate page based on login status
    if not st.session_state.logged_in:
        login_page()
    else:
        chat_page()

if __name__ == "__main__":
    main()
