# Deal Recommender API - Flask Application

A Flask-based REST API for the Deal Recommender Application that provides personalized deal recommendations based on user preferences, location, and transaction history.

## 🚀 Features

- **User Management**: Get and update user preferences
- **Deal Recommendations**: Personalized deals based on preferences and location
- **Search Functionality**: Search deals by location, pincode, and category
- **Subscription Management**: Subscribe/unsubscribe to deals
- **Savings Tracking**: Calculate total potential savings from subscribed deals
- **Comprehensive Validation**: Input validation and error handling

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository** (if not already done):
```bash
git clone <repository-url>
cd virtual_assistant_chatbot
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Verify data files exist**:
   - `documentation/sample_deals.json` - Deal database
   - `documentation/sample_users.json` - User profiles
   - `documentation/sample_subscriptions.json` - User subscriptions

## 🏃‍♂️ Running the Application

### Development Mode
```bash
# Option 1: Direct execution
python dealrecommendation.py

# Option 2: Using startup script (recommended)
python run_api.py
```

The application will start on `http://localhost:6000`

### Production Mode
```bash
export FLASK_ENV=production
python dealrecommendation.py
```

## 📚 API Documentation

### Base URL
```
http://localhost:6000/api/v1
```

### Available Endpoints

#### User Management
- `GET /preferences` - Get user preferences
- `PUT /preferences` - Update user preferences
- `GET /users/{user_id}` - Get user profile

#### Deal Recommendations
- `GET /deals/recommended` - Get personalized recommendations
- `GET /deals/search` - Search deals with filters
- `GET /deals/category/{category}` - Get deals by category
- `GET /categories` - Get all categories

#### Subscription Management
- `POST /deals/subscribe` - Subscribe to a deal
- `DELETE /deals/subscribe` - Unsubscribe from a deal
- `GET /deals/subscribed` - Get subscribed deals

## 🧪 Testing with Postman

### Import Postman Collection

1. Open Postman
2. Click "Import" button
3. Select the file: `documentation/Deal_Recommender_API.postman_collection.json`
4. The collection will be imported with all endpoints and test examples

### Environment Variables

Set up the following environment variables in Postman:
- `base_url`: `http://localhost:5000`
- `user_id`: `U001` (or any valid user ID)
- `deal_id`: `1005` (or any valid deal ID)

### Test Scenarios

The Postman collection includes:

1. **User Management Tests**
   - Get user preferences
   - Update user preferences
   - Get user profile

2. **Deal Recommendation Tests**
   - Get recommended deals
   - Search deals with filters
   - Get deals by category

3. **Subscription Tests**
   - Subscribe to deals
   - Unsubscribe from deals
   - Get subscribed deals

4. **Error Testing**
   - Invalid user ID
   - User not found
   - Deal not found
   - Invalid category

## 📊 Sample Data

The application comes with comprehensive sample data:

### Users (10 users)
- User IDs: U001-U010
- Diverse preferences across all categories
- Different locations across US states

### Deals (35 deals)
- 7 categories: travel, entertainment, health, events, financial, fashion, automotive
- Deal IDs: 1001-7005
- Geographic coverage across major US states
- Savings range: $15 to $5000

### Subscriptions
- Pre-configured subscriptions for all users
- Realistic subscription patterns

## 🔧 API Examples

### Get User Preferences
```bash
curl -X GET http://localhost:6000/api/v1/preferences \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

### Get Recommended Deals
```bash
curl -X GET http://localhost:6000/api/v1/deals/recommended \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001"}'
```

### Subscribe to Deal
```bash
curl -X POST http://localhost:6000/api/v1/deals/subscribe \
  -H "Content-Type: application/json" \
  -d '{"user_id": "U001", "deal_id": 1005}'
```

### Search Deals
```bash
curl -X GET http://localhost:6000/api/v1/deals/search \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "U001",
    "location_state": "California",
    "category": "travel"
  }'
```

## 📝 Response Format

All API responses follow a standard format:

```json
{
  "status": "success|error",
  "message": "Human-readable message",
  "data": {...},
  "total_count": 0
}
```

## ⚠️ Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input parameters
- **404 Not Found**: User or deal not found
- **409 Conflict**: Deal already subscribed
- **500 Internal Server Error**: Server-side errors

## 🔍 Validation Rules

- **User ID**: 4-character alphanumeric format (e.g., "U001")
- **Deal ID**: Positive integer
- **Dates**: YYYY-MM-DD format
- **Pincodes**: 5-digit format
- **Amounts**: Must include $ prefix
- **Preferences**: Boolean values for all 7 categories

## 🚦 Rate Limiting

- **Standard endpoints**: 100 requests/minute per user
- **Search endpoints**: 50 requests/minute per user
- **Subscription endpoints**: 20 requests/minute per user

## 📁 Project Structure

```
virtual_assistant_chatbot/
├── app.py                          # Streamlit application
├── dealrecommendation.py           # Flask API application
├── run_api.py                      # API startup script
├── test_api.py                     # API testing script
├── requirements.txt                # Python dependencies
├── data/                          # Original data files (if any)
├── documentation/
│   ├── sample_deals.json          # Sample deal database
│   ├── sample_users.json          # Sample user profiles
│   ├── sample_subscriptions.json  # Sample user subscriptions
│   ├── requirements_document.md   # Project requirements
│   ├── json_schemas.md           # Data schemas
│   ├── sample_data.json          # Sample data
│   ├── api_documentation.md      # API documentation
│   ├── api_specification_table.md # API specification table
│   ├── Deal_Recommender_API.postman_collection.json # Postman collection
│   └── README.md                 # Documentation overview
└── README.md                     # This file
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill the process
   kill -9 <PID>
   ```

2. **Data files not found**:
   - Ensure all JSON files exist in the `data/` directory
   - Check file permissions

3. **Import errors**:
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

### Debug Mode

Enable debug mode for detailed error messages:
```bash
export FLASK_DEBUG=1
python app.py
```

## 🔄 Data Updates

To update the sample data:

1. **Add new deals**: Edit `documentation/sample_deals.json`
2. **Add new users**: Edit `documentation/sample_users.json`
3. **Update subscriptions**: Edit `documentation/sample_subscriptions.json`

The application will automatically load the updated data on restart.

## 📈 Performance

- **Response Time**: < 2000ms for most requests
- **Concurrent Users**: Supports multiple concurrent requests
- **Data Loading**: Efficient JSON file loading with caching

## 🔒 Security Considerations

- Input validation on all endpoints
- SQL injection protection (JSON-based storage)
- CORS enabled for cross-origin requests
- Error message sanitization

## 🚀 Deployment

### Local Development
```bash
python dealrecommendation.py
```

### Production Deployment
```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:6000 app:app

# Using Docker
docker build -t deal-recommender-api .
docker run -p 6000:6000 deal-recommender-api
```

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Test with the provided Postman collection
4. Check the sample data for reference

## 📄 License

This project is part of the Deal Recommender Application suite.

---

**Happy Testing! 🎉** 