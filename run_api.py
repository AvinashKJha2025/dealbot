#!/usr/bin/env python3
"""
Startup script for the Deal Recommender API
This script provides an easy way to start the Flask application
"""

import subprocess
import sys
import os

def main():
    """Start the Flask API application"""
    print("🚀 Starting Deal Recommender API...")
    print("=" * 50)
    
    # Check if dealrecommendation.py exists
    if not os.path.exists('dealrecommendation.py'):
        print("❌ Error: dealrecommendation.py not found!")
        print("Make sure you're in the correct directory.")
        sys.exit(1)
    
    # Check if required data files exist
    required_files = [
        'documentation/sample_deals.json',
        'documentation/sample_users.json',
        'documentation/sample_subscriptions.json'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Error: Missing required data files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        print("\nPlease ensure all data files are present.")
        sys.exit(1)
    
    print("✅ All required files found!")
    print("🌐 Starting Flask server on http://localhost:6000")
    print("📚 API documentation available at http://localhost:6000/api/v1")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Start the Flask application
        subprocess.run([sys.executable, 'dealrecommendation.py'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 