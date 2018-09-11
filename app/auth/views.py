from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from .. import db
from ..models import Faculty
from . import auth
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		faculty = Faculty.query.filter_by(username=form.username.data).first()
		if faculty is not None and faculty.verify_password(form.password.data):
			login_user(user):
			if faculty.username = 'ithod':
				return redirect(url_for('hod.index'))
			else:
				return redirect(url_for('faculty.index'))
		else:
			flash('Invalid email or password.')

	return render_template('auth/login.html', form=form)