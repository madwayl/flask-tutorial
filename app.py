from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    { 'id': 1, 'title': 'Frontend Engineer', 'location': 'Remote', 'salary': 'Rs. 22,00,000' },
    { 'id': 2, 'title': 'Backtend Engineer', 'location': 'Remote', 'salary': 'Rs. 22,00,000' },
    { 'id': 3, 'title': 'Devend Engineer', 'location': 'Remote', 'salary': 'Rs. 15,00,000' },
    { 'id': 3, 'title': 'IT Engineer', 'location': 'In-Office, San Francisco', 'salary': 'Rs. 13,00,000' },
]

@app.route("/")
def index():
    return render_template('home.html', name='Careers', jobs=JOBS)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)