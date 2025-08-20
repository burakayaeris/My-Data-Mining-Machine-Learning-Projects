#!/usr/bin/env python3
"""
Example Runner for Web Scraping Scripts
Usage: python run_examples.py [example_name]
"""

import sys
import os
import importlib.util

def list_examples():
    """List available examples."""
    examples_dir = "web_scraping/examples"
    if not os.path.exists(examples_dir):
        print("No examples directory found!")
        return []
    
    examples = []
    for file in os.listdir(examples_dir):
        if file.endswith(".py") and not file.startswith("__"):
            examples.append(file[:-3])  # Remove .py extension
    
    return examples

def run_example(example_name):
    """Run a specific example."""
    examples_dir = "web_scraping/examples"
    example_path = os.path.join(examples_dir, f"{example_name}.py")
    
    if not os.path.exists(example_path):
        print(f"Example '{example_name}' not found!")
        return False
    
    print(f"🚀 Running example: {example_name}")
    print("-" * 50)
    
    # Import and run the example
    spec = importlib.util.spec_from_file_location(example_name, example_path)
    module = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"❌ Error running example: {e}")
        return False
    
    return True

def main():
    """Main function."""
    examples = list_examples()
    
    if len(sys.argv) < 2:
        print("Available examples:")
        for i, example in enumerate(examples, 1):
            print(f"  {i}. {example}")
        print(f"\nUsage: python {sys.argv[0]} <example_name>")
        return
    
    example_name = sys.argv[1]
    if example_name not in examples:
        print(f"Example '{example_name}' not found!")
        print("Available examples:", ", ".join(examples))
        return
    
    run_example(example_name)

if __name__ == "__main__":
    main()