import sqlite3


from simply_wisconsin_bot.commands.shared import DB_PATH
def fetch_metar():
    conn = sqlite3.connect("DB_PATH")
    c = conn.cursor()
    c.execute('SELECT * FROM wxdata WHERE rowid = 1')
    wxresult = c.fetchone()
    found_wx = list(wxresult)
    conn.close()
    return found_wx
