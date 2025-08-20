"""
Data Collection Pipeline Example
Demonstrates how to integrate scraped data with machine learning workflows.

This example shows how to:
1. Scrape data using CDP mode
2. Process and clean the data  
3. Prepare it for ML analysis
4. Save in formats suitable for existing ML scripts
"""

import os
import sys
from datetime import datetime

# Add parent directory to path for imports  
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from web_scraping.config import DEFAULT_DELAY, UC_MODE, TEST_MODE
except ImportError:
    DEFAULT_DELAY = 2.5
    UC_MODE = True  
    TEST_MODE = True

def simulate_scraping_pipeline():
    """
    Simulate a complete data collection pipeline.
    
    In a real scenario, this would:
    1. Use SeleniumBase CDP mode to scrape websites
    2. Extract structured data
    3. Clean and normalize the data
    4. Save in formats compatible with existing ML scripts
    """
    
    print("🔄 Starting data collection pipeline simulation...")
    
    # Simulated scraped data (would come from actual scraping)
    scraped_data = [
        {
            'product_name': 'Nike Air Force 1 Low',
            'price': '$90.00',
            'category': 'Shoes',
            'rating': 4.5,
            'reviews': 1250,
            'availability': 'In Stock',
            'scraped_at': datetime.now().isoformat()
        },
        {
            'product_name': 'Nike Air Force 1 High',  
            'price': '$110.00',
            'category': 'Shoes',
            'rating': 4.3,
            'reviews': 890,
            'availability': 'In Stock',
            'scraped_at': datetime.now().isoformat()
        },
        {
            'product_name': 'Nike Air Force 1 Mid',
            'price': '$100.00', 
            'category': 'Shoes',
            'rating': 4.4,
            'reviews': 567,
            'availability': 'Limited Stock',
            'scraped_at': datetime.now().isoformat()
        }
    ]
    
    print(f"📊 Collected {len(scraped_data)} product records")
    
    # Data processing and cleaning
    processed_data = process_scraped_data(scraped_data)
    print(f"🧹 Processed and cleaned {len(processed_data)} records")
    
    # Save in multiple formats for ML compatibility
    save_for_ml_analysis(processed_data)
    
    print("✅ Data collection pipeline completed!")
    
    return processed_data

def process_scraped_data(raw_data):
    """
    Process and clean scraped data.
    
    Args:
        raw_data (list): Raw scraped data
        
    Returns:
        list: Processed data ready for ML analysis
    """
    processed = []
    
    for item in raw_data:
        # Clean price data
        price_str = item['price'].replace('$', '').replace(',', '')
        try:
            price_numeric = float(price_str)
        except ValueError:
            price_numeric = 0.0
        
        # Encode categorical data
        availability_encoded = {
            'In Stock': 1,
            'Limited Stock': 0.5, 
            'Out of Stock': 0
        }.get(item['availability'], 0)
        
        # Create processed record
        processed_item = {
            'product_name': item['product_name'],
            'price_numeric': price_numeric,
            'rating': item['rating'],
            'reviews': item['reviews'],
            'availability_score': availability_encoded,
            'category': item['category'],
            'scraped_at': item['scraped_at']
        }
        
        processed.append(processed_item)
    
    return processed

def save_for_ml_analysis(data):
    """
    Save data in formats compatible with existing ML scripts.
    
    Args:
        data (list): Processed data to save
    """
    
    # Create data directory if it doesn't exist
    os.makedirs('scraped_data', exist_ok=True)
    
    # Save as CSV (compatible with pandas in existing scripts)
    try:
        import pandas as pd
        df = pd.DataFrame(data)
        csv_path = 'scraped_data/nike_products.csv'
        df.to_csv(csv_path, index=False)
        print(f"💾 Saved CSV to {csv_path}")
        
        # Create Excel file (compatible with existing xlsx files)
        excel_path = 'scraped_data/nike_products.xlsx' 
        df.to_excel(excel_path, index=False)
        print(f"💾 Saved Excel to {excel_path}")
        
    except ImportError:
        print("⚠️ pandas not available - saving as JSON")
        import json
        json_path = 'scraped_data/nike_products.json'
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"💾 Saved JSON to {json_path}")
    
    # Save as text for simple analysis
    txt_path = 'scraped_data/nike_products.txt'
    with open(txt_path, 'w') as f:
        f.write("Nike Product Data\n")
        f.write("=" * 50 + "\n\n")
        for item in data:
            f.write(f"Product: {item['product_name']}\n")
            f.write(f"Price: ${item['price_numeric']:.2f}\n")
            f.write(f"Rating: {item['rating']}/5.0\n")
            f.write(f"Reviews: {item['reviews']}\n")
            f.write(f"Availability: {item['availability_score']}\n")
            f.write("-" * 30 + "\n")
    
    print(f"💾 Saved text summary to {txt_path}")

def demonstrate_ml_integration():
    """
    Demonstrate how scraped data can be used with ML algorithms.
    """
    print("\n🤖 Demonstrating ML integration...")
    
    # This would use the actual ML classifiers from the repository
    print("📈 Scraped product data can be used for:")
    print("  • Price prediction models")
    print("  • Product recommendation systems") 
    print("  • Market trend analysis")
    print("  • Customer sentiment analysis")
    print("  • Inventory optimization")
    
    print("\n🔗 Integration with existing ML scripts:")
    print("  • Use scraped data as training features")
    print("  • Apply k-NN classification on product categories")
    print("  • Use naive Bayes for price range prediction")
    print("  • Apply clustering algorithms to group similar products")
    
    # Example feature vector creation
    sample_features = [90.0, 4.5, 1250, 1.0]  # price, rating, reviews, availability
    print(f"\n📊 Example feature vector: {sample_features}")
    print("   (Can be used with existing knn_classifier_ID2693653.py)")

if __name__ == "__main__":
    print("🚀 Data Collection Pipeline Demo")
    print("=" * 50)
    
    # Run the simulation
    data = simulate_scraping_pipeline()
    
    # Demonstrate ML integration
    demonstrate_ml_integration()
    
    print("\n✅ Demo completed!")
    print("💡 To run real scraping, install SeleniumBase and run:")
    print("   python setup_scraping.py")
    print("   python run_examples.py raw_nike")