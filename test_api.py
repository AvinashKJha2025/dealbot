#!/usr/bin/env python3
"""
Test script for the Deal Recommender API
Run this script to test all API endpoints
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:6000/api/v1"
TEST_USER_ID = "U001"
TEST_DEAL_ID = 1001  # Changed to a deal that U001 hasn't subscribed to yet

def test_endpoint(method, endpoint, data=None, description=""):
    """Test an API endpoint and print results"""
    url = f"{BASE_URL}{endpoint}"
    
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"Method: {method}")
    print(f"URL: {url}")
    if data:
        print(f"Data: {json.dumps(data, indent=2)}")
    print(f"{'='*60}")
    
    response = None
    try:
        if method == "GET":
            response = requests.get(url, json=data)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url, json=data)
        
        print(f"Status Code: {response.status_code}")
        try:
            response_json = response.json()
            print(f"Response: {json.dumps(response_json, indent=2)}")
        except json.JSONDecodeError:
            print(f"Response: {response.text}")
        
        # Check if this is an error test (expecting 400 or 404)
        is_error_test = "Error Test" in description
        
        # Check if this is a subscription test (409 is valid for already subscribed)
        is_subscription_test = "Subscribe" in description or "subscript" in description.lower()
        
        if response.status_code in [200, 201]:
            print("✅ SUCCESS")
            return True
        elif is_error_test and response.status_code in [400, 404]:
            print("✅ SUCCESS (Expected Error)")
            return True
        elif is_subscription_test and response.status_code == 409:
            print("✅ SUCCESS (Deal Already Subscribed)")
            return True
        else:
            print("❌ FAILED")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ FAILED - Could not connect to server")
        print(f"Make sure the Flask app (dealrecommendation.py) is running on {BASE_URL}")
        return False
    except Exception as e:
        print(f"❌ FAILED - Error: {str(e)}")
        return False

def main():
    """Run all API tests"""
    print("🚀 Deal Recommender API Test Suite")
    print("Make sure the Flask app (dealrecommendation.py) is running on "+str(BASE_URL))
    print("\nStarting tests in 3 seconds...")
    time.sleep(3)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Get User Preferences
    total_tests += 1
    if test_endpoint("GET", "/preferences", {"user_id": TEST_USER_ID}, "Get User Preferences"):
        tests_passed += 1
    
    # Test 2: Get User Profile
    total_tests += 1
    if test_endpoint("GET", f"/users/{TEST_USER_ID}", description="Get User Profile"):
        tests_passed += 1
    
    # Test 3: Get Available Categories
    total_tests += 1
    if test_endpoint("GET", "/categories", description="Get Available Categories"):
        tests_passed += 1
    
    # Test 4: Get Recommended Deals
    total_tests += 1
    if test_endpoint("GET", "/deals/recommended", {"user_id": TEST_USER_ID}, "Get Recommended Deals"):
        tests_passed += 1
    
    # Test 5: Search Deals
    total_tests += 1
    search_data = {
        "user_id": TEST_USER_ID,
        "location_state": "California",
        "category": "travel"
    }
    if test_endpoint("GET", "/deals/search", search_data, "Search Deals"):
        tests_passed += 1
    
    # Test 6: Get Deals by Category
    total_tests += 1
    if test_endpoint("GET", "/deals/category/travel", description="Get Deals by Category"):
        tests_passed += 1
    
    # Test 7: Get Subscribed Deals
    total_tests += 1
    if test_endpoint("GET", "/deals/subscribed", {"user_id": TEST_USER_ID}, "Get Subscribed Deals"):
        tests_passed += 1
    
    # Test 8: Subscribe to Deal
    total_tests += 1
    subscribe_data = {"user_id": TEST_USER_ID, "deal_id": TEST_DEAL_ID}
    if test_endpoint("POST", "/deals/subscribe", subscribe_data, "Subscribe to Deal"):
        tests_passed += 1
    
    # Test 8.5: Unsubscribe from Deal
    total_tests += 1
    unsubscribe_data = {"user_id": TEST_USER_ID, "deal_id": TEST_DEAL_ID}
    if test_endpoint("DELETE", "/deals/subscribe", unsubscribe_data, "Unsubscribe from Deal"):
        tests_passed += 1
    
    # Test 9: Update User Preferences
    total_tests += 1
    preferences_data = {
        "user_id": TEST_USER_ID,
        "preferences": {
            "travel": True,
            "entertainment": False,
            "health": True,
            "events": True,
            "financial": False,
            "fashion": True,
            "automotive": True
        }
    }
    if test_endpoint("PUT", "/preferences", preferences_data, "Update User Preferences"):
        tests_passed += 1
    
    # Test 10: Error Test - Invalid User ID
    total_tests += 1
    if test_endpoint("GET", "/preferences", {"user_id": "123"}, "Error Test - Invalid User ID"):
        tests_passed += 1  # This should return 400, which is expected
    
    # Test 11: Error Test - User Not Found
    total_tests += 1
    if test_endpoint("GET", "/preferences", {"user_id": "U999"}, "Error Test - User Not Found"):
        tests_passed += 1  # This should return 404, which is expected
    
    # Test 12: Error Test - Invalid Category
    total_tests += 1
    if test_endpoint("GET", "/deals/category/invalid", description="Error Test - Invalid Category"):
        tests_passed += 1  # This should return 400, which is expected
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Tests Passed: {tests_passed}/{total_tests}")
    print(f"Success Rate: {(tests_passed/total_tests)*100:.1f}%")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    print(f"\n💡 Tips:")
    print("- Use the Postman collection for more detailed testing")
    print("- Check the API documentation for endpoint details")
    print("- Review the sample data for valid test values")

if __name__ == "__main__":
    main() 