import sqlite3
import data
import json


from simply_wisconsin_bot.commands.shared import DB_PATH
def fetch_atis():
    conn = sqlite3.connect('DB_PATH')
    c = conn.cursor()
    c.execute("SELECT * FROM atisdata")
    found_atist = c.fetchall()
    found_atis = list(found_atist)
    conn.close()
    if found_atis != []:
        for airport in found_atis:
            airport = list(airport)
            json_data = airport[2]
            airport[2] = json.loads(json_data)
        return found_atis
    else:
        return None
