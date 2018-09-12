from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db, login_manager

class Faculty(UserMixin, db.Model):
	__tablename__ = 'faculty'

	faculty_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), index=True, unique=True)
	name = db.Column(db.String(50))
	password_hash = db.Column(db.String(128))
	#schedule = db.relationship('Schedule', backref = 'faculty_schedule', lazy='dynamic')

	@property
	def password(self):

		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):

		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):

		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User: {}>'.format(username)

@login_manager.user_loader
def load_user(faculty_id):
    return Faculty.query.get(int(faculty_id))

class Batches(db.Model):
	__tablename__ = 'batches'

	batch_code = db.Column(db.Integer, primary_key=True)
	section = db.Column(db.String(2))
	semester = db.Column(db.Integer)
	#students_list = db.relationship('Student', backref='batch_student', lazy='dynamic')
	#faculty_list = db.relationship('Faculty', backref='batch_faculty', lazy='dynamic')

	def __repr__(self):
		return '<Batch: {}>'.format(section)

class Student(db.Model):
	__tablename__ = 'students'

	roll_no = db.Column(db.Integer, primary_key=True)
	batch_code = db.Column(db.Integer, db.ForeignKey('batches.batch_code'))
	name = db.Column(db.String(50))

	def __repr__(self):
		return '<Student: {}>'.format(roll_no)

class Schedule(db.Model):

	__tablename__ = 'schedule'
	weekday_temp = datetime.now().weekday()
	schedule_id = db.Column(db.Integer, primary_key=True)
	week_no = db.Column(db.Integer)
	weekday = db.Column(db.Integer, default=weekday_temp)
	batch_code = db.Column(db.Integer, db.ForeignKey('batches.batch_code'))
	period_number = db.Column(db.Integer)
	faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.faculty_id'))
	subject = db.Column(db.String(5))

	def __repr__(self):
		return '<Week | Period No. : {}>'.format(week_no, period_number)


class Attendance(db.Model):
	__tablename__ = 'attendance'

	weekday_temp = datetime.now().weekday()
	date_temp = datetime.now()
	attendance_id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime, default=date_temp.date)
	week_no = db.Column(db.Integer)
	weekday = db.Column(db.Integer, default=weekday_temp)
	period_number = db.Column(db.Integer)
	faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.faculty_id'))
	roll_no = db.Column(db.Integer, db.ForeignKey('students.roll_no'))
	status = db.Column(db.String(2))

	def __repr__(self):
		return '<Roll No | Status : {}>'.format(roll_no, status)