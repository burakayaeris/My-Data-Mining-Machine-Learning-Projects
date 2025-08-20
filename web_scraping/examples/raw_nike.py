"""
Nike Website Scraping Example using SeleniumBase CDP Mode
Based on: https://github.com/mdmintz/undetected-testing/blob/master/raw_nike.py

This script demonstrates how to scrape the Nike website using SeleniumBase's
CDP (Chrome DevTools Protocol) mode which helps bypass bot detection.
"""

from seleniumbase import SB
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from web_scraping.config import *
except ImportError:
    # Fallback defaults if config not available
    UC_MODE = True
    TEST_MODE = True
    LOCALE = "en"
    DEFAULT_DELAY = 2.5
    NIKE_SEARCH_DELAY = 4
    NIKE_DEFAULT_SEARCH = "Nike Air Force 1"

def scrape_nike_products(search_term=None):
    """
    Scrape Nike products using undetected CDP mode.
    
    Args:
        search_term (str): Product to search for on Nike website
        
    Returns:
        list: List of product information dictionaries
    """
    if search_term is None:
        search_term = NIKE_DEFAULT_SEARCH
        
    print(f"🔍 Searching Nike for: {search_term}")
    
    # Store results
    products = []
    
    # Using UC mode with CDP for undetected scraping
    with SB(uc=UC_MODE, test=TEST_MODE, locale_code=LOCALE, pls="none") as sb:
        url = "https://www.nike.com/"
        
        # Activate CDP mode - this disconnects WebDriver and uses CDP for stealth
        sb.activate_cdp_mode(url)
        
        # Wait for page to load
        sb.sleep(DEFAULT_DELAY)
        
        try:
            # Click the search icon/container
            sb.cdp.mouse_click('div[data-testid="user-tools-container"]')
            sb.sleep(1.5)
            
            # Type the search term (human-like speed)
            sb.cdp.press_keys('input[type="search"]', search_term)
            sb.sleep(NIKE_SEARCH_DELAY)
            
            # Get search results
            elements = sb.cdp.select_all('ul[data-testid*="products"] figure .details')
            
            if elements:
                print(f'✅ Found {len(elements)} results for "{search_term}":')
                for i, element in enumerate(elements, 1):
                    product_text = element.text.strip()
                    if product_text:
                        print(f"  {i}. {product_text}")
                        
                        # Try to extract structured data
                        product_info = {
                            'rank': i,
                            'text': product_text,
                            'search_term': search_term
                        }
                        
                        # Try to get additional details from parent element
                        try:
                            parent = element.get_parent()
                            if parent:
                                # Look for price information
                                price_elem = parent.query_selector('[data-testid*="price"]')
                                if price_elem:
                                    product_info['price'] = price_elem.text.strip()
                                
                                # Look for link
                                link_elem = parent.query_selector('a')
                                if link_elem:
                                    href = link_elem.get_attribute('href')
                                    if href:
                                        if href.startswith('/'):
                                            href = 'https://www.nike.com' + href
                                        product_info['url'] = href
                        except Exception as e:
                            print(f"    ⚠️ Could not extract additional details: {e}")
                        
                        products.append(product_info)
            else:
                print(f"❌ No results found for: {search_term}")
            
            sb.sleep(2)
            
        except Exception as e:
            print(f"❌ Error during scraping: {e}")
            # Take screenshot if enabled
            try:
                sb.cdp.save_screenshot("nike_error.png")
                print("📸 Error screenshot saved as nike_error.png")
            except:
                pass
    
    return products

def save_results_to_csv(products, filename="nike_products.csv"):
    """
    Save scraping results to CSV file.
    
    Args:
        products (list): List of product dictionaries
        filename (str): Output filename
    """
    try:
        import pandas as pd
        df = pd.DataFrame(products)
        df.to_csv(filename, index=False)
        print(f"💾 Results saved to {filename}")
    except ImportError:
        print("⚠️ pandas not available - saving as text file")
        with open(filename.replace('.csv', '.txt'), 'w') as f:
            for product in products:
                f.write(f"{product}\n")

if __name__ == "__main__":
    # Example usage
    print("🚀 Starting Nike scraping with CDP mode...")
    
    # Allow command line argument for search term
    search_term = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        results = scrape_nike_products(search_term)
        
        if results:
            print(f"\n📊 Scraped {len(results)} products successfully!")
            
            # Save results
            save_results_to_csv(results)
            
        print("✅ Scraping completed.")
        
    except KeyboardInterrupt:
        print("\n⏹️ Scraping interrupted by user")
    except Exception as e:
        print(f"\n❌ Scraping failed: {e}")
        sys.exit(1)