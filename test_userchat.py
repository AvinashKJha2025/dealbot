import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
CHAT_ENDPOINT = f"{BASE_URL}/chat"
HEALTH_ENDPOINT = f"{BASE_URL}/health"

def test_health_check():
    """Test the health check endpoint"""
    print("=" * 80)
    print("🏥 TESTING HEALTH CHECK ENDPOINT")
    print("=" * 80)
    
    try:
        # Log request details
        print("📤 REQUEST DETAILS:")
        print(f"   Endpoint: GET {HEALTH_ENDPOINT}")
        print(f"   Headers: None")
        print()
        
        # Make the request
        response = requests.get(HEALTH_ENDPOINT)
        
        # Log response details
        print("📥 RESPONSE DETAILS:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response.elapsed.total_seconds():.3f}s")
        print(f"   Headers: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            result = response.json()
            print("✅ HEALTH CHECK SUCCESS:")
            print(f"   Status: {result.get('status', 'N/A')}")
            print(f"   Message: {result.get('message', 'N/A')}")
            print(f"   Full Response: {json.dumps(result, indent=2)}")
            print("✅ Health check passed\n")
            return True
        else:
            print("❌ HEALTH CHECK FAILED:")
            print(f"   Status Code: {response.status_code}")
            print(f"   Response: {response.text}")
            print()
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION ERROR:")
        print("   Could not connect to the server")
        print("   Make sure the Flask app is running on port 8000")
        print()
        return False
    except Exception as e:
        print("❌ EXCEPTION:")
        print(f"   Error: {str(e)}")
        print()
        return False

def test_chat_endpoint(chat_text, expected_type="success"):
    """Test the chat endpoint with given text"""
    print("=" * 80)
    print(f"🧪 TESTING: '{chat_text}'")
    print("=" * 80)
    
    try:
        payload = {"chat_text": chat_text}
        
        # Log request details
        print("📤 REQUEST DETAILS:")
        print(f"   Endpoint: POST {CHAT_ENDPOINT}")
        print(f"   Headers: Content-Type: application/json")
        print(f"   Payload: {json.dumps(payload, indent=2)}")
        print()
        
        # Make the request
        response = requests.post(CHAT_ENDPOINT, json=payload)
        
        # Log response details
        print("📥 RESPONSE DETAILS:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response.elapsed.total_seconds():.3f}s")
        print(f"   Headers: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            result = response.json()
            print("✅ SUCCESS RESPONSE:")
            print(f"   Message: {result.get('message', 'No message')}")
            print(f"   Results Count: {len(result.get('results', []))}")
            
            if result.get('results'):
                print("   Sample Results:")
                for i, deal in enumerate(result['results'][:3]):  # Show first 3 results
                    print(f"     {i+1}. {deal.get('deal_merchant', 'N/A')} - {deal.get('deal_saving_amount', 'N/A')}")
                    print(f"        Location: {deal.get('deal_location_city', 'N/A')}, {deal.get('deal_location_state', 'N/A')}")
                    print(f"        Code: {deal.get('deal_code', 'N/A')}")
                    print(f"        Expiry: {deal.get('deal_expiry', 'N/A')}")
                if len(result['results']) > 3:
                    print(f"     ... and {len(result['results']) - 3} more deals")
            
            print(f"   Full Response: {json.dumps(result, indent=2)}")
            print()
            return True
            
        elif response.status_code == 400 and expected_type == "error":
            # This is expected for error cases
            result = response.json()
            print("⚠️  EXPECTED ERROR RESPONSE:")
            print(f"   Error: {result.get('error', 'No error message')}")
            print(f"   Full Response: {json.dumps(result, indent=2)}")
            print()
            return True
            
        else:
            print("❌ UNEXPECTED RESPONSE:")
            print(f"   Error: {response.text}")
            print(f"   Full Response: {json.dumps(response.json() if response.content else {}, indent=2)}")
            print()
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION ERROR:")
        print("   Could not connect to the server")
        print("   Make sure the Flask app is running on port 8000")
        print()
        return False
    except Exception as e:
        print("❌ EXCEPTION:")
        print(f"   Error: {str(e)}")
        print()
        return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server")
        print()
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print()
        return False

def test_category_searches():
    """Test category-based searches"""
    print("=" * 60)
    print("Testing Category Searches")
    print("=" * 60)
    
    category_tests = [
        "Show me deals for travel",
        "Get me travel deals",
        "Show me deals related to entertainment",
        "Get deals for health",
        "Show me home deals",
        "Get me deals for food/drink",
        "Show deals for events",
        "Get me fashion deals",
        "Show me sports deals",
        "Get deals for fitness"
    ]
    
    success_count = 0
    for test in category_tests:
        if test_chat_endpoint(test):
            success_count += 1
    
    print(f"Category Search Results: {success_count}/{len(category_tests)} tests passed\n")
    return success_count

def test_location_searches():
    """Test location-based searches"""
    print("=" * 60)
    print("Testing Location Searches")
    print("=" * 60)
    
    location_tests = [
        "Show me deals from New York",
        "Get deals available in California",
        "Show deals from Miami",
        "Get me deals in Chicago",
        "Show deals available in Austin",
        "Get deals from Las Vegas",
        "Show me deals in Denver",
        "Get deals from Seattle",
        "Show deals available in Phoenix",
        "Get me deals from Portland"
    ]
    
    success_count = 0
    for test in location_tests:
        if test_chat_endpoint(test):
            success_count += 1
    
    print(f"Location Search Results: {success_count}/{len(location_tests)} tests passed\n")
    return success_count

def test_merchant_searches():
    """Test merchant-based searches"""
    print("=" * 60)
    print("Testing Merchant Searches")
    print("=" * 60)
    
    merchant_tests = [
        "Show me deals from Netflix",
        "Get deals from Amazon",
        "Show deals from Nike",
        "Get me deals from Expedia",
        "Show deals from CVS Pharmacy",
        "Get deals from Home Depot",
        "Show me deals from Uber Eats",
        "Get deals from Ticketmaster",
        "Show deals from Zara",
        "Get me deals from Planet Fitness"
    ]
    
    success_count = 0
    for test in merchant_tests:
        if test_chat_endpoint(test):
            success_count += 1
    
    print(f"Merchant Search Results: {success_count}/{len(merchant_tests)} tests passed\n")
    return success_count

def test_amount_searches():
    """Test amount-based searches"""
    print("=" * 60)
    print("Testing Amount Searches")
    print("=" * 60)
    
    amount_tests = [
        "Show me deals under $50",
        "Get deals under $100",
        "Show deals below $30",
        "Get me deals under $75",
        "Show deals less than $40",
        "Get deals under $25",
        "Show me deals below $60",
        "Get deals under $80",
        "Show deals less than $35",
        "Get me deals under $90"
    ]
    
    success_count = 0
    for test in amount_tests:
        if test_chat_endpoint(test):
            success_count += 1
    
    print(f"Amount Search Results: {success_count}/{len(amount_tests)} tests passed\n")
    return success_count

def test_timeline_searches():
    """Test timeline-based searches"""
    print("=" * 60)
    print("Testing Timeline Searches")
    print("=" * 60)
    
    timeline_tests = [
        "Show deals expiring this week",
        "Get me deals available in March",
        "Show deals available in April",
        "Get deals expiring this week",
        "Show me deals available in May",
        "Get deals available in June",
        "Show deals available in July",
        "Get me deals available in August",
        "Show deals available in September",
        "Get deals available in October"
    ]
    
    success_count = 0
    for test in timeline_tests:
        if test_chat_endpoint(test):
            success_count += 1
    
    print(f"Timeline Search Results: {success_count}/{len(timeline_tests)} tests passed\n")
    return success_count

def test_edge_cases():
    """Test edge cases and error handling"""
    print("=" * 60)
    print("Testing Edge Cases and Error Handling")
    print("=" * 60)
    
    edge_tests = [
        ("", "empty input", "error"),
        ("Show me deals for nonexistentcategory", "non-existent category", "success"),
        ("Get deals from nonexistentmerchant", "non-existent merchant", "success"),
        ("Show deals under $0", "zero amount", "success"),
        ("Get deals available in nonexistentmonth", "non-existent month", "success"),
        ("Random text that doesn't match any pattern", "random text", "success"),
        ("Show me deals for", "incomplete category", "success"),
        ("Get deals from", "incomplete merchant", "success"),
        ("Show deals under", "incomplete amount", "success"),
        ("Show deals available in", "incomplete month", "success")
    ]
    
    success_count = 0
    for test, description, expected_type in edge_tests:
        print(f"Testing: {description}")
        if test_chat_endpoint(test, expected_type):
            success_count += 1
    
    print(f"Edge Case Results: {success_count}/{len(edge_tests)} tests passed\n")
    return success_count

def test_invalid_requests():
    """Test invalid request formats"""
    print("=" * 80)
    print("🚫 TESTING INVALID REQUEST FORMATS")
    print("=" * 80)
    
    try:
        # Test without chat_text
        print("📤 TEST 1: Missing chat_text field")
        print(f"   Endpoint: POST {CHAT_ENDPOINT}")
        print(f"   Payload: {{}}")
        print()
        
        response = requests.post(CHAT_ENDPOINT, json={})
        
        print("📥 RESPONSE:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response.elapsed.total_seconds():.3f}s")
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
        print()
        
        # Test with wrong field name
        print("📤 TEST 2: Wrong field name")
        print(f"   Endpoint: POST {CHAT_ENDPOINT}")
        print(f"   Payload: {{\"message\": \"test\"}}")
        print()
        
        response = requests.post(CHAT_ENDPOINT, json={"message": "test"})
        
        print("📥 RESPONSE:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response.elapsed.total_seconds():.3f}s")
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
        print()
        
        # Test with non-JSON data
        print("📤 TEST 3: Non-JSON data")
        print(f"   Endpoint: POST {CHAT_ENDPOINT}")
        print(f"   Payload: \"not json\"")
        print()
        
        response = requests.post(CHAT_ENDPOINT, data="not json")
        
        print("📥 RESPONSE:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response.elapsed.total_seconds():.3f}s")
        print(f"   Response: {response.text}")
        print()
        
        print("✅ Invalid request tests completed\n")
        return True
        
    except Exception as e:
        print("❌ EXCEPTION:")
        print(f"   Error: {str(e)}")
        print()
        return False

def main():
    """Main test function"""
    print("🚀 Starting Deal Recommendation Chatbot Tests")
    print("=" * 60)
    
    # Check if server is running
    if not test_health_check():
        print("❌ Server is not running. Please start the Flask application first.")
        print("Run: python userchat.py")
        return
    
    # Wait a moment for server to be ready
    time.sleep(1)
    
    # Run all test suites
    total_tests = 0
    passed_tests = 0
    
    # Category searches
    passed = test_category_searches()
    total_tests += 10
    passed_tests += passed
    
    # Location searches
    passed = test_location_searches()
    total_tests += 10
    passed_tests += passed
    
    # Merchant searches
    passed = test_merchant_searches()
    total_tests += 10
    passed_tests += passed
    
    # Amount searches
    passed = test_amount_searches()
    total_tests += 10
    passed_tests += passed
    
    # Timeline searches
    passed = test_timeline_searches()
    total_tests += 10
    passed_tests += passed
    
    # Edge cases
    passed = test_edge_cases()
    total_tests += 10
    passed_tests += passed
    
    # Invalid requests
    if test_invalid_requests():
        passed_tests += 1
    total_tests += 1
    
    # Summary
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! The chatbot is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 