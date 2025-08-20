# Web Scraping with SeleniumBase CDP Mode

This directory contains everything needed to perform undetected web scraping using SeleniumBase CDP (Chrome DevTools Protocol) mode and patterns from the undetected-testing repository.

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run setup script:**
   ```bash
   python setup_scraping.py
   ```

3. **Test with Nike example:**
   ```bash
   python run_examples.py raw_nike
   ```

## 📋 What's Included

### Dependencies
- **seleniumbase>=4.39.6** - Main web automation framework with CDP mode
- **nodriver** - Pure CDP implementation for advanced scenarios  
- **pyvirtualdisplay** - Virtual display for headless environments
- **pdbp** - Enhanced Python debugger
- **tabcompleter** - Tab completion support
- **sbvirtualdisplay** - SeleniumBase virtual display utilities

### Examples
- **raw_nike.py** - Nike website scraping (from undetected-testing repo)
- **cdp_basic_examples.py** - Basic CDP mode usage patterns
- More examples can be added following the same patterns

### Scripts
- **setup_scraping.py** - Automated setup and installation
- **run_examples.py** - Easy way to run scraping examples

## 🔧 How CDP Mode Works

CDP Mode is a special stealth mode that:

1. **Disconnects WebDriver** - Prevents detection by anti-bot systems
2. **Uses Chrome DevTools Protocol** - Direct browser communication
3. **Supports PyAutoGUI** - Human-like CAPTCHA solving
4. **Maintains UC Mode benefits** - Undetected Chrome profile

### Basic Usage Pattern

```python
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", pls="none") as sb:
    # Navigate to target site
    url = "https://example.com"
    sb.activate_cdp_mode(url)  # Enables stealth mode
    
    # Use CDP methods for interaction
    sb.cdp.click("button#search")
    sb.cdp.type("input", "search term")
    
    # Extract data
    elements = sb.cdp.select_all(".result")
    for element in elements:
        print(element.text)
```

## 🛡️ Stealth Features

### Bot Detection Bypass
- **Undetected Chrome** - Modified Chrome profile
- **CDP Communication** - No WebDriver detection
- **Human-like timing** - Realistic delays between actions
- **CAPTCHA handling** - PyAutoGUI integration

### Supported Protection Systems
- Cloudflare
- DataDome  
- Kasada
- Shape Security
- Incapsula/Imperva
- Akamai with PerimeterX

## 📚 Key CDP Methods

### Navigation & Page Control
```python
sb.cdp.get(url)                    # Navigate to URL
sb.cdp.reload()                    # Reload page
sb.cdp.get_title()                 # Get page title
sb.cdp.get_current_url()           # Get current URL
```

### Element Interaction
```python
sb.cdp.click(selector)             # Click element
sb.cdp.type(selector, text)        # Type text
sb.cdp.press_keys(selector, text)  # Human-speed typing
sb.cdp.clear(selector)             # Clear input
```

### Data Extraction
```python
sb.cdp.get_text(selector)          # Get text content
sb.cdp.select_all(selector)        # Get all matching elements
sb.cdp.get_attribute(selector, attr) # Get element attribute
```

### Stealth Methods
```python
sb.cdp.gui_click_element(selector) # PyAutoGUI click
sb.uc_gui_click_captcha()          # Handle CAPTCHAs
sb.cdp.sleep(seconds)              # Human-like delays
```

## 🎯 Advanced Usage

### Handling Complex Sites

```python
from seleniumbase import SB

with SB(uc=True, test=True, locale="en", ad_block=True) as sb:
    url = "https://protected-site.com"
    sb.activate_cdp_mode(url)
    
    # Handle cookie consent
    sb.cdp.click_if_visible(".cookie-accept")
    
    # Wait for dynamic content
    sb.cdp.wait_for_element_visible(".content")
    
    # Extract data with error handling
    try:
        elements = sb.cdp.select_all(".data-item")
        for element in elements:
            # Process each element
            text = element.text.strip()
            if text:
                print(f"Found: {text}")
    except Exception as e:
        print(f"Extraction failed: {e}")
```

### Data Collection Pipeline

```python
def scrape_with_retry(url, max_retries=3):
    """Scrape with retry logic for robustness."""
    for attempt in range(max_retries):
        try:
            with SB(uc=True, test=True, headless=True) as sb:
                sb.activate_cdp_mode(url)
                # Your scraping logic here
                return extract_data(sb)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                raise
    
def extract_data(sb):
    """Extract and structure data."""
    data = []
    elements = sb.cdp.select_all(".item")
    for element in elements:
        item = {
            'title': element.query_selector('.title').text,
            'price': element.query_selector('.price').text,
            'url': element.query_selector('a').get_attribute('href')
        }
        data.append(item)
    return data
```

## ⚠️ Important Notes

### Rate Limiting
- Add delays between requests: `sb.cdp.sleep(2)`
- Respect robots.txt
- Monitor for IP blocks

### Legal Considerations
- Check website terms of service
- Respect copyright and privacy
- Use scraped data responsibly

### Best Practices
- Start with headless mode for production
- Use virtual displays in cloud environments
- Implement proper error handling
- Log scraping activities

## 🔍 Troubleshooting

### Common Issues

1. **Chrome not found**: Install Chrome browser
2. **Permission denied**: Run with appropriate privileges  
3. **CAPTCHA failures**: Adjust timing, try different methods
4. **Detection**: Increase delays, rotate user agents

### Debug Mode
```python
# Enable debug mode for troubleshooting
with SB(uc=True, test=True, debug=True, headless=False) as sb:
    # Your scraping code
    pass
```

## 📖 Resources

- [SeleniumBase CDP Mode Documentation](https://github.com/seleniumbase/SeleniumBase/tree/master/examples/cdp_mode)
- [Undetected Testing Repository](https://github.com/mdmintz/undetected-testing)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)

## 🤝 Contributing

To add new scraping examples:

1. Create a new Python file in `web_scraping/examples/`
2. Follow the existing pattern using CDP mode
3. Include error handling and documentation
4. Test thoroughly before committing

## 📄 License

This setup uses SeleniumBase (MIT License) and follows the same licensing terms.