#!/usr/bin/env python3

from flask import Flask
from flask import render_template as template

app = Flask(__name__)

@app.route("/")
def home():
	user = "Akalenga"
	tarefa = [{"titulo": "Estudar Flask", "feito": True},
			{"titulo": "Praticar jinja2", "feito": False},
			{"titulo": "Revisar API RESTs", "feito": False}]
	return template("tarefa.html", user=user, tarefa=tarefa)

if __name__ == "__main__":
	app.run(debug=True)
