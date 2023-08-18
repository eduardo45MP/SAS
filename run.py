from app import app  # Import the Flask app instance from the app module
import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Start the Flask development server
