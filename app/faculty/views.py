from flask import abort, render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from .. import db
from ..models import *
from . import faculty

@faculty.route('/')
@faculty.route('/index')
def index():
	return render_template('/faculty/index.html')

@faculty.route('/logout')
@login_required
def logout():

    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))