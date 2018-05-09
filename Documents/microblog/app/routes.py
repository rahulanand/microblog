from app import app
from flask import render_template
from forms import LoginForm
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
	