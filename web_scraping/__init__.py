"""
Web Scraping Package for SeleniumBase CDP Mode

This package provides tools and examples for undetected web scraping using
SeleniumBase CDP (Chrome DevTools Protocol) mode.

Key Features:
- Bypass bot detection systems
- Handle CAPTCHAs automatically  
- Human-like interaction patterns
- Support for protected websites

Usage:
    from web_scraping.examples.raw_nike import scrape_nike_products
    scrape_nike_products("Nike Air Force 1")
"""

__version__ = "1.0.0"
__author__ = "Data Mining & Machine Learning Projects"

# Import key functions for easy access
try:
    from .examples.raw_nike import scrape_nike_products
except ImportError:
    # Handle case where dependencies aren't installed yet
    pass