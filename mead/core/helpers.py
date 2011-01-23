from mead import app
from flask import g
from flaskext.themes import get_theme


@app.before_request
def get_my_theme():
	g.theme = get_theme(app.config['THEME'])