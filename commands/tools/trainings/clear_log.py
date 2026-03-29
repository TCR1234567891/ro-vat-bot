import sqlite3


from simply_wisconsin_bot.commands.shared import DB_PATH
def clear_log(x):
    conn = sqlite3.connect("DB_PATH")
    c = conn.cursor()
    c.execute("DELETE from trainingdata WHERE userid = ?",(x,))
    conn.commit()
    conn.close()
