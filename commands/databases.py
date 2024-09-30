import sqlite3

def init():
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()

    # Pilot Data (pilotdata)
    c.execute("CREATE TABLE IF NOT EXISTS pilotdata (userid text, q1 text, q2 text, q3 text, q4 text, q5 text, q6 text, q7 text, q8 text, q9 text, q10 text, q11 text, q12 text, passfail text, graded text)")
    # Flight Plan (fplan)
    c.execute("CREATE TABLE IF NOT EXISTS fplan (userid text, igcallsign text, callsign text, actype text, route text, cruise text, timestamp text)")
    # Active Controllers (con_active)
    c.execute("CREATE TABLE IF NOT EXISTS con_active (userid text, pos text, time_start text)")
    # Controller History (con_history)
    c.execute("CREATE TABLE IF NOT EXISTS con_history (userid text, s1time text, s2time text, c1time text)")
    # Weather Data (wxdata)
    c.execute("CREATE TABLE IF NOT EXISTS wxdata (winddirection text, windspeed text, visibility text, cloudalt text, cloudtype text, temp text, dew text, altimeter text)")
    # ATIS Data (atisdata)
    c.execute("CREATE TABLE IF NOT EXISTS atisdata (icao text, letter text, direction text, remarks text, time text)")
    # Training History (trainingdata)
    c.execute("CREATE TABLE IF NOT EXISTS trainingdata (userid text, trainingtype text, instructor text, datetime text, passfail INTEGER)")
    conn.commit()
    conn.close()