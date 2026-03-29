import sqlite3

from simply_wisconsin_bot.commands.shared import DB_PATH
def init():
    conn = sqlite3.connect("DB_PATH")
    c = conn.cursor()

    # Pilot Data (pilotdata)
    c.execute("CREATE TABLE IF NOT EXISTS pilotdata (userid text, q1 text, q2 text, q3 text, q4 text, q5 text, q6 text, q7 text, q8 text, q9 text, q10 text, q11 text, q12 text, passfail text, graded text)")
    conn.commit()
    conn.close()
