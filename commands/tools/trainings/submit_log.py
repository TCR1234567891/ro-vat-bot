import sqlite3

from simply_wisconsin_bot.commands.shared import DB_PATH
def submit_log(userid,training_type,auth_id,command_time,grade_int):
	conn = sqlite3.connect("DB_PATH")
	c = conn.cursor()
	c.execute("INSERT INTO trainingdata (userid, trainingtype, instructor, datetime, passfail) VALUES (?, ?, ?, ?, ?)",(userid,training_type,auth_id,command_time,grade_int))
	conn.commit()
	conn.close()
