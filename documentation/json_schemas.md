# JSON Schema Definitions - Deal Recommender Application

## 1. Deal Schema

### 1.1 Individual Deal Object
```json
{
  "type": "object",
  "properties": {
    "deal_id": {
      "type": "integer",
      "description": "Unique numeric identifier for the deal",
      "minimum": 1
    },
    "category": {
      "type": "string",
      "enum": ["travel", "entertainment", "health", "events", "financial", "fashion", "automotive"],
      "description": "Category classification of the deal"
    },
    "description": {
      "type": "string",
      "description": "Detailed description of the offer including deal code, vendor, and savings percentage",
      "minLength": 10,
      "maxLength": 500
    },
    "start_date": {
      "type": "string",
      "format": "date",
      "description": "Deal start date in YYYY-MM-DD format"
    },
    "end_date": {
      "type": "string",
      "format": "date",
      "description": "Deal end date in YYYY-MM-DD format"
    },
    "location_state": {
      "type": "string",
      "description": "US state where the deal is valid",
      "minLength": 2,
      "maxLength": 50
    },
    "location_pincode": {
      "type": "string",
      "description": "Specific pincode for deal location",
      "pattern": "^[0-9]{5}$"
    },
    "amount_saved": {
      "type": "string",
      "description": "Approximate savings in USD with $ prefix",
      "pattern": "^\\$[0-9]+$"
    }
  },
  "required": ["deal_id", "category", "description", "start_date", "end_date", "location_state", "location_pincode", "amount_saved"],
  "additionalProperties": false
}
```

### 1.2 Deals Database Structure
```json
{
  "type": "object",
  "properties": {
    "travel": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "entertainment": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "health": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "events": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "financial": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "fashion": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "automotive": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    }
  },
  "required": ["travel", "entertainment", "health", "events", "financial", "fashion", "automotive"],
  "additionalProperties": false
}
```

## 2. User Schema

### 2.1 User Preferences Object
```json
{
  "type": "object",
  "properties": {
    "travel": {
      "type": "boolean",
      "description": "User preference for travel deals"
    },
    "entertainment": {
      "type": "boolean",
      "description": "User preference for entertainment deals"
    },
    "health": {
      "type": "boolean",
      "description": "User preference for health deals"
    },
    "events": {
      "type": "boolean",
      "description": "User preference for events deals"
    },
    "financial": {
      "type": "boolean",
      "description": "User preference for financial deals"
    },
    "fashion": {
      "type": "boolean",
      "description": "User preference for fashion deals"
    },
    "automotive": {
      "type": "boolean",
      "description": "User preference for automotive deals"
    }
  },
  "required": ["travel", "entertainment", "health", "events", "financial", "fashion", "automotive"],
  "additionalProperties": false
}
```

### 2.2 Individual User Object
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "description": "4-digit alphanumeric unique identifier",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "user_name": {
      "type": "string",
      "description": "User's full name",
      "minLength": 2,
      "maxLength": 100
    },
    "user_location": {
      "type": "string",
      "description": "User's location in format 'City, State'",
      "minLength": 5,
      "maxLength": 100
    },
    "user_pincode": {
      "type": "string",
      "description": "User's pincode",
      "pattern": "^[0-9]{5}$"
    },
    "user_preferences": {
      "$ref": "#/definitions/userPreferences"
    }
  },
  "required": ["user_id", "user_name", "user_location", "user_pincode", "user_preferences"],
  "additionalProperties": false
}
```

### 2.3 Users Database Structure
```json
{
  "type": "array",
  "items": {
    "$ref": "#/definitions/user"
  },
  "minItems": 0
}
```

## 3. Subscription Schema

### 3.1 Individual Subscription Object
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "description": "Reference to user ID",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "subscribed_deals": {
      "type": "string",
      "description": "Comma-separated list of deal IDs",
      "pattern": "^[0-9]+(,[0-9]+)*$"
    }
  },
  "required": ["user_id", "subscribed_deals"],
  "additionalProperties": false
}
```

