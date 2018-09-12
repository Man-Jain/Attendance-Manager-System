import sqlite3

conn = sqlite3.connect('instance/app.db')

def query_attendance(section,from_date,to_date,):
	l=list()
	cur = conn.cursor()
	from_date = from_date + ' 00:00:00.000000'
	to_date = to_date + '00:00:00.000000'
	query = "select * from students where date between {} and {} and section={}".format(from_date, to_date,section)
	cur.execute(query)
	data = cur.fetchall()
	l.extend(data)
	conn.close()
	return l
