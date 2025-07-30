from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

# Data file paths
DEALS_FILE = 'documentation/sample_deals.json'
USERS_FILE = 'documentation/sample_users.json'
SUBSCRIPTIONS_FILE = 'documentation/sample_subscriptions.json'

# Create subscriptions file if it doesn't exist
if not os.path.exists(SUBSCRIPTIONS_FILE):
    with open(SUBSCRIPTIONS_FILE, 'w') as f:
        json.dump([], f)

def load_data(file_path):
    """Load JSON data from file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {} if 'deals' in file_path else []

def save_data(file_path, data):
    """Save JSON data to file"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def validate_user_id(user_id):
    """Validate user ID format"""
    if not user_id or not re.match(r'^[A-Z0-9]{4}$', user_id):
        return False
    return True

def validate_deal_id(deal_id):
    """Validate deal ID format"""
    try:
        deal_id = int(deal_id)
        return deal_id > 0
    except (ValueError, TypeError):
        return False

def get_user_by_id(user_id):
    """Get user by ID"""
    users = load_data(USERS_FILE)
    for user in users:
        if user['user_id'] == user_id:
            return user
    return None

def get_deal_by_id(deal_id):
    """Get deal by ID from all categories"""
    deals_data = load_data(DEALS_FILE)
    # Handle nested structure: {"deals": {...}}
    if isinstance(deals_data, dict) and 'deals' in deals_data:
        deals = deals_data['deals']
    else:
        deals = deals_data
    
    for category, category_deals in deals.items():
        for deal in category_deals:
            if deal.get('deal_id') == deal_id:
                return deal
    return None

def get_user_subscriptions(user_id):
    """Get user's subscribed deals"""
    subscriptions = load_data(SUBSCRIPTIONS_FILE)
    for sub in subscriptions:
        if sub['user_id'] == user_id:
            return sub.get('subscribed_deals', '').split(',') if sub.get('subscribed_deals') else []
    return []

def is_deal_subscribed(user_id, deal_id):
    """Check if user has subscribed to a deal"""
    subscribed_deals = get_user_subscriptions(user_id)
    return str(deal_id) in subscribed_deals

def calculate_total_savings(subscribed_deals):
    """Calculate total savings from subscribed deals"""
    total = 0
    for deal in subscribed_deals:
        amount_str = deal.get('amount_saved', '$0')
        amount = int(amount_str.replace('$', ''))
        total += amount
    return f"${total}"

def filter_deals_by_preferences(deals, user_preferences, user_location, user_pincode):
    """Filter deals based on user preferences and location"""
    filtered_deals = []
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Handle nested structure: {"deals": {...}}
    if isinstance(deals, dict) and 'deals' in deals:
        deals = deals['deals']
    
    for category, category_deals in deals.items():
        if user_preferences.get(category, False):
            for deal in category_deals:
                # Check if deal is valid (current date between start and end)
                if deal['start_date'] <= current_date <= deal['end_date']:
                 # Check location match - more flexible matching
                    user_state = user_location.split(', ')[-1].lower()
                    deal_state = deal['location_state'].lower()
                
                # Handle common state abbreviations
                state_mapping = {
                    'ny': 'new york',
                    'ca': 'california', 
                    'fl': 'florida',
                    'il': 'illinois',
                    'co': 'colorado',
                    'tx': 'texas',
                    'az': 'arizona',
                    'wa': 'washington',
                    'pa': 'pennsylvania',
                    'oh': 'ohio'
                }
                
                # Check if user state matches deal state (including abbreviations)
                state_match = (deal_state == user_state or 
                             deal_state == state_mapping.get(user_state, user_state) or
                             user_state == state_mapping.get(deal_state, deal_state))
                
                if state_match and deal['location_pincode'] == user_pincode:
                    filtered_deals.append(deal)
    
    return filtered_deals

def filter_deals_by_search(deals, location_state=None, location_pincode=None, category=None):
    """Filter deals based on search criteria"""
    filtered_deals = []
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Handle nested structure: {"deals": {...}}
    if isinstance(deals, dict) and 'deals' in deals:
        deals = deals['deals']
    
    for cat, category_deals in deals.items():
        if category and cat != category:
            continue
            
        for deal in category_deals:
            # Check if deal is valid
            if deal['start_date'] <= current_date <= deal['end_date']:
                # Check location filters
                location_match = True
                if location_state and deal['location_state'].lower() != location_state.lower():
                    location_match = False
                if location_pincode and deal['location_pincode'] != location_pincode:
                    location_match = False
                
                if location_match:
                    filtered_deals.append(deal)
    
    return filtered_deals

@app.route('/api/v1/preferences', methods=['GET'])
def get_user_preferences():
    """Get user preferences"""
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID is required'
        }), 400
    
    user_id = data['user_id']
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found',
            'error_code': 'USER_NOT_FOUND'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'User preferences retrieved successfully',
        'data': user['user_preferences']
    })

