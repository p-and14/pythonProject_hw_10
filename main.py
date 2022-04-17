from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates_list = import_candidates("candidates.json")

    return withdraws_candidates(candidates_list)


@app.route("/candidates/<int:uid>")
def candidates(uid):
    candidates_list = import_candidates("candidates.json")
    candidate = search_candidate_id(candidates_list, uid)

    return f'<img src={candidate[0]["picture"]}\n>' + withdraws_candidates(candidate)


@app.route("/skills/<skill>")
def skills(skill):
    candidates_list = import_candidates("candidates.json")
    candidates_with_skill = search_skills(candidates_list, skill)

    return withdraws_candidates(candidates_with_skill)


app.run()
