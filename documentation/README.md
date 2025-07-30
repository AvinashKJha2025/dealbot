# Deal Recommender Application - Documentation

This directory contains comprehensive documentation for the Deal Recommender Application, a personalized deal recommendation system that matches users with relevant deals based on their preferences, location, and transaction history.

## 📁 Documentation Structure

```
documentation/
├── README.md                    # This overview file
├── requirements_document.md     # Detailed requirements specification
├── json_schemas.md             # JSON schema definitions
├── sample_data.json            # Sample data following the schemas
└── api_documentation.md        # Complete API documentation with examples
```

## 📋 Documentation Overview

### 1. Requirements Document (`requirements_document.md`)
- **Purpose**: Comprehensive project requirements and specifications
- **Contents**:
  - Project overview and core features
  - Data models and business rules
  - Technical requirements
  - User experience requirements
  - Security requirements
  - Future enhancements

### 2. JSON Schemas (`json_schemas.md`)
- **Purpose**: Complete schema definitions for all data structures
- **Contents**:
  - Deal object schemas
  - User and preference schemas
  - Subscription schemas
  - API request/response schemas
  - Validation rules and error handling

### 3. Sample Data (`sample_data.json`)
- **Purpose**: Realistic sample data following the defined schemas
- **Contents**:
  - 35 deals across 7 categories (travel, entertainment, health, events, financial, fashion, automotive)
  - 10 user profiles with diverse preferences
  - 10 subscription records
  - All data follows the defined schemas and validation rules

### 4. API Documentation (`api_documentation.md`)
- **Purpose**: Complete API reference with examples
- **Contents**:
  - 10 API endpoints with detailed specifications
  - Request/response examples for each endpoint
  - Error codes and HTTP status codes
  - cURL and JavaScript examples
  - Rate limiting and validation rules

## 🚀 Quick Start Guide

### Understanding the Application

1. **Read the Requirements Document** to understand the project scope and features
2. **Review the JSON Schemas** to understand data structures
3. **Examine the Sample Data** to see realistic examples
4. **Use the API Documentation** for implementation reference

### Key Features

- **Personalized Recommendations**: Deals matched based on user preferences and location
- **Location-Based Filtering**: Support for state and pincode-based filtering
- **Subscription Management**: Users can subscribe/unsubscribe to deals
- **Search Functionality**: Advanced search with location and category filters
- **Savings Tracking**: Calculate potential savings from subscribed deals

### Data Categories

The application supports 7 deal categories:
- **Travel**: Hotels, resorts, vacation packages
- **Entertainment**: Movies, restaurants, amusement parks
- **Health**: Medical services, fitness, wellness
- **Events**: Concerts, sports, cultural events
- **Financial**: Loans, banking, insurance
- **Fashion**: Clothing, accessories, beauty
- **Automotive**: Cars, maintenance, accessories

## 📊 Sample Data Highlights

### Deals
- **35 total deals** across all categories
- **Unique deal IDs** (1001-7005) for easy identification
- **Realistic descriptions** with deal codes and vendor information
- **Geographic diversity** across major US states
- **Varied savings amounts** from $15 to $5000

### Users
- **10 diverse user profiles** with realistic names and locations
- **Varied preferences** across all deal categories
- **Geographic distribution** across different US states
- **4-character alphanumeric IDs** (U001-U010)

### Subscriptions
- **Realistic subscription patterns** based on user preferences
- **Comma-separated deal IDs** for easy parsing
- **Varied subscription counts** per user

## 🔧 API Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/preferences` | GET | Get user preferences |
| `/preferences` | PUT | Update user preferences |
| `/deals/recommended` | GET | Get personalized recommendations |
| `/deals/search` | GET | Search deals with filters |
| `/deals/subscribe` | POST | Subscribe to a deal |
| `/deals/subscribe` | DELETE | Unsubscribe from a deal |
| `/deals/subscribed` | GET | Get user's subscribed deals |
| `/deals/category/{category}` | GET | Get deals by category |
| `/users/{user_id}` | GET | Get user profile |
| `/categories` | GET | Get all categories |

## 🛠️ Implementation Notes

### Data Storage
- JSON-based storage for simplicity
- Separate files for deals, users, and subscriptions
- Easy to migrate to database in future

### Validation Rules
- User IDs: 4-character alphanumeric format
- Deal IDs: Positive integers
- Dates: YYYY-MM-DD format
- Pincodes: 5-digit format
- Amounts: $ prefix required

### Business Logic
- Deals filtered by user preferences (boolean flags)
- Location matching (state and pincode)
- Date range validation (current date between start/end)
- Subscription exclusion (don't show already subscribed deals)

## 🔍 Testing with Sample Data

### Example User Scenarios

1. **Sarah Johnson (U001)** - New York resident
   - Preferences: Travel, Entertainment, Events, Fashion
   - Subscribed to: 4 deals (travel, entertainment, events, fashion)
   - Total potential savings: $180

2. **Michael Chen (U002)** - Los Angeles resident
   - Preferences: All categories enabled
   - Subscribed to: 6 deals across all categories
   - Total potential savings: $6,150

3. **Emily Rodriguez (U003)** - Miami resident
   - Preferences: Travel, Health, Events, Fashion
   - Subscribed to: 4 deals (travel, health, events, fashion)
   - Total potential savings: $625

## 📈 Future Enhancements

The documentation includes considerations for:
- Database migration from JSON to SQL
- Microservices architecture
- Caching mechanisms
- Push notifications
- Social sharing features
- Advanced analytics

## 🤝 Contributing

When updating the documentation:
1. Ensure all schemas are consistent
2. Update sample data to match schema changes
3. Verify API examples work with current implementation
4. Maintain consistency across all documents

## 📞 Support

For questions about the documentation or implementation:
1. Review the requirements document for feature specifications
2. Check the JSON schemas for data structure details
3. Use the API documentation for integration guidance
4. Test with the provided sample data

---

**Last Updated**: January 2024  
**Version**: 1.0  
**Status**: Complete 