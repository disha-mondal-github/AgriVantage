from app import create_app

app = create_app()  # Initialize the app using the factory function

if __name__ == "__main__":
    app.run(debug=True)
