import sqlite3


def check_con_active(user_id):
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute('SELECT *, rowid FROM con_active WHERE userid = ?',(user_id,))
    cont = c.fetchone()
    found_con = list(cont)
    conn.close() 
    return found_con