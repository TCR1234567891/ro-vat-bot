import sqlite3


from simply_wisconsin_bot.commands.shared import DB_PATH
def check_con_active(user_id):
    conn = sqlite3.connect("DB_PATH")
    c = conn.cursor()
    c.execute('SELECT *, rowid FROM con_active WHERE userid = ?',(user_id,))
    cont = c.fetchone()
    found_con = list(cont)
    conn.close() 
    return found_con
