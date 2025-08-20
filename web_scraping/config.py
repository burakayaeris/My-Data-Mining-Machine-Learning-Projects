# Web Scraping Configuration
# 
# This file contains default settings for SeleniumBase CDP mode scraping
# Modify these values to customize scraping behavior

# Browser Settings
HEADLESS = False  # Set to True for production/server environments
USER_AGENT = "auto"  # Let SeleniumBase choose optimal user agent
BROWSER_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--disable-dev-shm-usage",
    "--no-sandbox"
]

# Timing Settings (in seconds)
DEFAULT_DELAY = 2.5  # Default delay between actions
PAGE_LOAD_TIMEOUT = 30  # Max time to wait for page loads
ELEMENT_TIMEOUT = 10  # Max time to wait for elements

# CDP Mode Settings
UC_MODE = True  # Always use undetected Chrome mode
TEST_MODE = True  # Enable test mode features
LOCALE = "en"  # Browser locale
AD_BLOCK = True  # Enable ad blocking for faster loading

# Retry Settings
MAX_RETRIES = 3  # Number of retry attempts for failed requests
RETRY_DELAY = 5  # Delay between retry attempts

# Output Settings
SAVE_SCREENSHOTS = False  # Save screenshots on errors
SCREENSHOT_DIR = "screenshots"  # Directory for screenshots
LOG_LEVEL = "INFO"  # Logging level (DEBUG, INFO, WARNING, ERROR)

# Example-specific settings
NIKE_SEARCH_DELAY = 4  # Extra delay for Nike search results
NIKE_DEFAULT_SEARCH = "Nike Air Force 1"  # Default search term