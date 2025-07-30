# API Documentation - Deal Recommender Application

## Base URL
```
http://localhost:5000/api/v1
```

## Authentication
All API endpoints require a valid `user_id` in the request payload. No additional authentication is required for this version.

## Response Format
All API responses follow a standard format:
```json
{
  "status": "success|error",
  "message": "Human-readable message",
  "data": {...},
  "total_count": 0
}
```

## API Endpoints

### 1. Get User Preferences

**Endpoint:** `GET /preferences`

**Description:** Retrieve user preferences for deal categories

**Request:**
```json
{
  "user_id": "U001"
}
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

**Error Response:**
```json
{
  "status": "error",
  "message": "User not found",
  "error_code": "USER_NOT_FOUND"
}
```

---

### 2. Update User Preferences

**Endpoint:** `PUT /preferences`

**Description:** Update user preferences for deal categories

**Request:**
```json
{
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
}
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

**Error Response:**
```json
{
  "status": "error",
  "message": "Invalid preference format",
  "error_code": "INVALID_PREFERENCES"
}
```

---

### 3. Get Recommended Deals

**Endpoint:** `GET /deals/recommended`

**Description:** Get personalized deal recommendations based on user preferences and location

**Request:**
```json
{
  "user_id": "U001"
}
```

**Optional Parameters:**
```json
{
  "user_id": "U001",
  "location_state": "New York",
  "location_pincode": "10001"
}
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

**Error Response:**
```json
{
  "status": "error",
  "message": "No deals found for user preferences",
  "error_code": "NO_DEALS_FOUND"
}
```

---

### 4. Search Deals

**Endpoint:** `GET /deals/search`

**Description:** Search deals by location, pincode, and/or category

**Request:**
```json
{
  "user_id": "U001",
  "location_state": "California",
  "location_pincode": "90210",
  "category": "travel"
}
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

**Error Response:**
```json
{
  "status": "error",
  "message": "Invalid search parameters",
  "error_code": "INVALID_SEARCH_PARAMS"
}
```

---

### 5. Subscribe to Deal

**Endpoint:** `POST /deals/subscribe`

**Description:** Subscribe to a specific deal

**Request:**
```json
{
  "user_id": "U001",
  "deal_id": 1005
}
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

**Error Response:**
```json
{
  "status": "error",
  "message": "Deal not found or already subscribed",
  "error_code": "DEAL_NOT_AVAILABLE"
}
```

---

### 6. Unsubscribe from Deal

**Endpoint:** `DELETE /deals/subscribe`

**Description:** Unsubscribe from a specific deal

**Request:**
```json
{
  "user_id": "U001",
  "deal_id": 1005
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Successfully unsubscribed from deal",
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

**Error Response:**
```json
{
  "status": "error",
  "message": "Deal not found in subscriptions",
  "error_code": "DEAL_NOT_SUBSCRIBED"
}
```

---

### 7. Get Subscribed Deals

**Endpoint:** `GET /deals/subscribed`

**Description:** Get all deals subscribed by the user with total savings

**Request:**
```json
{
  "user_id": "U001"
}
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

**Error Response:**
```json
{
  "status": "error",
  "message": "No subscribed deals found",
  "error_code": "NO_SUBSCRIPTIONS"
}
```

---

### 8. Get All Deals by Category

**Endpoint:** `GET /deals/category/{category}`

**Description:** Get all deals for a specific category

**Request:**
```
GET /deals/category/travel
```

**Response:**
```json
{
  "status": "success",
  "message": "Travel deals retrieved successfully",
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
    },
    {
      "deal_id": 1002,
      "category": "travel",
      "description": "Short Term Stay - 25% discount on vacation rentals for 3+ days. Use code TRAVEL002 at VacationRentals.com",
      "start_date": "2024-01-20",
      "end_date": "2024-04-15",
      "location_state": "Florida",
      "location_pincode": "33101",
      "amount_saved": "$200"
    }
  ],
  "total_count": 2
}
```

---

### 9. Get User Profile

**Endpoint:** `GET /users/{user_id}`

**Description:** Get user profile information

**Request:**
```
GET /users/U001
```

**Response:**
```json
{
  "status": "success",
  "message": "User profile retrieved successfully",
  "data": {
    "user_id": "U001",
    "user_name": "Sarah Johnson",
    "user_location": "New York, NY",
    "user_pincode": "10001",
    "user_preferences": {
      "travel": true,
      "entertainment": true,
      "health": false,
      "events": true,
      "financial": false,
      "fashion": true,
      "automotive": false
    }
  }
}
```

---

### 10. Get Available Categories

**Endpoint:** `GET /categories`

**Description:** Get all available deal categories

**Request:**
```
GET /categories
```

**Response:**
```json
{
  "status": "success",
  "message": "Categories retrieved successfully",
  "data": [
    "travel",
    "entertainment",
    "health",
    "events",
    "financial",
    "fashion",
    "automotive"
  ],
  "total_count": 7
}
```

## Error Codes

| Error Code | Description |
|------------|-------------|
| `USER_NOT_FOUND` | User ID does not exist |
| `DEAL_NOT_FOUND` | Deal ID does not exist |
| `DEAL_NOT_AVAILABLE` | Deal is not available for subscription |
| `DEAL_NOT_SUBSCRIBED` | Deal is not in user's subscriptions |
| `INVALID_PREFERENCES` | Invalid preference format |
| `INVALID_SEARCH_PARAMS` | Invalid search parameters |
| `NO_DEALS_FOUND` | No deals match the criteria |
| `NO_SUBSCRIPTIONS` | User has no subscribed deals |
| `INVALID_USER_ID` | Invalid user ID format |
| `INVALID_DEAL_ID` | Invalid deal ID format |
| `INVALID_DATE_FORMAT` | Invalid date format |
| `INVALID_LOCATION` | Invalid location format |

## HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 201 | Created (for subscription) |
| 400 | Bad Request |
| 404 | Not Found |
| 409 | Conflict (already subscribed) |
| 500 | Internal Server Error |

## Example API Calls

### cURL Examples

**Get User Preferences:**
```bash
curl -X GET http://localhost:5000/api/v1/preferences \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

**Update User Preferences:**
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

**Get Recommended Deals:**
```bash
curl -X GET http://localhost:5000/api/v1/deals/recommended \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

**Subscribe to Deal:**
```bash
curl -X POST http://localhost:5000/api/v1/deals/subscribe \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001", "deal_id": 1005}'
```

**Search Deals:**
```bash
curl -X GET http://localhost:5000/api/v1/deals/search \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "U001",
    "location_state": "California",
    "category": "travel"
  }'
```

### JavaScript Examples

**Get User Preferences:**
```javascript
fetch('http://localhost:5000/api/v1/preferences', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    user_id: 'U001'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

**Subscribe to Deal:**
```javascript
fetch('http://localhost:5000/api/v1/deals/subscribe', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    user_id: 'U001',
    deal_id: 1005
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Rate Limiting

- **Standard endpoints:** 100 requests per minute per user
- **Search endpoints:** 50 requests per minute per user
- **Subscription endpoints:** 20 requests per minute per user

## Data Validation

All API endpoints validate:
- User ID format (4-character alphanumeric)
- Deal ID format (positive integer)
- Date formats (YYYY-MM-DD)
- Location formats (valid US states and 5-digit pincodes)
- Preference formats (boolean values for all categories)

## Notes

1. All dates are in UTC timezone
2. Amount saved values include the $ prefix
3. Location matching is case-insensitive
4. Deal recommendations exclude already subscribed deals
5. Search functionality overrides preference-based filtering
6. All responses include a `total_count` field for pagination support 