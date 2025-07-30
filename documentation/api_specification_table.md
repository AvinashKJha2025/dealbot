# API Specification Table - Deal Recommender Application

## Complete API Endpoints with Request/Response Examples

| API Endpoint | Request Type | Input Payload | Output JSON |
|--------------|--------------|---------------|-------------|
| **Get User Preferences** | GET | `{"user_id": "U001"}` | `{"status": "success", "message": "User preferences retrieved successfully", "data": {"travel": true, "entertainment": true, "health": false, "events": true, "financial": false, "fashion": true, "automotive": false}}` |
| **Update User Preferences** | PUT | `{"user_id": "U001", "preferences": {"travel": true, "entertainment": false, "health": true, "events": true, "financial": false, "fashion": true, "automotive": true}}` | `{"status": "success", "message": "User preferences updated successfully", "data": {"travel": true, "entertainment": false, "health": true, "events": true, "financial": false, "fashion": true, "automotive": true}}` |
| **Get Recommended Deals** | GET | `{"user_id": "U001"}` | `{"status": "success", "message": "Deals retrieved successfully", "data": [{"deal_id": 1005, "category": "travel", "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels", "start_date": "2024-02-10", "end_date": "2024-04-30", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$120"}, {"deal_id": 2002, "category": "entertainment", "description": "Restaurant Dining - 30% discount on fine dining experiences. Use code ENTERTAIN002 at Fine Dining Group", "start_date": "2024-02-01", "end_date": "2024-05-31", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$60"}], "total_count": 2}` |
| **Get Recommended Deals (with location filter)** | GET | `{"user_id": "U001", "location_state": "New York", "location_pincode": "10001"}` | `{"status": "success", "message": "Deals retrieved successfully", "data": [{"deal_id": 1005, "category": "travel", "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels", "start_date": "2024-02-10", "end_date": "2024-04-30", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$120"}], "total_count": 1}` |
| **Search Deals** | GET | `{"user_id": "U001", "location_state": "California", "location_pincode": "90210", "category": "travel"}` | `{"status": "success", "message": "Search results retrieved successfully", "data": [{"deal_id": 1001, "category": "travel", "description": "Weekend Gateway Package - 30% off on 2-night stays at luxury resorts. Use code TRAVEL001 at Luxury Escapes", "start_date": "2024-01-15", "end_date": "2024-03-31", "location_state": "California", "location_pincode": "90210", "amount_saved": "$150"}], "total_count": 1}` |
| **Subscribe to Deal** | POST | `{"user_id": "U001", "deal_id": 1005}` | `{"status": "success", "message": "Successfully subscribed to deal", "data": {"deal_id": 1005, "category": "travel", "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels", "start_date": "2024-02-10", "end_date": "2024-04-30", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$120"}}` |
| **Unsubscribe from Deal** | DELETE | `{"user_id": "U001", "deal_id": 1005}` | `{"status": "success", "message": "Successfully unsubscribed from deal", "data": {"deal_id": 1005, "category": "travel", "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels", "start_date": "2024-02-10", "end_date": "2024-04-30", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$120"}}` |
| **Get Subscribed Deals** | GET | `{"user_id": "U001"}` | `{"status": "success", "message": "Subscribed deals retrieved successfully", "data": {"subscribed_deals": [{"deal_id": 1005, "category": "travel", "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels", "start_date": "2024-02-10", "end_date": "2024-04-30", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$120"}, {"deal_id": 2002, "category": "entertainment", "description": "Restaurant Dining - 30% discount on fine dining experiences. Use code ENTERTAIN002 at Fine Dining Group", "start_date": "2024-02-01", "end_date": "2024-05-31", "location_state": "New York", "location_pincode": "10001", "amount_saved": "$60"}], "total_savings": "$180", "deal_count": 2}}` |
| **Get Deals by Category** | GET | `GET /deals/category/travel` | `{"status": "success", "message": "Travel deals retrieved successfully", "data": [{"deal_id": 1001, "category": "travel", "description": "Weekend Gateway Package - 30% off on 2-night stays at luxury resorts. Use code TRAVEL001 at Luxury Escapes", "start_date": "2024-01-15", "end_date": "2024-03-31", "location_state": "California", "location_pincode": "90210", "amount_saved": "$150"}, {"deal_id": 1002, "category": "travel", "description": "Short Term Stay - 25% discount on vacation rentals for 3+ days. Use code TRAVEL002 at VacationRentals.com", "start_date": "2024-01-20", "end_date": "2024-04-15", "location_state": "Florida", "location_pincode": "33101", "amount_saved": "$200"}], "total_count": 2}` |
| **Get User Profile** | GET | `GET /users/U001` | `{"status": "success", "message": "User profile retrieved successfully", "data": {"user_id": "U001", "user_name": "Sarah Johnson", "user_location": "New York, NY", "user_pincode": "10001", "user_preferences": {"travel": true, "entertainment": true, "health": false, "events": true, "financial": false, "fashion": true, "automotive": false}}}` |
| **Get Available Categories** | GET | `GET /categories` | `{"status": "success", "message": "Categories retrieved successfully", "data": ["travel", "entertainment", "health", "events", "financial", "fashion", "automotive"], "total_count": 7}` |

