#!/usr/bin/python3
"""script that is starting web flask application"""

from models import storage
from flask import render_template, Flask
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    sorted_states=sorted(states.values(),key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
