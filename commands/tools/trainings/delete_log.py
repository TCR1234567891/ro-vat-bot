import sqlite3


def delete_log(x,y):
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute("SELECT *, rowid FROM trainingdata WHERE userid = ?",(y,))
    records = c.fetchall()
    conn.close()
    found_username= list(records)
    if x > 0:
        if x <= len(found_username):
            deletion_rowid = str(found_username[x-1][-1])
            if deletion_rowid:
                conn = sqlite3.connect("serverdata.db")
                c = conn.cursor()
                c.execute("DELETE from trainingdata WHERE rowid = ?",(deletion_rowid,))
                conn.commit()
                conn.close()
                return False
            else:
                return True
        else:
            return True
    else:
        return True