## Error Response Examples

| Error Scenario | Input Payload | Error Response |
|----------------|---------------|----------------|
| **User Not Found** | `{"user_id": "U999"}` | `{"status": "error", "message": "User not found", "error_code": "USER_NOT_FOUND"}` |
| **Invalid User ID Format** | `{"user_id": "123"}` | `{"status": "error", "message": "Invalid user ID format", "error_code": "INVALID_USER_ID"}` |
| **Deal Not Found** | `{"user_id": "U001", "deal_id": 9999}` | `{"status": "error", "message": "Deal not found", "error_code": "DEAL_NOT_FOUND"}` |
| **Deal Already Subscribed** | `{"user_id": "U001", "deal_id": 1005}` | `{"status": "error", "message": "Deal already subscribed", "error_code": "DEAL_ALREADY_SUBSCRIBED"}` |
| **Invalid Preferences Format** | `{"user_id": "U001", "preferences": {"travel": "yes"}}` | `{"status": "error", "message": "Invalid preference format", "error_code": "INVALID_PREFERENCES"}` |
| **No Deals Found** | `{"user_id": "U001", "location_state": "Alaska"}` | `{"status": "error", "message": "No deals found for user preferences", "error_code": "NO_DEALS_FOUND"}` |
| **Invalid Search Parameters** | `{"user_id": "U001", "location_pincode": "123"}` | `{"status": "error", "message": "Invalid search parameters", "error_code": "INVALID_SEARCH_PARAMS"}` |

## Complete Request/Response Examples

### 1. Get User Preferences
**Request:**
```bash
curl -X GET http://localhost:5000/api/v1/preferences \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

**Response:**
```json
{
  "status": "success",
  "message": "User preferences retrieved successfully",
  "data": {
    "travel": true,
    "entertainment": true,
    "health": false,
    "events": true,
    "financial": false,
    "fashion": true,
    "automotive": false
  }
}
```

### 2. Update User Preferences
**Request:**
```bash
curl -X PUT http://localhost:5000/api/v1/preferences \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "U001",
    "preferences": {
      "travel": true,
      "entertainment": false,
      "health": true,
      "events": true,
      "financial": false,
      "fashion": true,
      "automotive": true
    }
  }'
```

**Response:**
```json
{
  "status": "success",
  "message": "User preferences updated successfully",
  "data": {
    "travel": true,
    "entertainment": false,
    "health": true,
    "events": true,
    "financial": false,
    "fashion": true,
    "automotive": true
  }
}
```

### 3. Get Recommended Deals
**Request:**
```bash
curl -X GET http://localhost:5000/api/v1/deals/recommended \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

**Response:**
```json
{
  "status": "success",
  "message": "Deals retrieved successfully",
  "data": [
    {
      "deal_id": 1005,
      "category": "travel",
      "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels",
      "start_date": "2024-02-10",
      "end_date": "2024-04-30",
      "location_state": "New York",
      "location_pincode": "10001",
      "amount_saved": "$120"
    },
    {
      "deal_id": 2002,
      "category": "entertainment",
      "description": "Restaurant Dining - 30% discount on fine dining experiences. Use code ENTERTAIN002 at Fine Dining Group",
      "start_date": "2024-02-01",
      "end_date": "2024-05-31",
      "location_state": "New York",
      "location_pincode": "10001",
      "amount_saved": "$60"
    }
  ],
  "total_count": 2
}
```

