# Postman Collection for Deal Recommender API

This document provides instructions for importing and using the Postman collection to test the Deal Recommendation Chatbot API.

## 📁 Files

- `Deal_Recommender_API.postman_collection.json` - The Postman collection file
- `POSTMAN_README.md` - This instruction file

## 🚀 Getting Started

### 1. Start the Flask Application

First, make sure your Flask application is running:

```bash
python userchat.py
```

The application will start on `http://localhost:8000`

### 2. Import the Postman Collection

1. **Open Postman**
2. **Click "Import"** (top left corner)
3. **Choose "File"** tab
4. **Select** `Deal_Recommender_API.postman_collection.json`
5. **Click "Import"**

### 3. Set Up Environment Variables

The collection uses a variable for the base URL:

1. **Click on the collection name** "Deal Recommender API"
2. **Go to "Variables" tab**
3. **Verify** `base_url` is set to `http://localhost:8000`
4. **Click "Save"**

## 📋 Collection Structure

The collection is organized into the following folders:

### 🔍 **Health Check**
- **GET** `/health` - Verify API is running

### 🎯 **Category Searches**
- Show me deals for travel
- Get me travel deals
- Show me deals related to entertainment
- Get deals for health
- Show me home deals

### 📍 **Location Searches**
- Show me deals from New York
- Get deals available in California
- Show deals from Miami
- Get me deals in Chicago
- Show deals available in Austin

### 🏪 **Merchant Searches**
- Show me deals from Netflix
- Get deals from Amazon
- Show deals from Nike
- Get me deals from Expedia
- Show deals from CVS Pharmacy

### 💰 **Amount Searches**
- Show me deals under $50
- Get deals under $100
- Show deals below $30
- Get me deals under $75
- Show deals less than $40

### ⏰ **Timeline Searches**
- Show deals expiring this week
- Get me deals available in March
- Show deals available in April
- Get deals expiring this week
- Show me deals available in September

### ⚠️ **Edge Cases & Error Handling**
- Empty chat text (should return 400)
- Missing chat_text field (should return 400)
- Non-existent category (should return 200 with no results)
- Non-existent merchant (should return 200 with no results)
- Zero amount (should return 200 with no results)
- Random text (should return 200 with no results)
- Incomplete category (should return 200 with no results)

## 🧪 Running Tests

### Individual Tests
1. **Select any request** from the collection
2. **Click "Send"**
3. **Review the response** in the bottom panel

### Run All Tests
1. **Right-click** on the collection name
2. **Select "Run collection"**
3. **Click "Run Deal Recommender API"**
4. **Review results** in the test runner

### Automated Test Scripts
Each request includes automated tests that verify:
- ✅ Status code is 200
- ✅ Response has required fields (message, results)
- ✅ Response time is less than 2000ms

## 📊 Expected Responses

### Successful Search Response
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

### No Results Response
```json
{
    "message": "No results available for your search. Please try different search criteria for deals.",
    "results": []
}
```

### Error Response
```json
{
    "error": "Chat text cannot be empty"
}
```

## 🔧 Customization

### Adding New Tests
1. **Right-click** on any folder
2. **Select "Add request"**
3. **Configure** the request with your test data
4. **Save** the request

### Modifying Base URL
1. **Click** on collection name
2. **Go to "Variables"**
3. **Update** `base_url` value
4. **Save** changes

### Environment-Specific Variables
You can create different environments (dev, staging, prod) with different base URLs.

## 🐛 Troubleshooting

### Common Issues

1. **Connection Refused**
   - Ensure Flask app is running on port 8000
   - Check if port is available: `lsof -i :8000`

2. **404 Not Found**
   - Verify base_url is correct
   - Check if Flask app is running

3. **500 Internal Server Error**
   - Check Flask app logs for errors
   - Verify JSON data files exist in `chatbotsampledata/`

4. **Import Failed**
   - Ensure JSON file is not corrupted
   - Try downloading the file again

### Debug Mode
Enable debug mode in Flask for detailed error messages:
```python
app.run(host='0.0.0.0', port=8000, debug=True)
```

## 📈 Performance Testing

The collection includes response time tests. For load testing:

1. **Use Postman's Collection Runner**
2. **Set iterations** to desired number
3. **Enable delays** between requests
4. **Monitor** response times and success rates

## 🔄 Continuous Integration

You can integrate this collection with:
- **Newman** (Postman CLI)
- **Jenkins** pipelines
- **GitHub Actions**
- **Azure DevOps**

Example Newman command:
```bash
newman run Deal_Recommender_API.postman_collection.json -e environment.json
```

## 📞 Support

If you encounter issues:
1. Check Flask application logs
2. Verify all dependencies are installed
3. Ensure JSON data files are present
4. Test with curl to isolate issues

---

**Happy Testing! 🎉** 