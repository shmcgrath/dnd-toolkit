from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sarah'}
    chars = [
        {
            'owner': {'username': 'Mo'},
            'body': 'Level 3 Monk'
        },
        {
            'owner': {'username': 'Jon'},
            'body': 'Level 10 Cleric'
        }
    ]
    return render_template('index.html', title='Home', user=user, chars=chars)
