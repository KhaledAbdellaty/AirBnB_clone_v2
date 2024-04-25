#!/usr/bin/python3
"""A Flask web application.

runs on host=0.0.0.0, port=5000"""
from flask import Flask, render_template
from models import storage, state

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_route():
    """This route that displays HTML page with dynamic data"""
    states = storage.all(state.State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tearDown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
