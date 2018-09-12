from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from wtforms.fields.html5 import DateField

class GetStudentsAttendance(FlaskForm):
	section = StringField('Enter Section', validators=[DataRequired()])
	datefrom = DateField('From Date', validators=[DataRequired()], format='%Y-%m-%d')
	dateto = DateField('To Date', validators=[DataRequired()], format='%Y-%m-%d')
	submit = SubmitField('Submit')

class AddClass(FlaskForm):
	section = StringField('Enter Section Name', validators=[DataRequired()])
	semester = IntegerField('Enter Semester Number', validators=[DataRequired()])
	excel_file = FileField('Enter Student List',validators=[FileRequired()])
	submit = SubmitField('Submit')