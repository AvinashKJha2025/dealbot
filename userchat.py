from flask import Flask, request, jsonify
import json
import re
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Load the JSON data files
def load_json_data():
    """Load all JSON data files from chatbotsampledata directory"""
    data = {}
    data_dir = "chatbotsampledata"
    
    try:
        # Load deals data
        with open(os.path.join(data_dir, "mock_db_users_deals.json"), "r") as f:
            data['deals'] = json.load(f)
        
        # Load user preferences
        with open(os.path.join(data_dir, "mock_db_user_pref.json"), "r") as f:
            data['user_prefs'] = json.load(f)
        
        # Load user deals
        with open(os.path.join(data_dir, "mock_db_users.json"), "r") as f:
            data['user_deals'] = json.load(f)
        
        # Load user transactions
        with open(os.path.join(data_dir, "mock_db_users_tx.json"), "r") as f:
            data['user_tx'] = json.load(f)
            
    except FileNotFoundError as e:
        print(f"Error loading data files: {e}")
        return None
    
    return data

# Initialize data
data = load_json_data()

def extract_intent_and_entities(chat_text):
    """Extract intent and entities from user chat text"""
    chat_text = chat_text.lower().strip()
    
    # Define patterns for different intents
    patterns = {
        'category_search': [
            r'show\s+(?:me\s+)?(?:deals\s+)?(?:for|related\s+to|in\s+)?\s*(\w+)',
            r'get\s+(?:me\s+)?(?:deals\s+)?(?:for|related\s+to|in\s+)?\s*(\w+)',
            r'show\s+(?:me\s+)?(\w+)\s+deals',
            r'get\s+(?:me\s+)?(\w+)\s+deals'
        ],
        'location_search': [
            r'show\s+(?:me\s+)?(?:deals\s+)?(?:from|in|available\s+in)\s+([^$]+)',
            r'get\s+(?:me\s+)?(?:deals\s+)?(?:from|in|available\s+in)\s+([^$]+)',
            r'deals\s+(?:available\s+)?(?:in|from)\s+([^$]+)'
        ],
        'merchant_search': [
            r'show\s+(?:me\s+)?(?:deals\s+)?(?:from)\s+([^$]+)',
            r'get\s+(?:me\s+)?(?:deals\s+)?(?:from)\s+([^$]+)',
            r'show\s+deals\s+from\s+([^$]+)'
        ],
        'amount_search': [
            r'show\s+(?:me\s+)?(?:deals\s+)?(?:under|below|less\s+than)\s+\$?(\d+)',
            r'get\s+(?:me\s+)?(?:deals\s+)?(?:under|below|less\s+than)\s+\$?(\d+)',
            r'deals\s+(?:under|below|less\s+than)\s+\$?(\d+)'
        ],
        'timeline_search': [
            r'show\s+(?:me\s+)?(?:deals\s+)?(?:expiring\s+)?(?:this\s+week|next\s+week)',
            r'get\s+(?:me\s+)?(?:deals\s+)?(?:expiring\s+)?(?:this\s+week|next\s+week)',
            r'show\s+(?:me\s+)?(?:deals\s+)?(?:available\s+)?(?:in|during)\s+(\w+)',
            r'get\s+(?:me\s+)?(?:deals\s+)?(?:available\s+)?(?:in|during)\s+(\w+)'
        ]
    }
    
    # Check each intent pattern
    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            match = re.search(pattern, chat_text)
            if match:
                if intent == 'timeline_search' and 'this week' in chat_text or 'next week' in chat_text:
                    return intent, {'timeframe': 'week'}
                elif intent == 'timeline_search' and match.group(1):
                    return intent, {'month': match.group(1)}
                elif intent in ['category_search', 'location_search', 'merchant_search', 'amount_search']:
                    return intent, {'value': match.group(1)}
    
    return 'unknown', {}

def search_deals_by_category(category):
    """Search deals by category"""
    category = category.lower()
    results = []
    
    for category_data in data['deals']:
        if category_data['category'].lower() == category:
            results.extend(category_data['deals'])
    
    return results

def search_deals_by_location(location):
    """Search deals by location"""
    location = location.lower()
    results = []
    
    for category_data in data['deals']:
        for deal in category_data['deals']:
            if (location in deal['deal_location_city'].lower() or 
                location in deal['deal_location_state'].lower()):
                results.append(deal)
    
    return results

