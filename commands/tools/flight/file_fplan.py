import sqlite3


from simply_wisconsin_bot.commands.shared import DB_PATH
def file_fplan(user_id, igcallsign, callsign, actype, route, cruise, command_time):
    conn = sqlite3.connect("DB_PATH")
    c = conn.cursor()
    c.execute("INSERT INTO fplan (userid, igcallsign, callsign, actype, route, cruise, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, igcallsign, callsign, actype, route, cruise, command_time))
    conn.commit()
    conn.close()

