"""
Frontend Application

A modern web application built with JavaScript, HTML, and CSS.
"""

import os

# Check if the project is being run from the root directory
if os.getcwd()!= os.path.dirname(os.path.abspath(__file__)):
    print("Error: This script must be run from the project root directory.")
    exit(1)

# Check if the required dependencies are installed
try:
    import frontend_app.dependencies
except ImportError:
    print("Error: Required dependencies are not installed. Run 'pip install -r requirements.txt' to install them.")
    exit(1)

# Run the application
if __name__ == "__main__":
    import frontend_app.main
    frontend_app.main.run()