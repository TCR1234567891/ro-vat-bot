import sqlite3
import time


def update_con_active(airport, user):
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute('SELECT *, rowid FROM con_active')
    cont = c.fetchall()
    found_con = list(cont)
    conn.close() 
    for con_active in found_con:
        if con_active[0] == str(user):
            return 1
        elif con_active[1] == airport:
            return 0
    start_time = time.time()
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO con_active (userid, pos, time_start) VALUES (?, ?, ?)
        """, (user, airport, start_time))
    conn.commit()
    conn.close()
    return 2