@app.route('/api/v1/preferences', methods=['PUT'])
def update_user_preferences():
    """Update user preferences"""
    data = request.get_json()
    if not data or 'user_id' not in data or 'preferences' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID and preferences are required'
        }), 400
    
    user_id = data['user_id']
    preferences = data['preferences']
    
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    # Validate preferences format
    required_categories = ['travel', 'entertainment', 'health', 'events', 'financial', 'fashion', 'automotive']
    if not all(cat in preferences for cat in required_categories):
        return jsonify({
            'status': 'error',
            'message': 'Invalid preference format',
            'error_code': 'INVALID_PREFERENCES'
        }), 400
    
    if not all(isinstance(preferences[cat], bool) for cat in required_categories):
        return jsonify({
            'status': 'error',
            'message': 'Invalid preference format',
            'error_code': 'INVALID_PREFERENCES'
        }), 400
    
    users = load_data(USERS_FILE)
    user_found = False
    
    for user in users:
        if user['user_id'] == user_id:
            user['user_preferences'] = preferences
            user_found = True
            break
    
    if not user_found:
        return jsonify({
            'status': 'error',
            'message': 'User not found',
            'error_code': 'USER_NOT_FOUND'
        }), 404
    
    save_data(USERS_FILE, users)
    
    return jsonify({
        'status': 'success',
        'message': 'User preferences updated successfully',
        'data': preferences
    })

@app.route('/api/v1/deals/recommended', methods=['GET'])
def get_recommended_deals():
    """Get recommended deals based on user preferences"""
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID is required'
        }), 400
    
    user_id = data['user_id']
    location_state = data.get('location_state')
    location_pincode = data.get('location_pincode')
    
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found',
            'error_code': 'USER_NOT_FOUND'
        }), 404
    
    deals = load_data(DEALS_FILE)
    subscribed_deals = get_user_subscriptions(user_id)
    
    # Filter deals based on search criteria or user preferences
    if location_state or location_pincode:
        filtered_deals = filter_deals_by_search(deals, location_state, location_pincode)
    else:
        filtered_deals = filter_deals_by_preferences(
            deals, 
            user['user_preferences'], 
            user['user_location'], 
            user['user_pincode']
        )
    
    # Remove already subscribed deals
    filtered_deals = [deal for deal in filtered_deals if str(deal['deal_id']) not in subscribed_deals]
    
    if not filtered_deals:
        return jsonify({
            'status': 'error',
            'message': 'No deals found for user preferences',
            'error_code': 'NO_DEALS_FOUND'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'Deals retrieved successfully',
        'data': filtered_deals,
        'total_count': len(filtered_deals)
    })

@app.route('/api/v1/deals/search', methods=['GET'])
def search_deals():
    """Search deals by location, pincode, and/or category"""
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID is required'
        }), 400
    
    user_id = data['user_id']
    location_state = data.get('location_state')
    location_pincode = data.get('location_pincode')
    category = data.get('category')
    
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    # Validate search parameters
    if location_pincode and not re.match(r'^[0-9]{5}$', location_pincode):
        return jsonify({
            'status': 'error',
            'message': 'Invalid search parameters',
            'error_code': 'INVALID_SEARCH_PARAMS'
        }), 400
    
    if category and category not in ['travel', 'entertainment', 'health', 'events', 'financial', 'fashion', 'automotive']:
        return jsonify({
            'status': 'error',
            'message': 'Invalid search parameters',
            'error_code': 'INVALID_SEARCH_PARAMS'
        }), 400
    
    deals = load_data(DEALS_FILE)
    subscribed_deals = get_user_subscriptions(user_id)
    
    filtered_deals = filter_deals_by_search(deals, location_state, location_pincode, category)
    
    # Remove already subscribed deals
    filtered_deals = [deal for deal in filtered_deals if str(deal['deal_id']) not in subscribed_deals]
    
    return jsonify({
        'status': 'success',
        'message': 'Search results retrieved successfully',
        'data': filtered_deals,
        'total_count': len(filtered_deals)
    })

@app.route('/api/v1/deals/subscribe', methods=['POST'])
def subscribe_to_deal():
    """Subscribe to a deal"""
    data = request.get_json()
    if not data or 'user_id' not in data or 'deal_id' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID and deal ID are required'
        }), 400
    
    user_id = data['user_id']
    deal_id = data['deal_id']
    
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    if not validate_deal_id(deal_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid deal ID format',
            'error_code': 'INVALID_DEAL_ID'
        }), 400
    
    # Check if user exists
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found',
            'error_code': 'USER_NOT_FOUND'
        }), 404
    
    # Check if deal exists
    deal = get_deal_by_id(deal_id)
    if not deal:
        return jsonify({
            'status': 'error',
            'message': 'Deal not found',
            'error_code': 'DEAL_NOT_FOUND'
        }), 404
    
    # Check if already subscribed
    if is_deal_subscribed(user_id, deal_id):
        return jsonify({
            'status': 'error',
            'message': 'Deal already subscribed',
            'error_code': 'DEAL_ALREADY_SUBSCRIBED'
        }), 409
    
    # Add to subscriptions
    subscriptions = load_data(SUBSCRIPTIONS_FILE)
    user_subscription = None
    
    for sub in subscriptions:
        if sub['user_id'] == user_id:
            user_subscription = sub
            break
    
    if user_subscription:
        current_deals = user_subscription.get('subscribed_deals', '')
        if current_deals:
            user_subscription['subscribed_deals'] = f"{current_deals},{deal_id}"
        else:
            user_subscription['subscribed_deals'] = str(deal_id)
    else:
        subscriptions.append({
            'user_id': user_id,
            'subscribed_deals': str(deal_id)
        })
    
    save_data(SUBSCRIPTIONS_FILE, subscriptions)
    
    return jsonify({
        'status': 'success',
        'message': 'Successfully subscribed to deal',
        'data': deal
    }), 201

