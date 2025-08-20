#!/usr/bin/env python3
"""
Setup Script for Web Scraping with SeleniumBase CDP Mode
This script installs and configures everything needed for undetected web scraping.
"""

import subprocess
import sys
import os

def run_command(command, description=""):
    """Run a command and handle errors."""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed")
        print(f"Error: {e.stderr}")
        return False

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing web scraping dependencies...")
    
    # Upgrade pip first
    run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip")
    
    # Install from requirements.txt if it exists
    if os.path.exists("requirements.txt"):
        run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing from requirements.txt")
    else:
        # Install core dependencies manually
        dependencies = [
            "seleniumbase>=4.39.6",
            "nodriver",
            "pyvirtualdisplay", 
            "pdbp",
            "tabcompleter",
            "sbvirtualdisplay",
            "pandas",
            "numpy",
            "matplotlib"
        ]
        
        for dep in dependencies:
            run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}")

def setup_seleniumbase():
    """Set up SeleniumBase browser drivers."""
    print("🌐 Setting up SeleniumBase browser drivers...")
    
    # Install browser drivers
    run_command("seleniumbase install chromedriver", "Installing ChromeDriver")
    run_command("seleniumbase install geckodriver", "Installing GeckoDriver")

def verify_installation():
    """Verify the installation by running a simple test."""
    print("🧪 Verifying installation...")
    
    test_script = '''
from seleniumbase import SB
import sys

try:
    print("Testing SeleniumBase import... ✅")
    
    # Test basic SB functionality
    with SB(uc=True, test=True, headless=True) as sb:
        sb.open("https://www.example.com")
        title = sb.get_title()
        print(f"Successfully loaded page: {title} ✅")
    
    print("All tests passed! 🎉")
    sys.exit(0)
    
except Exception as e:
    print(f"Verification failed: {e} ❌")
    sys.exit(1)
'''
    
    with open("test_setup.py", "w") as f:
        f.write(test_script)
    
    success = run_command(f"{sys.executable} test_setup.py", "Running verification test")
    
    # Clean up test file
    if os.path.exists("test_setup.py"):
        os.remove("test_setup.py")
    
    return success

def create_example_runner():
    """Create a script to easily run examples."""
    runner_script = '''#!/usr/bin/env python3
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
    spec.loader.exec_module(module)
    
    return True

def main():
    """Main function."""
    examples = list_examples()
    
    if len(sys.argv) < 2:
        print("Available examples:")
        for i, example in enumerate(examples, 1):
            print(f"  {i}. {example}")
        print(f"\\nUsage: python {sys.argv[0]} <example_name>")
        return
    
    example_name = sys.argv[1]
    if example_name not in examples:
        print(f"Example '{example_name}' not found!")
        print("Available examples:", ", ".join(examples))
        return
    
    run_example(example_name)

if __name__ == "__main__":
    main()
'''
    
    with open("run_examples.py", "w") as f:
        f.write(runner_script)
    
    # Make it executable on Unix systems
    if os.name != 'nt':
        os.chmod("run_examples.py", 0o755)

def main():
    """Main setup function."""
    print("🎯 Setting up Web Scraping with SeleniumBase CDP Mode")
    print("=" * 60)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        return False
    
    # Setup SeleniumBase
    if not setup_seleniumbase():
        print("❌ Failed to setup SeleniumBase")
        return False
    
    # Verify installation
    if not verify_installation():
        print("❌ Installation verification failed")
        return False
    
    # Create example runner
    create_example_runner()
    
    print("🎉 Setup completed successfully!")
    print("📝 You can now run examples using: python run_examples.py <example_name>")
    print("📁 Examples are located in: web_scraping/examples/")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)