def search_deals_by_merchant(merchant):
    """Search deals by merchant"""
    merchant = merchant.lower()
    results = []
    
    for category_data in data['deals']:
        for deal in category_data['deals']:
            if merchant in deal['deal_merchant'].lower():
                results.append(deal)
    
    return results

def search_deals_by_amount(amount_limit):
    """Search deals by amount limit"""
    try:
        amount_limit = float(amount_limit)
        results = []
        
        for category_data in data['deals']:
            for deal in category_data['deals']:
                # Extract numeric value from deal_saving_amount
                amount_str = deal['deal_saving_amount'].replace('$', '').replace(',', '')
                try:
                    deal_amount = float(amount_str)
                    if deal_amount <= amount_limit:
                        results.append(deal)
                except ValueError:
                    continue
        
        return results
    except ValueError:
        return []

def search_deals_by_timeline(timeframe=None, month=None):
    """Search deals by timeline"""
    results = []
    current_date = datetime.now()
    
    for category_data in data['deals']:
        for deal in category_data['deals']:
            try:
                expiry_date = datetime.strptime(deal['deal_expiry'], '%Y-%m-%d')
                
                if timeframe == 'week':
                    # Deals expiring this week
                    week_end = current_date + timedelta(days=7)
                    if current_date <= expiry_date <= week_end:
                        results.append(deal)
                
                elif month:
                    # Deals available in specific month
                    month_lower = month.lower()
                    month_mapping = {
                        'january': 1, 'february': 2, 'march': 3, 'april': 4,
                        'may': 5, 'june': 6, 'july': 7, 'august': 8,
                        'september': 9, 'october': 10, 'november': 11, 'december': 12
                    }
                    
                    if month_lower in month_mapping:
                        target_month = month_mapping[month_lower]
                        if expiry_date.month == target_month and expiry_date.year == current_date.year:
                            results.append(deal)
            
            except ValueError:
                continue
    
    return results

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint that handles deal searches"""
    try:
        request_data = request.get_json()
        
        if not request_data or 'chat_text' not in request_data:
            return jsonify({
                'error': 'Missing chat_text in request body'
            }), 400
        
        chat_text = request_data['chat_text']
        
        if not chat_text.strip():
            return jsonify({
                'error': 'Chat text cannot be empty'
            }), 400
        
        # Extract intent and entities
        intent, entities = extract_intent_and_entities(chat_text)
        
        # Process based on intent
        if intent == 'category_search':
            category = entities.get('value', '').strip()
            if category:
                results = search_deals_by_category(category)
            else:
                results = []
        
        elif intent == 'location_search':
            location = entities.get('value', '').strip()
            if location:
                results = search_deals_by_location(location)
            else:
                results = []
        
        elif intent == 'merchant_search':
            merchant = entities.get('value', '').strip()
            if merchant:
                results = search_deals_by_merchant(merchant)
            else:
                results = []
        
        elif intent == 'amount_search':
            amount = entities.get('value', '').strip()
            if amount:
                results = search_deals_by_amount(amount)
            else:
                results = []
        
        elif intent == 'timeline_search':
            timeframe = entities.get('timeframe')
            month = entities.get('month')
            results = search_deals_by_timeline(timeframe, month)
        
        else:
            # Unknown intent
            return jsonify({
                'message': 'No results available for your search. Please try different search criteria for deals.',
                'results': []
            })
        
        # Format response
        if results:
            return jsonify({
                'message': f'Found {len(results)} deals matching your search criteria.',
                'results': results
            })
        else:
            return jsonify({
                'message': 'No results available for your search. Please try different search criteria for deals.',
                'results': []
            })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Deal recommendation chatbot is running'
    })

if __name__ == '__main__':
    if data is None:
        print("Error: Could not load data files. Please ensure all JSON files exist in chatbotsampledata directory.")
        exit(1)
    
    print("Starting Deal Recommendation Chatbot...")
    print("Available search types:")
    print("- Category: 'Show me travel deals', 'Get deals for entertainment'")
    print("- Location: 'Show deals from New York', 'Deals available in California'")
    print("- Merchant: 'Show deals from Netflix', 'Get deals from Amazon'")
    print("- Amount: 'Show deals under $100', 'Get deals under $50'")
    print("- Timeline: 'Show deals expiring this week', 'Show deals available in September'")
    
    app.run(host='0.0.0.0', port=8000, debug=True)