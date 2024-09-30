import sqlite3
import random
import json

def event_start():
    global atis_updated
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor() 
    c.execute("SELECT *, rowid FROM atisdata")
    atis_records = c.fetchall()
    c.execute("SELECT *, rowid FROM wxdata")
    wx_records = c.fetchall()
    conn.close()
    if atis_records:
        hosted_success = False
        atis_updated = True
        return hosted_success
    else:
        conn = sqlite3.connect("serverdata.db")
        c = conn.cursor()
        nill = ["Nill"]
        wxtype = ["CLR","SCT"]
        json_data = json.dumps(nill)
        row_id = 1
        idirection = random.randrange(10,360,10)
        if idirection < 100:
            direction = "0"+str(idirection)
        else:
            direction = str(idirection)
        speed = str(random.randint(0,20))
        vis = str(random.randint(5,10))
        ialt = random.randrange(10,50,5)
        alt = "0"+str(ialt)
        cloud = random.choice(wxtype)
        itemp = random.randint(15,30)
        temperature = str(itemp)
        dewpoint = str(itemp - random.randint(2,10))
        alti = str(random.randint(2980,3010))
        if wx_records == []:
            c.execute("""
            INSERT INTO wxdata (winddirection, windspeed, visibility, cloudalt, cloudtype, temp, dew, altimeter) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (direction, speed, vis, alt, cloud, temperature, dewpoint, alti))
        else:
            c.execute("""
            UPDATE wxdata SET winddirection = ?, windspeed = ?, visibility = ?, cloudalt = ?, cloudtype = ?, temp = ?, dew = ?, altimeter = ? WHERE rowid = ?
                """, (direction, speed, vis, alt, cloud, temperature, dewpoint, alti, row_id))
        conn.commit()
        conn.close()
        hosted_success = True
        return hosted_success