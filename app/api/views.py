from flask_restful import Api, Resource
from . import api, rest
from .. import db
from ..models import Schedule, Student, Attendance
from datetime import datetime

class Faculty_Schedule(Resource):
	"""docstring for Note"""
	def get(self, faculty_id):
		today_date = datetime.now().date()
		today_classes = Schedule.query.filter_by(faculty_id=faculty_id).filter_by(date_and_time=today_date).all()
		return {'notes':today_classes}

class Test(Resource):
	def get(self):
		hello = 'wahts up'
		return {'Hello':hello}

class Students(Resource):
	def get(self, batch_code):
		data=[]
		students_list = Student.query.filter_by(batch_code=batch_code).all()
		for a in students_list:
			data.append({
				'roll_no':a.roll_no,
				'name' : a.name
				})

		return {'status':'Good', 'students':data}

	def post(self):

		attendance = {'All details of of attendacne'}

		db.session.add(attendance)
		db.session.commit()
		return {'status': 'Attendace Done'}
class Attendance(Resource):
	def post(self):
		roll_no = request.form['roll_no']
		status = request.form['status']


rest.add_resource(Faculty_Schedule, '/faculty/schedule/<int:faculty_id>')
rest.add_resource(Students, '/students/list/<int:batch_code>')
rest.add_resource(Test, '/test')


#pbkdf2:sha256:50000$g2mwDcDJ$fd6fbb1398217e35b1cca2d5272517ce732c0cc107107b472447defdfbbd76cc