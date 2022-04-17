from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    withdraws_all_candidates()
    return withdraws_all_candidates()


@app.route("/candidates/<int:uid>")
def candidates(uid):
    """
    <img src="(ссылка на картинку)">
    <pre>
      Имя кандидата -
      Позиция кандидата
      Навыки через запятую
    </pre>
    """
    candidates = import_candidates()
    return f"Профиль пользователя {candidates[uid]}"


# @app.route("/feed/")
# def page_feed():
#     return "Лента пользователя"
#
#
# @app.route("/messages/")
# def page_messages():
#     return "Сообщения пользователя"
#
#
# @app.route('/users/<uid>')
# def profile(uid):
#     return f'<h1>Профиль {uid}</h1>'
#
#
# @app.route('/catalog/items/<itemid>')
# def catalog(itemid):
#     return f'<h1>Страничка товара {itemid}</h1>'
#
#
app.run()
