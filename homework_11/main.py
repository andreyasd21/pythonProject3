from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    candidate = get_candidate_by_pk(pk)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidate_name(candidate_name):
    candidates = get_candidate_by_name(candidate_name.lower())
    return render_template('search.html', candidates=candidates, count_candidate=len(candidates))


@app.route('/skill/<skill>')
def get_candidate_by_skills(skill):
    candidates = get_candidate_by_skill(skill.lower())
    return render_template('skill.html', skills=candidates, count_candidates=len(candidates))


app.run()
