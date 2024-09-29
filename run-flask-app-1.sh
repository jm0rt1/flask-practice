#!/bin/bash

# Navigate to the src directory
cd "src"
# Activate the virtual environment
source venv/bin/activate

# Set the PYTHONPATH to include the src directory
export PYTHONPATH=$(pwd)
# Set the FLASK_APP environment variable to point to your Flask application
export FLASK_APP=flask_app_1/app.py
# Ensure Flask-Migrate is installed
pip show Flask-Migrate > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing Flask-Migrate..."
    pip install Flask-Migrate
else
    echo "Flask-Migrate is already installed."
fi

# Initialize migrations if not already done
if [ ! -d "migrations" ]; then
    echo "Initializing migrations..."
    flask db init
fi

# Generate and apply migrations
echo "Generating migrations..."
flask db migrate -m "Initial migration."
echo "Applying migrations..."
flask db upgrade

# Create the database (if necessary)
python create_db.py

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