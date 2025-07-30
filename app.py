import streamlit as st
import json
import os
import requests
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
        color: white !important;
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
    
    /* Deal card styling */
    .deal-card {
        background: white;
        border-radius: 12px;
        padding: 16px;
        margin: 8px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #e5e7eb;
    }
    
    .deal-title {
        font-size: 16px;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 8px;
    }
    
    .deal-description {
        font-size: 14px;
        color: #374151;
        margin-bottom: 8px;
        line-height: 1.4;
    }
    
    .deal-details {
        font-size: 12px;
        color: #6b7280;
        margin-bottom: 4px;
    }
    
    .deal-savings {
        font-size: 16px;
        font-weight: 700;
        color: #16a34a;
        margin-top: 8px;
    }
    
    .deal-code {
        background: #f3f4f6;
        color: #1f2937;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-top: 8px;
    }
    
    /* Pagination styling */
    .pagination {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin: 20px 0;
    }
    
    .pagination button {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .pagination button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .pagination button:disabled {
        background: #e5e7eb;
        color: #9ca3af;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }
    
    .page-info {
        font-size: 14px;
        color: #1f2937;
        font-weight: 500;
    }
    
    /* Back button styling */
    .back-button {
        background: #f3f4f6;
        color: #1f2937;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        margin-bottom: 15px;
    }
    
    .back-button:hover {
        background: #e5e7eb;
        color: #1f2937;
    }
    
    /* Force dark text for all non-button elements */
    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: #1f2937 !important;
    }
    
    /* Only button text should be white */
    .stButton > button {
        color: white !important;
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
    """Load user data from sample_users.json file"""
    try:
        with open('data/sample_users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("User data file not found!")
        return []

def load_deals_data():
    """Load deals data from sample_deals.json file"""
    try:
        with open('data/sample_deals.json', 'r') as file:
            data = json.load(file)
            return data.get('deals', {})
    except FileNotFoundError:
        st.error("Deals data file not found!")
        return {}

def load_subscriptions_data():
    """Load subscriptions data from sample_subscriptions.json file"""
    try:
        with open('data/sample_subscriptions.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Subscriptions data file not found!")
        return []

def authenticate_user(user_id, users):
    """Authenticate user by user_id"""
    for user in users:
        if user['user_id'] == user_id:
            return user
    return None

def get_user_subscriptions(user_id, subscriptions_data):
    """Get subscribed deals for a specific user"""
    for subscription in subscriptions_data:
        if subscription['user_id'] == user_id:
            return subscription['subscribed_deals'].split(',')
    return []

def subscribe_to_deal(deal_id):
    """Subscribe user to a deal by making POST call to backend"""
    try:
        import requests
        
        # Get current user
        user = st.session_state.get('user')
        if not user:
            st.error("User not logged in!")
            return
        
        # Prepare the subscription data
        subscription_data = {
            "user_id": user['user_id'],
            "deal_id": deal_id
        }
        
        # Make POST request to backend API
        # You can update this URL to match your backend endpoint
        api_url = "http://localhost:8000/subscribe"  # Update this to your actual backend URL
        
        response = requests.post(
            api_url,
            json=subscription_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            st.success(f"Successfully subscribed to deal {deal_id}!")
            # Optionally refresh the page or update local state
            st.rerun()
        elif response.status_code == 409:
            st.warning("You are already subscribed to this deal!")
        else:
            st.error(f"Failed to subscribe: {response.status_code} - {response.text}")
            
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {str(e)}")
    except Exception as e:
        st.error(f"Error subscribing to deal: {str(e)}")

def is_user_subscribed_to_deal(user_id, deal_id, subscriptions_data):
    """Check if user is already subscribed to a specific deal"""
    user_subscriptions = get_user_subscriptions(user_id, subscriptions_data)
    return str(deal_id) in user_subscriptions

def filter_deals_by_location(deals_data, location=None, pincode=None):
    """Filter deals by location and/or pincode"""
    matching_deals = []
    
    for category, category_deals in deals_data.items():
        for deal in category_deals:
            match_location = False
            match_pincode = False
            
            # Check location match
            if location and location.lower() in deal.get('location_state', '').lower():
                match_location = True
            # Check pincode match
            if pincode and pincode in deal.get('location_pincode', ''):
                match_pincode = True
            
            # If both location and pincode are provided, both must match
            if location and pincode:
                if match_location and match_pincode:
                    matching_deals.append(deal)
            # If only location is provided
            elif location and not pincode:
                if match_location:
                    matching_deals.append(deal)
            # If only pincode is provided
            elif pincode and not location:
                if match_pincode:
                    matching_deals.append(deal)
    
    return matching_deals

def display_deals_page(deals, page, deals_per_page=5):
    """Display deals for a specific page in single row cards"""
    start_idx = page * deals_per_page
    end_idx = start_idx + deals_per_page
    page_deals = deals[start_idx:end_idx]
    
    # Get user subscription status
    user = st.session_state.get('user')
    subscriptions_data = load_subscriptions_data()
    user_subscriptions = get_user_subscriptions(user['user_id'], subscriptions_data) if user else []
    
    for i, deal in enumerate(page_deals):
        # Extract deal code from description and clean description
        deal_code = deal['description'].split('Use code ')[-1].split(' ')[0] if 'Use code ' in deal['description'] else 'N/A'
        clean_description = deal['description'].split('Use code ')[0].strip() if 'Use code ' in deal['description'] else deal['description']
        
        # Check if user is already subscribed to this deal
        is_subscribed = str(deal['deal_id']) in user_subscriptions
        
        # Create two-column layout: deal info + subscribe button
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            <div style="background: white; padding: 8px 12px; border-radius: 8px; margin: 4px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1); width: 100%;">
                <div style="display: flex; flex-direction: column; width: 100%;">
                    <div style="font-weight: 600; color: #1f2937; font-size: 11px; margin-bottom: 2px; line-height: 1.2;">{clean_description[:70]}{'...' if len(clean_description) > 70 else ''}</div>
                    <div style="color: #6b7280; font-size: 10px; margin-bottom: 4px;">{deal.get('location_state', 'N/A')} • {deal['category'].title()}</div>
                    <div style="background: #f0fdf4; padding: 4px 8px; border-radius: 4px; border: 1px solid #bbf7d0; text-align: center; display: inline-block; width: fit-content;">
                        <div style="font-weight: 700; color: #16a34a; font-size: 10px;">{deal['amount_saved']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Tick mark as subscribe button
            if is_subscribed:
                # Show subscribed state (non-clickable)
                st.markdown(f"""
                <div style="background: #dcfce7; padding: 4px 8px; border-radius: 4px; border: 1px solid #22c55e; text-align: center; min-width: 35px; margin: 4px 0;">
                    <div style="font-weight: 600; color: #16a34a; font-size: 12px;">✓</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Tick mark as subscribe button
                if st.button("✓", key=f"subscribe_{deal['deal_id']}_{page}_{i}", help="Subscribe to this deal"):
                    subscribe_to_deal(deal['deal_id'])

def display_pagination_controls(deals, current_page, deals_per_page=5, page_key_prefix=""):
    """Display pagination controls as footer"""
    total_pages = (len(deals) + deals_per_page - 1) // deals_per_page
    
    if total_pages > 1:
        st.markdown("""
        <div style="background: white; padding: 8px 16px; border: 1px solid #e5e7eb; margin-top: 16px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <button id="prev-btn" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; border: none; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;" """ + f"""onclick="changePage({current_page - 1}, '{page_key_prefix}')" """ + f"""{"disabled" if current_page == 0 else ""}">← Previous</button>
                <span style="font-size: 11px; color: #1f2937; font-weight: 500;">Page {current_page + 1} of {total_pages}</span>
                <button id="next-btn" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; border: none; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;" """ + f"""onclick="changePage({current_page + 1}, '{page_key_prefix}')" """ + f"""{"disabled" if current_page >= total_pages - 1 else ""}">Next →</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add JavaScript for pagination
        st.markdown(f"""
        <script>
        function changePage(newPage, prefix) {{
            // This would typically trigger a Streamlit rerun with the new page
            console.log('Changing to page:', newPage, 'for prefix:', prefix);
            // For now, we'll use a simple approach - you can enhance this with AJAX
            window.location.href = window.location.href + '&page=' + newPage + '&prefix=' + prefix;
        }}
        </script>
        """, unsafe_allow_html=True)

def get_personalized_deals(user, deals_data, subscriptions_data):
    """Get personalized deals based on user preferences and subscriptions"""
    personalized_deals = []
    user_preferences = user.get('user_preferences', {})
    user_subscriptions = get_user_subscriptions(user['user_id'], subscriptions_data)
    
    for category, category_deals in deals_data.items():
        # Check if user has preference for this category
        if user_preferences.get(category, False):
            for deal in category_deals:
                # Check if user is already subscribed to this deal
                if str(deal['deal_id']) not in user_subscriptions:
                    personalized_deals.append(deal)
    
    return personalized_deals

def location_deals_page():
    """Display location-based deals page"""
    deals_data = load_deals_data()
    
    # Initialize session state for location deals
    if 'location_deals_state' not in st.session_state:
        st.session_state.location_deals_state = 'input'  # 'input' or 'results'
        st.session_state.location_deals = []
        st.session_state.current_page = 0
    
    # Back button and pagination controls as small icons
    deals = st.session_state.location_deals
    current_page = st.session_state.current_page
    total_pages = (len(deals) + 5 - 1) // 5 if deals else 0
    
    # Create a container for the navigation controls
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        
        with col1:
            if st.button("←", key="back_location", help="Back to main page"):
                st.session_state.selected_action = None
                st.session_state.current_page = 0
                # Clear cached location deals data
                if 'location_deals' in st.session_state:
                    del st.session_state.location_deals
                if 'location_deals_state' in st.session_state:
                    del st.session_state.location_deals_state
                st.rerun()
        
        with col2:
            if total_pages > 1 and current_page > 0:
                if st.button("‹", key="prev_location", help="Previous page"):
                    st.session_state.current_page = current_page - 1
                    st.rerun()
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        with col3:
            if total_pages > 1:
                st.markdown(f"<div style='text-align: center; font-size: 11px; color: #6b7280; font-weight: 500; padding-top: 4px;'>{current_page + 1}/{total_pages}</div>", unsafe_allow_html=True)
        
        with col4:
            if total_pages > 1 and current_page < total_pages - 1:
                if st.button("›", key="next_location", help="Next page"):
                    st.session_state.current_page = current_page + 1
                    st.rerun()
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        with col5:
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Add spacing for fixed chat
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    
    if st.session_state.location_deals_state == 'input':
        # Location input form
        st.markdown("#### 📍 Find Deals by Location")
        st.markdown("<span style='font-size: 10px; color: #6b7280;'>Enter location (state) and/or pincode to find deals near you.</span>", unsafe_allow_html=True)
        
        # Use Streamlit's text_input for visible text color
        location = st.text_input("Location (State)", placeholder="e.g., California, New York", key="location_input")
        pincode = st.text_input("Pincode", placeholder="e.g., 90210", key="pincode_input")
        
        # Search button with magnifying glass icon - right aligned
        col1, col2, col3 = st.columns([2, 1, 1])
        with col3:
            if st.button("🔍", key="search_deals", use_container_width=False):
                if not location and not pincode:
                    st.error("Please enter either location or pincode (or both).")
                else:
                    matching_deals = filter_deals_by_location(deals_data, location, pincode)
                    st.session_state.location_deals = matching_deals
                    st.session_state.current_page = 0
                    st.session_state.location_deals_state = 'results'
                    st.rerun()
    
    elif st.session_state.location_deals_state == 'results':
        # Display results
        deals = st.session_state.location_deals
        current_page = st.session_state.current_page
        deals_per_page = 5
        
        if not deals:
            st.warning("No deals found for the specified location/pincode.")
            if st.button("Try Different Search", key="try_again"):
                st.session_state.location_deals_state = 'input'
                st.rerun()
        else:
            # Use visible color for found deals text
            st.markdown(f"<span style='font-size:14px; color:#1f2937; font-weight:600; margin: 8px 0; display: block;'>📍 Found {len(deals)} Deals</span>", unsafe_allow_html=True)
            
            # Display deals for current page
            display_deals_page(deals, current_page, deals_per_page)
            


def category_deals_page():
    """Display category-based deals page"""
    deals_data = load_deals_data()
    
    # Initialize session state for category deals
    if 'category_deals_state' not in st.session_state:
        st.session_state.category_deals_state = 'select'  # 'select' or 'results'
        st.session_state.selected_category = None
        st.session_state.category_deals = []
        st.session_state.current_page = 0
    
    # Back button and pagination controls as small icons
    deals = st.session_state.category_deals
    current_page = st.session_state.current_page
    total_pages = (len(deals) + 5 - 1) // 5 if deals else 0
    
    # Create a container for the navigation controls
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        
        with col1:
            if st.button("←", key="back_category", help="Back to main page"):
                st.session_state.selected_action = None
                st.session_state.current_page = 0
                # Clear cached category deals data
                if 'category_deals' in st.session_state:
                    del st.session_state.category_deals
                if 'category_deals_state' in st.session_state:
                    del st.session_state.category_deals_state
                if 'selected_category' in st.session_state:
                    del st.session_state.selected_category
                st.rerun()
        
        with col2:
            if total_pages > 1 and current_page > 0:
                if st.button("‹", key="prev_category", help="Previous page"):
                    st.session_state.current_page = current_page - 1
                    st.rerun()
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        with col3:
            if total_pages > 1:
                st.markdown(f"<div style='text-align: center; font-size: 11px; color: #6b7280; font-weight: 500; padding-top: 4px;'>{current_page + 1}/{total_pages}</div>", unsafe_allow_html=True)
        
        with col4:
            if total_pages > 1 and current_page < total_pages - 1:
                if st.button("›", key="next_category", help="Next page"):
                    st.session_state.current_page = current_page + 1
                    st.rerun()
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        with col5:
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Add spacing for fixed chat
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    
    if st.session_state.category_deals_state == 'select':
        # Category selection
        st.markdown("### 🎯 Browse Deals by Category")
        st.markdown("Select a category to view available deals.")
        
        categories = list(deals_data.keys())
        selected_category = st.selectbox("Choose Category", categories, key="category_select")
        
        if st.button("🔍 View Deals", key="view_category_deals"):
            if selected_category:
                category_deals = deals_data.get(selected_category, [])
                st.session_state.selected_category = selected_category
                st.session_state.category_deals = category_deals
                st.session_state.current_page = 0
                st.session_state.category_deals_state = 'results'
                st.rerun()
    
    elif st.session_state.category_deals_state == 'results':
        # Display results
        deals = st.session_state.category_deals
        current_page = st.session_state.current_page
        deals_per_page = 5
        category = st.session_state.selected_category
        
        if not deals:
            st.warning(f"No deals found for {category} category.")
            if st.button("Try Different Category", key="try_again_category"):
                st.session_state.category_deals_state = 'select'
                st.rerun()
        else:
            # Use visible color for found deals text
            st.markdown(f"<span style='font-size:14px; color:#1f2937; font-weight:600; margin: 8px 0; display: block;'>🎯 {category.title()} Deals ({len(deals)} found)</span>", unsafe_allow_html=True)
            
            # Display deals for current page
            display_deals_page(deals, current_page, deals_per_page)
            


def personalized_deals_page():
    """Display personalized deals based on user preferences"""
    user = st.session_state.user
    deals_data = load_deals_data()
    subscriptions_data = load_subscriptions_data()
    
    # Initialize session state for personalized deals
    if 'personalized_deals_state' not in st.session_state:
        st.session_state.personalized_deals_state = 'loading'
        st.session_state.personalized_deals = []
        st.session_state.current_page = 0
    
    # Back button and pagination controls as small icons
    deals = st.session_state.personalized_deals
    current_page = st.session_state.current_page
    total_pages = (len(deals) + 5 - 1) // 5 if deals else 0
    
    # Create a container for the navigation controls
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        
        with col1:
            if st.button("←", key="back_personalized", help="Back to main page"):
                st.session_state.selected_action = None
                st.session_state.current_page = 0
                # Clear cached personalized deals data
                if 'personalized_deals' in st.session_state:
                    del st.session_state.personalized_deals
                if 'personalized_deals_state' in st.session_state:
                    del st.session_state.personalized_deals_state
                st.rerun()
        
        with col2:
            if total_pages > 1 and current_page > 0:
                if st.button("‹", key="prev_personalized", help="Previous page"):
                    st.session_state.current_page = current_page - 1
                    st.rerun()
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        with col3:
            if total_pages > 1:
                st.markdown(f"<div style='text-align: center; font-size: 11px; color: #6b7280; font-weight: 500; padding-top: 4px;'>{current_page + 1}/{total_pages}</div>", unsafe_allow_html=True)
        
        with col4:
            if total_pages > 1 and current_page < total_pages - 1:
                if st.button("›", key="next_personalized", help="Next page"):
                    st.session_state.current_page = current_page + 1
                    st.rerun()
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        with col5:
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Add spacing for fixed chat
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    
    # Get personalized deals
    if st.session_state.personalized_deals_state == 'loading':
        personalized_deals = get_personalized_deals(user, deals_data, subscriptions_data)
        st.session_state.personalized_deals = personalized_deals
        st.session_state.personalized_deals_state = 'results'
        st.rerun()
    
    elif st.session_state.personalized_deals_state == 'results':
        deals = st.session_state.personalized_deals
        current_page = st.session_state.current_page
        deals_per_page = 5
        
        if not deals:
            st.warning("No personalized deals found based on your preferences.")
            st.info("Try updating your preferences or browse deals by category.")
            if st.button("Browse All Categories", key="browse_categories"):
                st.session_state.selected_action = "category"
                st.rerun()
        else:
            # Use visible color for found deals text
            st.markdown(f"<span style='font-size:14px; color:#1f2937; font-weight:600; margin: 8px 0; display: block;'>🎯 Personalized Deals ({len(deals)} found)</span>", unsafe_allow_html=True)
            
            # Display deals for current page
            display_deals_page(deals, current_page, deals_per_page)
            


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
    
    # Create a container for the main content area with fixed height
    with st.container():
        # Check if we're in specific action mode
        if st.session_state.get('selected_action') == 'location':
            location_deals_page()
        elif st.session_state.get('selected_action') == 'category':
            category_deals_page()
        elif st.session_state.get('selected_action') == 'personalized':
            personalized_deals_page()
        else:
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
            
            if st.button("🎯 Personalized Deals", key="personalized_btn"):
                st.session_state.selected_action = "personalized"
                st.session_state.current_page = 0
                st.rerun()
            
            if st.button("📂 Deals by Category", key="category_btn"):
                st.session_state.selected_action = "category"
                st.session_state.current_page = 0
                st.rerun()
            
            if st.button("📍 Deals by Location", key="location_btn"):
                st.session_state.selected_action = "location"
                st.session_state.current_page = 0
                st.rerun()
    
    # Fixed chat input area at bottom - always visible
    st.markdown("""
    <style>
    .fixed-chat-container {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 375px;
        background: white;
        padding: 16px 20px;
        border-top: 1px solid #e5e7eb;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        z-index: 1000;
    }
    .chat-input-row {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .chat-input-field {
        flex: 1;
        border: 1px solid #e5e7eb;
        border-radius: 20px;
        padding: 12px 16px;
        font-size: 14px;
        background: #f9fafb;
    }
    .chat-send-btn {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .chat-send-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Fixed chat input at bottom
    st.markdown("""
    <div class="fixed-chat-container">
        <div class="chat-input-row">
            <input type="text" class="chat-input-field" placeholder="Type your message here..." id="chat-input">
            <button class="chat-send-btn" onclick="sendMessage()">➤</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add bottom padding to prevent content from being hidden behind fixed chat
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    
    # JavaScript for chat functionality
    st.markdown("""
    <script>
    function sendMessage() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        if (message) {
            // Here you would typically send the message to your backend
            console.log('Sending message:', message);
            input.value = '';
            // You can add AJAX call here to send message to Streamlit
        }
    }
    
    // Allow Enter key to send message
    document.getElementById('chat-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
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
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0
    

    
    # Show appropriate page based on login status
    if not st.session_state.logged_in:
        login_page()
    else:
        chat_page()

if __name__ == "__main__":
    main()
