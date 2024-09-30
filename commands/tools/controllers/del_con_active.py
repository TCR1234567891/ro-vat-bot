import sqlite3
import time


def del_con_active(user, position):
    user_str = str(user)
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute('SELECT *, rowid FROM con_active')
    cont = c.fetchall()
    found_con = list(cont)
    c.execute('DELETE FROM con_active WHERE userid = ?', (user_str,))
    c.execute('SELECT *, rowid FROM con_history WHERE userid = ?', (user_str,))
    thistory = c.fetchone()
    if thistory is None:
        c.execute('INSERT INTO con_history (userid, s1time, s2time, c1time) VALUES (?, ?, ?, ?)', (user, 0, 0, 0))
        c.execute('SELECT *, rowid FROM con_history WHERE userid = ?', (user_str,))
        thistory = c.fetchone()
    found_history = list(thistory)
    if position.endswith("_CTR"):
        elapsed_time = time.time() - float(found_con[0][2])
        found_history[3] = float(found_history[3]) + elapsed_time
        c.execute('UPDATE con_history SET c1time = ? WHERE userid = ?',(found_history[3],user))
    elif position.endswith("_TWR"):
        elapsed_time = time.time() - float(found_con[0][2])
        found_history[2] = float(found_history[2]) + elapsed_time
        c.execute('UPDATE con_history SET s2time = ? WHERE userid = ?',(found_history[2],user))
    else:
        elapsed_time = time.time() - float(found_con[0][2])
        found_history[1] = float(found_history[1]) + elapsed_time
        c.execute('UPDATE con_history SET s1time = ? WHERE userid = ?',(found_history[1],user))
    conn.commit()
    conn.close() 