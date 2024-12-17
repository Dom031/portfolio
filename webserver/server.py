from flask import Flask, render_template, request # Importing the Flask modules
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return 'form submitted'
    else:
        return 'something went wrong'