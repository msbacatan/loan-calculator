# test project, app.py
# Emily Bacatan 10/23/2020

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emily')
def emily():
    return render_template('emily.html')

if __name__ == '__main__':
    app.run(debug=True)