### 4. Search Deals
**Request:**
```bash
curl -X GET http://localhost:5000/api/v1/deals/search \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "U001",
    "location_state": "California",
    "location_pincode": "90210",
    "category": "travel"
  }'
```

**Response:**
```json
{
  "status": "success",
  "message": "Search results retrieved successfully",
  "data": [
    {
      "deal_id": 1001,
      "category": "travel",
      "description": "Weekend Gateway Package - 30% off on 2-night stays at luxury resorts. Use code TRAVEL001 at Luxury Escapes",
      "start_date": "2024-01-15",
      "end_date": "2024-03-31",
      "location_state": "California",
      "location_pincode": "90210",
      "amount_saved": "$150"
    }
  ],
  "total_count": 1
}
```

### 5. Subscribe to Deal
**Request:**
```bash
curl -X POST http://localhost:5000/api/v1/deals/subscribe \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001", "deal_id": 1005}'
```

**Response:**
```json
{
  "status": "success",
  "message": "Successfully subscribed to deal",
  "data": {
    "deal_id": 1005,
    "category": "travel",
    "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels",
    "start_date": "2024-02-10",
    "end_date": "2024-04-30",
    "location_state": "New York",
    "location_pincode": "10001",
    "amount_saved": "$120"
  }
}
```

### 6. Get Subscribed Deals
**Request:**
```bash
curl -X GET http://localhost:5000/api/v1/deals/subscribed \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

**Response:**
```json
{
  "status": "success",
  "message": "Subscribed deals retrieved successfully",
  "data": {
    "subscribed_deals": [
      {
        "deal_id": 1005,
        "category": "travel",
        "description": "City Break - 20% off on urban hotel stays in major cities. Use code TRAVEL005 at Urban Hotels",
        "start_date": "2024-02-10",
        "end_date": "2024-04-30",
        "location_state": "New York",
        "location_pincode": "10001",
        "amount_saved": "$120"
      },
      {
        "deal_id": 2002,
        "category": "entertainment",
        "description": "Restaurant Dining - 30% discount on fine dining experiences. Use code ENTERTAIN002 at Fine Dining Group",
        "start_date": "2024-02-01",
        "end_date": "2024-05-31",
        "location_state": "New York",
        "location_pincode": "10001",
        "amount_saved": "$60"
      }
    ],
    "total_savings": "$180",
    "deal_count": 2
  }
}
```

## Data Validation Rules

| Field | Format | Validation Rules |
|-------|--------|------------------|
| `user_id` | String | 4-character alphanumeric (A-Z, 0-9) |
| `deal_id` | Integer | Positive integer |
| `category` | String | Must be one of: travel, entertainment, health, events, financial, fashion, automotive |
| `start_date` | String | YYYY-MM-DD format, must be valid date |
| `end_date` | String | YYYY-MM-DD format, must be after start_date |
| `location_state` | String | Valid US state name |
| `location_pincode` | String | 5-digit format (0-9) |
| `amount_saved` | String | Must start with $ followed by positive number |
| `user_preferences` | Object | Boolean values for all 7 categories |

## HTTP Status Codes

| Status Code | Description | Usage |
|-------------|-------------|-------|
| 200 | OK | Successful GET, PUT, DELETE operations |
| 201 | Created | Successful POST operations (subscriptions) |
| 400 | Bad Request | Invalid input parameters |
| 404 | Not Found | User or deal not found |
| 409 | Conflict | Deal already subscribed |
| 500 | Internal Server Error | Server-side errors |

## Rate Limiting

| Endpoint Type | Rate Limit | Description |
|---------------|------------|-------------|
| Standard endpoints | 100 requests/minute | GET, PUT operations |
| Search endpoints | 50 requests/minute | Search operations |
| Subscription endpoints | 20 requests/minute | Subscribe/unsubscribe operations | 