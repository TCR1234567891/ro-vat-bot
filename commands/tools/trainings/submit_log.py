import sqlite3

def submit_log(userid,training_type,auth_id,command_time,grade_int):
	conn = sqlite3.connect("serverdata.db")
	c = conn.cursor()
	c.execute("INSERT INTO trainingdata (userid, trainingtype, instructor, datetime, passfail) VALUES (?, ?, ?, ?, ?)",(userid,training_type,auth_id,command_time,grade_int))
	conn.commit()
	conn.close()