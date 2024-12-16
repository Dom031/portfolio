from flask import Flask, render_template # Importing the Flask modules
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', "GET"])
def submit_form():
    print("Form submission received!")  # Debugging output
    return 'Form submitted'
