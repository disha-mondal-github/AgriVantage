from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/resources')
def resources():
    return render_template('resources.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        access_key = request.form.get('access_key')  # This will be your API key

        # Here you can process the data or send it to the API
        # For example, you can send a POST request to the Web3Forms API

        # For this example, just return a success message
        return jsonify(success=True, message=f'Message from {name} received!')

    return render_template('contact.html')  # Handle GET requests
