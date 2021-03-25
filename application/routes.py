from flask import current_app as app
from flask import redirect, url_for


@app.route('/', methods=('GET', 'POST'))
def index():
    text = 'hi'

    return text


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))
