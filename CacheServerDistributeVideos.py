from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)


@app.route('/test')
def test():
    return 'Test app working!'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
