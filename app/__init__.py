from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

def create_app():
    app = Flask(__name__)
    
    # Get API key from environment variable
    app.config['ACCESS_KEY'] = os.getenv('ACCESS_KEY')

    # Import the routes from the routes.py file
    from .routes import main
    app.register_blueprint(main)  # Registering the main blueprint

    return app
