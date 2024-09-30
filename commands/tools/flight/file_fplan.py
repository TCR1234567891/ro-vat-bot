import sqlite3


def file_fplan(user_id, igcallsign, callsign, actype, route, cruise, command_time):
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute("INSERT INTO fplan (userid, igcallsign, callsign, actype, route, cruise, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, igcallsign, callsign, actype, route, cruise, command_time))
    conn.commit()
    conn.close()
