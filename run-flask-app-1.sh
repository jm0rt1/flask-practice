#!/bin/bash

# Navigate to the src directory
cd "src"
# Activate the virtual environment
source venv/bin/activate

# Set the PYTHONPATH to include the src directory
export PYTHONPATH=$(pwd)

# Run the Flask application
python flask_app_1/app.py &

# Function to check if the Flask app is running
check_flask_app() {
    curl --output /dev/null --silent --head --fail http://127.0.0.1:5000
}

# Wait until the Flask app is running
until check_flask_app; do
    echo "Waiting for Flask app to start..."
    sleep 1
done

# Open the Flask application in Safari
open -a "Safari" http://127.0.0.1:5000/