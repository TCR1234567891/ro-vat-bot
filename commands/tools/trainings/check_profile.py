import interactions
import sqlite3

def check_profile(y):
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor() 
    c.execute("SELECT *, rowid FROM trainingdata")
    records = c.fetchall()
    found_username= []
    for record in records:
        string_query = str(y)
        if string_query == record[0]:
            found_username.append(record)
    c.execute("SELECT *, rowid FROM con_history WHERE userid = ?",(str(y),))
    tup_history = c.fetchone()
    found_history = list(tup_history) if tup_history != None else ["nill",0,0,0]
    conn.close()
    found_data = [found_username, found_history]
    return found_data