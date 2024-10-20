from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    
    try:
        matches = re.findall(regex_pattern, test_string)
        return render_template('results.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)
    except re.error:
        error_message = "Invalid regular expression"
        return render_template('results.html', error=error_message)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = re.match(email_regex, email) is not None
        return render_template('index.html', email=email, is_valid=is_valid)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)