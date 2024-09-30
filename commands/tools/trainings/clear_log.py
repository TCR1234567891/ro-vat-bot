import sqlite3


def clear_log(x):
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute("DELETE from trainingdata WHERE userid = ?",(x,))
    conn.commit()
    conn.close()