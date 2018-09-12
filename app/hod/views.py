from flask import abort, render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from .. import db
from ..models import *
from . import hod

def check_admin():
    if not current_user.is_admin:
        abort(403)

@hod.route('/index')
def admin_index():
	#check_admin()
	return render_template('/hod/hod_index.html')

@hod.route('/logout')
@login_required
def hod_logout():

    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))