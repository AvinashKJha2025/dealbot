# Deal Recommender Application - Requirements Document

## 1. Project Overview

The Deal Recommender Application is a personalized deal recommendation system that matches users with relevant deals based on their preferences, location, and transaction history. The system enables users to subscribe to deals, manage their preferences, and track potential savings.

## 2. Core Features

### 2.1 User Management
- User registration and profile management
- User preference management across deal categories
- Location-based deal filtering (state and pincode)

### 2.2 Deal Management
- Deal categorization and storage
- Deal recommendation engine based on user preferences
- Location-based deal filtering
- Deal subscription and unsubscription

### 2.3 Recommendation Engine
- Preference-based deal matching
- Location-based filtering (state and pincode)
- Exclusion of already subscribed deals
- Search functionality with location/pincode filters

### 2.4 Subscription Management
- Deal subscription tracking
- Potential savings calculation
- Subscription history management

## 3. Data Models

### 3.1 Deal Structure
Each deal contains:
- **deal_id**: Unique numeric identifier
- **category**: Deal category (travel, entertainment, health, events, financial, fashion, automotive)
- **description**: Offer description with deal code, vendor, and savings percentage
- **start_date**: Deal start date (US format)
- **end_date**: Deal end date (US format)
- **location_state**: US state where deal is valid
- **location_pincode**: Specific pincode for deal location
- **amount_saved**: Approximate savings in USD

### 3.2 User Structure
Each user contains:
- **user_id**: 4-digit alphanumeric unique identifier
- **user_name**: User's full name
- **user_preferences**: JSON object with boolean values for each deal category
- **user_location**: User's location (state, city)
- **user_pincode**: User's pincode

### 3.3 Subscription Structure
Each subscription contains:
- **user_id**: Reference to user
- **subscribed_deals**: Comma-separated list of deal IDs

## 4. Business Rules

### 4.1 Deal Recommendation Rules
1. Deals are shown based on user preferences (categories marked as true)
2. Location matching: User's state/pincode must match deal location
3. Exclude deals already subscribed by the user
4. Show deals within valid date range (current date between start_date and end_date)

### 4.2 Search Functionality
1. Users can search deals by specifying location and/or pincode
2. Search results override preference-based filtering
3. Still exclude already subscribed deals

### 4.3 Subscription Rules
1. Users can subscribe to any available deal
2. Subscribed deals are removed from recommendation lists
3. Users can view all subscribed deals and total potential savings

## 5. Technical Requirements

### 5.1 API Requirements
- RESTful API design
- JSON payload format for all requests/responses
- Proper HTTP status codes
- Error handling and validation

### 5.2 Data Storage
- JSON-based data storage
- Separate files for deals, users, and subscriptions
- Data persistence and backup mechanisms

### 5.3 Performance Requirements
- Fast deal recommendation generation
- Efficient search functionality
- Scalable architecture for future enhancements

## 6. User Experience Requirements

### 6.1 Interface Requirements
- Intuitive deal browsing interface
- Easy preference management
- Clear subscription status
- Savings calculation display

### 6.2 Accessibility
- Mobile-responsive design
- Clear navigation
- Error message clarity
- Loading state indicators

## 7. Security Requirements

### 7.1 Data Protection
- User data privacy
- Secure API endpoints
- Input validation and sanitization
- Protection against common web vulnerabilities

### 7.2 Authentication
- User session management
- Secure user identification
- Access control for user-specific data

## 8. Future Enhancements

### 8.1 Planned Features
- Deal rating and reviews
- Social sharing functionality
- Push notifications for new deals
- Advanced analytics and reporting
- Integration with external deal providers

### 8.2 Scalability Considerations
- Database migration from JSON to SQL
- Microservices architecture
- Caching mechanisms
- Load balancing capabilities 