### 3.2 Subscriptions Database Structure
```json
{
  "type": "array",
  "items": {
    "$ref": "#/definitions/subscription"
  },
  "minItems": 0
}
```

## 4. API Request/Response Schemas

### 4.1 Get User Preferences Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    }
  },
  "required": ["user_id"],
  "additionalProperties": false
}
```

### 4.2 Get User Preferences Response
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["success", "error"]
    },
    "message": {
      "type": "string"
    },
    "data": {
      "$ref": "#/definitions/userPreferences"
    }
  },
  "required": ["status", "message"],
  "additionalProperties": false
}
```

### 4.3 Update User Preferences Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "preferences": {
      "$ref": "#/definitions/userPreferences"
    }
  },
  "required": ["user_id", "preferences"],
  "additionalProperties": false
}
```

### 4.4 Get Recommended Deals Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "location_state": {
      "type": "string",
      "description": "Optional: Filter by specific state"
    },
    "location_pincode": {
      "type": "string",
      "pattern": "^[0-9]{5}$",
      "description": "Optional: Filter by specific pincode"
    }
  },
  "required": ["user_id"],
  "additionalProperties": false
}
```

### 4.5 Get Recommended Deals Response
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["success", "error"]
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/deal"
      }
    },
    "total_count": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["status", "message", "data", "total_count"],
  "additionalProperties": false
}
```

### 4.6 Subscribe to Deal Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "deal_id": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": ["user_id", "deal_id"],
  "additionalProperties": false
}
```

### 4.7 Unsubscribe from Deal Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "deal_id": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": ["user_id", "deal_id"],
  "additionalProperties": false
}
```

### 4.8 Get Subscribed Deals Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    }
  },
  "required": ["user_id"],
  "additionalProperties": false
}
```

### 4.9 Get Subscribed Deals Response
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["success", "error"]
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "subscribed_deals": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/deal"
          }
        },
        "total_savings": {
          "type": "string",
          "pattern": "^\\$[0-9]+$"
        },
        "deal_count": {
          "type": "integer",
          "minimum": 0
        }
      },
      "required": ["subscribed_deals", "total_savings", "deal_count"]
    }
  },
  "required": ["status", "message", "data"],
  "additionalProperties": false
}
```

### 4.10 Search Deals Request
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "pattern": "^[A-Z0-9]{4}$"
    },
    "location_state": {
      "type": "string",
      "description": "Optional: Search by state"
    },
    "location_pincode": {
      "type": "string",
      "pattern": "^[0-9]{5}$",
      "description": "Optional: Search by pincode"
    },
    "category": {
      "type": "string",
      "enum": ["travel", "entertainment", "health", "events", "financial", "fashion", "automotive"],
      "description": "Optional: Filter by category"
    }
  },
  "required": ["user_id"],
  "additionalProperties": false
}
```

## 5. Error Response Schema

### 5.1 Standard Error Response
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["error"]
    },
    "message": {
      "type": "string",
      "description": "Human-readable error message"
    },
    "error_code": {
      "type": "string",
      "description": "Machine-readable error code"
    },
    "details": {
      "type": "object",
      "description": "Additional error details"
    }
  },
  "required": ["status", "message"],
  "additionalProperties": false
}
```

## 6. Validation Rules

### 6.1 Date Validation
- `start_date` must be before `end_date`
- Both dates must be in YYYY-MM-DD format
- Dates must be valid calendar dates

### 6.2 Amount Validation
- `amount_saved` must be a positive number
- Must include $ prefix
- No decimal places allowed

### 6.3 ID Validation
- `user_id` must be exactly 4 characters (alphanumeric)
- `deal_id` must be a positive integer
- All IDs must be unique within their respective collections

### 6.4 Location Validation
- `location_pincode` must be exactly 5 digits
- `location_state` must be a valid US state name
- Location combinations must be consistent 