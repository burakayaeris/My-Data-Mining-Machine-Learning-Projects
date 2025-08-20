"""
Basic CDP Mode Example for Undetected Web Scraping
Based on SeleniumBase CDP mode examples

This demonstrates the basic setup and usage of CDP mode for bypassing
bot detection systems.
"""

from seleniumbase import SB

def basic_cdp_example():
    """
    Basic example of using CDP mode for undetected browsing.
    """
    with SB(uc=True, test=True, locale="en") as sb:
        # Example with a basic website
        url = "https://gitlab.com/users/sign_in"
        
        # Activate CDP mode - disconnects WebDriver, uses CDP for stealth
        sb.activate_cdp_mode(url)
        sb.sleep(1)
        
        # Handle CAPTCHA if present (uses PyAutoGUI for human-like interaction)
        sb.uc_gui_click_captcha()
        
        # Basic assertions to verify page loaded correctly
        sb.cdp.assert_text("Username", '[for="user_login"]', timeout=3)
        sb.cdp.assert_element('label[for="user_login"]')
        
        # Highlight elements (useful for debugging)
        sb.cdp.highlight('button:contains("Sign in")')
        sb.cdp.highlight('h1:contains("GitLab.com")')
        
        # Display success message
        sb.post_message("SeleniumBase wasn't detected", duration=4)
        
        print("✅ Successfully accessed GitLab without being detected!")

def advanced_scraping_example():
    """
    More advanced example with form interaction and data extraction.
    """
    with SB(uc=True, test=True, locale="en", ad_block=True) as sb:
        url = "https://www.bestwestern.com/en_US.html"
        sb.activate_cdp_mode(url)
        sb.sleep(2.5)
        
        # Handle cookie consent
        sb.cdp.click_if_visible(".onetrust-close-btn-handler")
        sb.sleep(1)
        
        # Click on destination input
        sb.cdp.click("input#destination-input")
        sb.sleep(2)
        
        # Enter location
        location = "Palm Springs, CA, USA"
        sb.cdp.press_keys("input#destination-input", location)
        sb.sleep(1)
        
        # Select from suggestions
        sb.cdp.click("ul#google-suggestions li")
        sb.sleep(1)
        
        # Click search button
        sb.cdp.click("button#btn-modify-stay-update")
        sb.sleep(4)
        
        # Filter for available hotels
        sb.cdp.click("label#available-label")
        sb.sleep(2.5)
        
        print("Best Western Hotels in %s:" % location)
        
        # Extract hotel information
        summary_details = sb.cdp.get_text("#summary-details-column")
        dates = summary_details.split("DESTINATION")[-1]
        dates = dates.split(" CHECK-OUT")[0].strip() + " CHECK-OUT"
        dates = dates.replace("  ", " ")
        print("(Dates: %s)" % dates)
        
        # Get hotel cards and extract information
        flip_cards = sb.cdp.select_all(".flipCard")
        for i, flip_card in enumerate(flip_cards):
            hotel = flip_card.query_selector(".hotelName")
            price = flip_card.query_selector(".priceSection")
            if hotel and price:
                print("* %s: %s => %s" % (
                    i + 1, hotel.text.strip(), price.text.strip())
                )

if __name__ == "__main__":
    print("=== Basic CDP Mode Example ===")
    basic_cdp_example()
    
    print("\n=== Advanced Scraping Example ===")
    try:
        advanced_scraping_example()
    except Exception as e:
        print(f"Advanced example failed: {e}")
        print("This is normal - some sites may block or require additional setup")