import sqlite3


def fetch_metar():
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute('SELECT * FROM wxdata WHERE rowid = 1')
    wxresult = c.fetchone()
    found_wx = list(wxresult)
    conn.close()
    return found_wx