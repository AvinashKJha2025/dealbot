#!/usr/bin/env python3
"""
Script to generate 15 deals per category with diverse data
"""

import json
from datetime import datetime, timedelta
import random

def generate_deals():
    """Generate 15 deals per category"""
    
    # Define categories
    categories = ['travel', 'entertainment', 'health', 'events', 'financial', 'fashion', 'automotive']
    
    # Define locations and pincodes
    locations = [
        ("California", "90210"), ("California", "90211"), ("California", "90212"),
        ("New York", "10001"), ("New York", "10002"), ("New York", "10003"),
        ("Florida", "33101"), ("Florida", "33102"), ("Florida", "33103"),
        ("Texas", "75001"), ("Texas", "75002"), ("Texas", "75003"),
        ("Colorado", "80202"), ("Colorado", "80203"), ("Colorado", "80204"),
        ("Illinois", "60601"), ("Illinois", "60602"), ("Illinois", "60603"),
        ("Arizona", "85001"), ("Arizona", "85002"), ("Arizona", "85003"),
        ("Washington", "98101"), ("Washington", "98102"), ("Washington", "98103"),
        ("Pennsylvania", "19101"), ("Pennsylvania", "19102"), ("Pennsylvania", "19103"),
        ("Ohio", "43201"), ("Ohio", "43202"), ("Ohio", "43203"),
        ("Georgia", "30301"), ("Georgia", "30302"), ("Georgia", "30303"),
        ("Michigan", "48201"), ("Michigan", "48202"), ("Michigan", "48203"),
        ("Tennessee", "37201"), ("Tennessee", "37202"), ("Tennessee", "37203"),
        ("Oregon", "97201"), ("Oregon", "97202"), ("Oregon", "97203"),
        ("Nevada", "89101"), ("Nevada", "89102"), ("Nevada", "89103"),
        ("Utah", "84101"), ("Utah", "84102"), ("Utah", "84103"),
        ("Minnesota", "55401"), ("Minnesota", "55402"), ("Minnesota", "55403")
    ]
    
    # Category-specific deal templates
    deal_templates = {
        'travel': [
            "Weekend Gateway Package - {discount}% off on {duration}-night stays at luxury resorts. Use code {code} at {vendor}",
            "Beach Resort Special - {discount}% discount on beachfront properties. Use code {code} at {vendor}",
            "Mountain Adventure - {discount}% off on ski resort bookings. Use code {code} at {vendor}",
            "Urban Explorer - {discount}% off on city hotel stays. Use code {code} at {vendor}",
            "City Break - {discount}% off on urban hotel stays in major cities. Use code {code} at {vendor}",
            "Luxury Cruise - {discount}% off on Caribbean cruises. Use code {code} at {vendor}",
            "Adventure Tour - {discount}% off on guided hiking tours. Use code {code} at {vendor}",
            "Business Travel - {discount}% off on corporate hotel bookings. Use code {code} at {vendor}",
            "Family Vacation - {discount}% off on family-friendly resorts. Use code {code} at {vendor}",
            "Romantic Getaway - {discount}% off on couples retreats. Use code {code} at {vendor}",
            "Backpacking Trip - {discount}% off on budget hostels. Use code {code} at {vendor}",
            "Cultural Tour - {discount}% off on historical site visits. Use code {code} at {vendor}",
            "Food & Wine Tour - {discount}% off on culinary experiences. Use code {code} at {vendor}",
            "Photography Tour - {discount}% off on scenic photography trips. Use code {code} at {vendor}",
            "Wellness Retreat - {discount}% off on spa and wellness packages. Use code {code} at {vendor}"
        ],
        'entertainment': [
            "Movie Night Special - Buy 2 tickets, get 1 free at {vendor}. Use code {code}",
            "Restaurant Dining - {discount}% discount on fine dining experiences. Use code {code} at {vendor}",
            "Theme Park Adventure - {discount}% off on {vendor} tickets. Use code {code}",
            "Concert Tickets - {discount}% off on live music events. Use code {code} at {vendor}",
            "Bowling Night - 2 games for the price of 1. Use code {code} at {vendor}",
            "Comedy Show - {discount}% off on stand-up comedy nights. Use code {code} at {vendor}",
            "Escape Room - {discount}% off on puzzle adventures. Use code {code} at {vendor}",
            "Arcade Games - {discount}% off on gaming tokens. Use code {code} at {vendor}",
            "Karaoke Night - {discount}% off on private karaoke rooms. Use code {code} at {vendor}",
            "Dance Class - {discount}% off on dance lessons. Use code {code} at {vendor}",
            "Art Workshop - {discount}% off on painting classes. Use code {code} at {vendor}",
            "Cooking Class - {discount}% off on culinary workshops. Use code {code} at {vendor}",
            "Wine Tasting - {discount}% off on wine sampling events. Use code {code} at {vendor}",
            "Trivia Night - {discount}% off on pub quiz events. Use code {code} at {vendor}",
            "Board Game Cafe - {discount}% off on tabletop gaming. Use code {code} at {vendor}"
        ],
        'health': [
            "Gym Membership - {discount}% off on annual fitness memberships. Use code {code} at {vendor}",
            "Yoga Classes - {discount}% off on yoga sessions. Use code {code} at {vendor}",
            "Personal Training - {discount}% off on fitness coaching. Use code {code} at {vendor}",
            "Nutrition Consultation - {discount}% off on diet planning. Use code {code} at {vendor}",
            "Massage Therapy - {discount}% off on relaxation treatments. Use code {code} at {vendor}",
            "Dental Checkup - {discount}% off on dental cleaning. Use code {code} at {vendor}",
            "Eye Exam - {discount}% off on vision screening. Use code {code} at {vendor}",
            "Physical Therapy - {discount}% off on rehabilitation sessions. Use code {code} at {vendor}",
            "Mental Health - {discount}% off on therapy sessions. Use code {code} at {vendor}",
            "Chiropractic Care - {discount}% off on spinal adjustments. Use code {code} at {vendor}",
            "Acupuncture - {discount}% off on traditional treatments. Use code {code} at {vendor}",
            "Meditation App - {discount}% off on mindfulness subscriptions. Use code {code} at {vendor}",
            "Fitness Equipment - {discount}% off on home gym gear. Use code {code} at {vendor}",
            "Health Supplements - {discount}% off on vitamin packages. Use code {code} at {vendor}",
            "Wellness Retreat - {discount}% off on health-focused getaways. Use code {code} at {vendor}"
        ],
        'events': [
            "Music Festival - {discount}% off on festival tickets. Use code {code} at {vendor}",
            "Sports Game - {discount}% off on stadium tickets. Use code {code} at {vendor}",
            "Conference Pass - {discount}% off on business events. Use code {code} at {vendor}",
            "Wedding Expo - {discount}% off on bridal shows. Use code {code} at {vendor}",
            "Food Festival - {discount}% off on culinary events. Use code {code} at {vendor}",
            "Art Exhibition - {discount}% off on gallery openings. Use code {code} at {vendor}",
            "Tech Conference - {discount}% off on innovation summits. Use code {code} at {vendor}",
            "Comic Con - {discount}% off on pop culture conventions. Use code {code} at {vendor}",
            "Book Fair - {discount}% off on literary events. Use code {code} at {vendor}",
            "Film Festival - {discount}% off on cinema celebrations. Use code {code} at {vendor}",
            "Fashion Show - {discount}% off on runway events. Use code {code} at {vendor}",
            "Car Show - {discount}% off on automotive exhibitions. Use code {code} at {vendor}",
            "Wine Festival - {discount}% off on wine tasting events. Use code {code} at {vendor}",
            "Beer Festival - {discount}% off on craft beer events. Use code {code} at {vendor}",
            "Holiday Market - {discount}% off on seasonal markets. Use code {code} at {vendor}"
        ],
        'financial': [
            "Credit Card - {discount}% off on annual fees. Use code {code} at {vendor}",
            "Investment Account - {discount}% off on trading fees. Use code {code} at {vendor}",
            "Insurance Policy - {discount}% off on premium payments. Use code {code} at {vendor}",
            "Loan Application - {discount}% off on processing fees. Use code {code} at {vendor}",
            "Tax Preparation - {discount}% off on tax filing services. Use code {code} at {vendor}",
            "Financial Planning - {discount}% off on advisory services. Use code {code} at {vendor}",
            "Retirement Account - {discount}% off on management fees. Use code {code} at {vendor}",
            "Mortgage Refinance - {discount}% off on closing costs. Use code {code} at {vendor}",
            "Student Loan - {discount}% off on consolidation fees. Use code {code} at {vendor}",
            "Business Banking - {discount}% off on account fees. Use code {code} at {vendor}",
            "Cryptocurrency - {discount}% off on trading fees. Use code {code} at {vendor}",
            "Real Estate - {discount}% off on property management. Use code {code} at {vendor}",
            "Peer Lending - {discount}% off on platform fees. Use code {code} at {vendor}",
            "Forex Trading - {discount}% off on currency exchange. Use code {code} at {vendor}",
            "Commodities - {discount}% off on futures trading. Use code {code} at {vendor}"
        ],
        'fashion': [
            "Designer Clothing - {discount}% off on luxury apparel. Use code {code} at {vendor}",
            "Shoe Collection - {discount}% off on footwear. Use code {code} at {vendor}",
            "Accessories - {discount}% off on jewelry and bags. Use code {code} at {vendor}",
            "Luxury Watches - {discount}% off on timepieces. Use code {code} at {vendor}",
            "Designer Bags - {discount}% off on handbags. Use code {code} at {vendor}",
            "Formal Wear - {discount}% off on suits and dresses. Use code {code} at {vendor}",
            "Casual Clothing - {discount}% off on everyday wear. Use code {code} at {vendor}",
            "Athletic Wear - {discount}% off on sports clothing. Use code {code} at {vendor}",
            "Swimwear - {discount}% off on beach attire. Use code {code} at {vendor}",
            "Winter Collection - {discount}% off on cold weather gear. Use code {code} at {vendor}",
            "Summer Collection - {discount}% off on warm weather clothing. Use code {code} at {vendor}",
            "Vintage Clothing - {discount}% off on retro fashion. Use code {code} at {vendor}",
            "Sustainable Fashion - {discount}% off on eco-friendly clothing. Use code {code} at {vendor}",
            "Custom Tailoring - {discount}% off on bespoke clothing. Use code {code} at {vendor}",
            "Fashion Styling - {discount}% off on personal styling services. Use code {code} at {vendor}"
        ],
        'automotive': [
            "Car Insurance - {discount}% off on auto insurance. Use code {code} at {vendor}",
            "Car Maintenance - {discount}% off on service packages. Use code {code} at {vendor}",
            "Car Wash - {discount}% off on detailing services. Use code {code} at {vendor}",
            "Oil Change - {discount}% off on maintenance services. Use code {code} at {vendor}",
            "Tire Replacement - {discount}% off on tire packages. Use code {code} at {vendor}",
            "Car Rental - {discount}% off on vehicle rentals. Use code {code} at {vendor}",
            "Car Financing - {discount}% off on loan rates. Use code {code} at {vendor}",
            "Extended Warranty - {discount}% off on protection plans. Use code {code} at {vendor}",
            "GPS Navigation - {discount}% off on navigation systems. Use code {code} at {vendor}",
            "Car Audio - {discount}% off on sound systems. Use code {code} at {vendor}",
            "Car Accessories - {discount}% off on vehicle add-ons. Use code {code} at {vendor}",
            "Motorcycle Insurance - {discount}% off on bike coverage. Use code {code} at {vendor}",
            "RV Rental - {discount}% off on recreational vehicles. Use code {code} at {vendor}",
            "Boat Insurance - {discount}% off on marine coverage. Use code {code} at {vendor}",
            "Auto Parts - {discount}% off on replacement parts. Use code {code} at {vendor}"
        ]
    }
    
    # Vendor names for each category
    vendors = {
        'travel': ['Luxury Escapes', 'Coastal Resorts', 'Mountain Getaways', 'Urban Hotels', 'Adventure Tours', 'Luxury Cruises', 'Guided Hikes', 'Corporate Hotels', 'Family Resorts', 'Couples Retreats', 'Budget Hostels', 'Historical Tours', 'Culinary Experiences', 'Photography Trips', 'Wellness Spas'],
        'entertainment': ['AMC Theaters', 'Fine Dining Group', 'Disney World', 'Live Nation', 'Strike Zone', 'Comedy Club', 'Escape Rooms', 'Game Arcade', 'Karaoke Bar', 'Dance Studio', 'Art Gallery', 'Cooking School', 'Wine Cellar', 'Pub Quiz', 'Board Game Cafe'],
        'health': ['Fitness First', 'Yoga Studio', 'Personal Trainers', 'Nutrition Experts', 'Relaxation Spa', 'Dental Care', 'Vision Center', 'Physical Therapy', 'Mental Health Clinic', 'Chiropractic Care', 'Acupuncture Center', 'Meditation App', 'Fitness Equipment', 'Health Supplements', 'Wellness Retreat'],
        'events': ['Music Festivals', 'Sports Stadium', 'Business Events', 'Bridal Shows', 'Food Festivals', 'Art Galleries', 'Tech Conferences', 'Comic Con', 'Book Fairs', 'Film Festivals', 'Fashion Shows', 'Car Shows', 'Wine Festivals', 'Beer Festivals', 'Holiday Markets'],
        'financial': ['Credit Union', 'Investment Bank', 'Insurance Co', 'Loan Services', 'Tax Prep', 'Financial Advisors', 'Retirement Plans', 'Mortgage Bank', 'Student Loans', 'Business Bank', 'Crypto Exchange', 'Real Estate', 'Peer Lending', 'Forex Trading', 'Commodities'],
        'fashion': ['Luxury Boutique', 'Shoe Store', 'Accessories Shop', 'Watch Store', 'Designer Bags', 'Formal Wear', 'Casual Clothing', 'Athletic Wear', 'Swimwear Shop', 'Winter Collection', 'Summer Collection', 'Vintage Store', 'Eco Fashion', 'Custom Tailor', 'Fashion Stylist'],
        'automotive': ['Auto Insurance', 'Car Service', 'Car Wash', 'Oil Change', 'Tire Shop', 'Car Rental', 'Auto Finance', 'Warranty Co', 'GPS Systems', 'Car Audio', 'Auto Accessories', 'Motorcycle Ins', 'RV Rental', 'Boat Insurance', 'Auto Parts']
    }
    
    deals_data = {"deals": {}}
    deal_id_counter = 1001
    
    for category in categories:
        deals_data["deals"][category] = []
        
        for i in range(15):
            # Select random location
            location_state, location_pincode = random.choice(locations)
            
            # Generate random discount and savings
            discount = random.randint(10, 50)
            savings = random.randint(10, 300)
            
            # Select template and vendor
            template = random.choice(deal_templates[category])
            vendor = random.choice(vendors[category])
            
            # Generate code
            code = f"{category.upper()}{deal_id_counter:03d}"
            
            # Generate dates
            start_date = datetime(2025, random.randint(1, 6), random.randint(1, 28))
            end_date = start_date + timedelta(days=random.randint(30, 180))
            
            # Create deal description
            description = template.format(
                discount=discount,
                duration=random.randint(1, 7),
                code=code,
                vendor=vendor
            )
            
            deal = {
                "deal_id": deal_id_counter,
                "category": category,
                "description": description,
                "start_date": start_date.strftime('%Y-%m-%d'),
                "end_date": end_date.strftime('%Y-%m-%d'),
                "location_state": location_state,
                "location_pincode": location_pincode,
                "amount_saved": f"${savings}"
            }
            
            deals_data["deals"][category].append(deal)
            deal_id_counter += 1
    
    # Write to file
    with open('documentation/sample_deals.json', 'w') as f:
        json.dump(deals_data, f, indent=2)
    
    print("✅ Generated 15 deals per category (105 total deals)")
    print("📊 Deal distribution:")
    for category in categories:
        print(f"   {category.capitalize()}: {len(deals_data['deals'][category])} deals")
    print(f"📁 Saved to documentation/sample_deals.json")

if __name__ == "__main__":
    generate_deals() 