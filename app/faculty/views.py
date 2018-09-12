from flask import abort, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from datetime import datetime
from ..sql_queries import *
import sqlite3

from .. import db
from ..models import *
from . import faculty
from .forms import *

def query_attendance(section,from_date,to_date):
	with sqlite3.connect('instance/app.db') as conn:
		l=list()
		cur = conn.cursor()
		from_date = from_date + ' 00:00:00.000000'
		to_date = to_date + '00:00:00.000000'
		query = "select * from attendance where date between {0} and {1} ".format(from_date,to_date)
		cur.execute(query)
		data = cur.fetchall()
		conn.close()
	return data

@faculty.route('/')
@faculty.route('/index')
def index():
	return render_template('/faculty/index.html')

@faculty.route('/attendance', methods=['GET', 'POST'])
def get_attendance():
	current_date = datetime.now()
	form = GetStudentsAttendance()
	if form.validate_on_submit():
		section = form.section.data
		date_from = form.datefrom.data.strftime('%Y-%m-%d')
		date_to = form.dateto.data.strftime('%Y-%m-%d')
		print(query_attendance(section,date_from,date_to))

	return render_template('/faculty/get_attendance.html',form=form, students = None)

@faculty.route('/addstudents')
def add_students():
	form = AddClass()
	if form.validate_on_submit():
		file = form.excel_file.data
	return render_template('/faculty/add_class.html',form=form)

@faculty.route('/logout')
@login_required
def logout():

    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))