from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)


@app.route('/list.html')
def index():
    candidates = get_all()
    return f'<pre> {candidates} </pre>'


app.run()