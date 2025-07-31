# Deal Recommendation Chatbot - Flask API

This is a Flask-based API that mimics Google Dialogflow to identify user intent and search for deals based on various criteria.

## Features

The chatbot supports the following types of searches:

### 1. Category-based Searches
- "Show me deals for travel"
- "Get me travel deals"
- "Show me deals related to entertainment"
- "Get deals for health"
- "Show me home deals"
- "Get me deals for food/drink"
- "Show deals for events"
- "Get me fashion deals"
- "Show me sports deals"
- "Get deals for fitness"

### 2. Location-based Searches
- "Show me deals from New York"
- "Get deals available in California"
- "Show deals from Miami"
- "Get me deals in Chicago"
- "Show deals available in Austin"

### 3. Merchant-based Searches
- "Show me deals from Netflix"
- "Get deals from Amazon"
- "Show deals from Nike"
- "Get me deals from Expedia"

### 4. Amount-based Searches
- "Show me deals under $50"
- "Get deals under $100"
- "Show deals below $30"
- "Get me deals under $75"

### 5. Timeline-based Searches
- "Show deals expiring this week"
- "Get me deals available in March"
- "Show deals available in September"

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### POST /chat
Main endpoint for chat interactions.

**Request Body:**
```json
{
    "chat_text": "Show me travel deals"
}
```

**Response:**
```json
{
    "message": "Found 10 deals matching your search criteria.",
    "results": [
        {
            "deal_id": "TRAV001",
            "deal_merchant": "Expedia",
            "deal_expiry": "2025-03-15",
            "start_date": "2025-01-20",
            "deal_code": "EXP20OFF",
            "deal_saving_amount": "$100",
            "deal_location_state": "California",
            "deal_location_city": "Los Angeles",
            "deal_zipcode": "90210",
            "png_file": "expedia.png"
        }
    ]
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
    "status": "healthy",
    "message": "Deal recommendation chatbot is running"
}
```

## Testing

Run the comprehensive test suite:

```bash
python test_app.py
```

The test script will:
- Test all search types (category, location, merchant, amount, timeline)
- Test edge cases and error handling
- Test invalid request formats
- Provide a detailed summary of test results

## Data Structure

The application uses JSON files in the `chatbotsampledata` directory:

- `mock_db_user_pref.json` - User preferences and categories
- `mock_db_users_deals.json` - Available deals organized by category
- `mock_db_users.json` - User activated deals
- `mock_db_users_tx.json` - User transaction history

## Example Usage

### Using curl:
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"chat_text": "Show me travel deals"}'
```

### Using Python requests:
```python
import requests

response = requests.post('http://localhost:5000/chat', 
                        json={'chat_text': 'Show me travel deals'})
print(response.json())
```

## Error Handling

The API handles various error scenarios:
- Missing or empty chat_text
- Invalid JSON format
- Non-existent categories/merchants/locations
- Invalid amount formats
- Server errors

All errors return appropriate HTTP status codes and error messages.

## Supported Categories

The system supports deals in the following categories:
- travel
- entertainment
- health
- home
- food/drink
- events
- fashion
- sports
- fitness

Each category contains 10 deals from different merchants across various US locations. 