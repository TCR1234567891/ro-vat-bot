import sqlite3

from simply_wisconsin_bot.commands.shared import DB_PATH
def publish_atis(airport, identifier, rwys, rmks, timestamp):
    global atis_updated
    atis_updated = True
    conn = sqlite3.connect('DB_PATH')
    c = conn.cursor()
    c.execute("SELECT *, rowid FROM atisdata")
    all_atis = c.fetchall()
    for atis in all_atis:
        if airport == atis[0]:
            c.execute("UPDATE atisdata SET icao = ?, letter = ?, direction = ?, remarks = ?, time = ? WHERE rowid = ?", (airport, identifier, rwys, rmks, timestamp, atis[5]))
            conn.commit()
            conn.close()
            return
    c.execute("INSERT INTO atisdata (icao, letter, direction, remarks, time) VALUES (?,?,?,?,?)", (airport, identifier, rwys, rmks, timestamp))
    conn.commit()
    conn.close()
    