@app.route('/api/v1/deals/subscribe', methods=['DELETE'])
def unsubscribe_from_deal():
    """Unsubscribe from a deal"""
    data = request.get_json()
    if not data or 'user_id' not in data or 'deal_id' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID and deal ID are required'
        }), 400
    
    user_id = data['user_id']
    deal_id = data['deal_id']
    
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    if not validate_deal_id(deal_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid deal ID format',
            'error_code': 'INVALID_DEAL_ID'
        }), 400
    
    # Check if deal exists
    deal = get_deal_by_id(deal_id)
    if not deal:
        return jsonify({
            'status': 'error',
            'message': 'Deal not found',
            'error_code': 'DEAL_NOT_FOUND'
        }), 404
    
    # Check if subscribed
    if not is_deal_subscribed(user_id, deal_id):
        return jsonify({
            'status': 'error',
            'message': 'Deal not found in subscriptions',
            'error_code': 'DEAL_NOT_SUBSCRIBED'
        }), 404
    
    # Remove from subscriptions
    subscriptions = load_data(SUBSCRIPTIONS_FILE)
    
    for sub in subscriptions:
        if sub['user_id'] == user_id:
            current_deals = sub.get('subscribed_deals', '').split(',')
            if str(deal_id) in current_deals:
                current_deals.remove(str(deal_id))
                sub['subscribed_deals'] = ','.join(current_deals)
                break
    
    save_data(SUBSCRIPTIONS_FILE, subscriptions)
    
    return jsonify({
        'status': 'success',
        'message': 'Successfully unsubscribed from deal',
        'data': deal
    })

@app.route('/api/v1/deals/subscribed', methods=['GET'])
def get_subscribed_deals():
    """Get user's subscribed deals"""
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({
            'status': 'error',
            'message': 'User ID is required'
        }), 400
    
    user_id = data['user_id']
    
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    subscribed_deal_ids = get_user_subscriptions(user_id)
    
    if not subscribed_deal_ids:
        return jsonify({
            'status': 'error',
            'message': 'No subscribed deals found',
            'error_code': 'NO_SUBSCRIPTIONS'
        }), 404
    
    # Get full deal details
    subscribed_deals = []
    for deal_id in subscribed_deal_ids:
        deal = get_deal_by_id(int(deal_id))
        if deal:
            subscribed_deals.append(deal)
    
    total_savings = calculate_total_savings(subscribed_deals)
    
    return jsonify({
        'status': 'success',
        'message': 'Subscribed deals retrieved successfully',
        'data': {
            'subscribed_deals': subscribed_deals,
            'total_savings': total_savings,
            'deal_count': len(subscribed_deals)
        }
    })

@app.route('/api/v1/deals/category/<category>', methods=['GET'])
def get_deals_by_category(category):
    """Get all deals for a specific category"""
    if category not in ['travel', 'entertainment', 'health', 'events', 'financial', 'fashion', 'automotive']:
        return jsonify({
            'status': 'error',
            'message': 'Invalid category',
            'error_code': 'INVALID_CATEGORY'
        }), 400
    
    deals_data = load_data(DEALS_FILE)
    # Handle nested structure: {"deals": {...}}
    if isinstance(deals_data, dict) and 'deals' in deals_data:
        deals = deals_data['deals']
    else:
        deals = deals_data
    
    category_deals = deals.get(category, [])
    
    # Filter by current date
    current_date = datetime.now().strftime('%Y-%m-%d')
    valid_deals = [
        deal for deal in category_deals 
        if deal['start_date'] <= current_date <= deal['end_date']
    ]
    
    return jsonify({
        'status': 'success',
        'message': f'{category.capitalize()} deals retrieved successfully',
        'data': valid_deals,
        'total_count': len(valid_deals)
    })

@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    """Get user profile"""
    if not validate_user_id(user_id):
        return jsonify({
            'status': 'error',
            'message': 'Invalid user ID format',
            'error_code': 'INVALID_USER_ID'
        }), 400
    
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found',
            'error_code': 'USER_NOT_FOUND'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'User profile retrieved successfully',
        'data': user
    })

@app.route('/api/v1/categories', methods=['GET'])
def get_categories():
    """Get all available categories"""
    categories = ['travel', 'entertainment', 'health', 'events', 'financial', 'fashion', 'automotive']
    
    return jsonify({
        'status': 'success',
        'message': 'Categories retrieved successfully',
        'data': categories,
        'total_count': len(categories)
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found',
        'error_code': 'ENDPOINT_NOT_FOUND'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'error_code': 'INTERNAL_ERROR'
    }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000) 