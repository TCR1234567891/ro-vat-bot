import sqlite3


def check_leaderboard():
    conn = sqlite3.connect("serverdata.db")
    c = conn.cursor()
    c.execute('SELECT * FROM con_history')
    leaderboard = c.fetchall()
    conn.close()
    processed_leaderboard = []
    for leader in leaderboard:
        leader = list(leader)
        try:
            leader[1] = float(leader[1])
            leader[2] = float(leader[2])
            leader[3] = float(leader[3])
        except ValueError:
            continue
        processed_leaderboard.append(leader)
    tuples_with_sums = [(tup, sum(tup[1:4])) for tup in processed_leaderboard]
    sorted_tuples = sorted(tuples_with_sums, key=lambda x: x[1], reverse=True)
    top_three_tuples = sorted_tuples[:3]
    return top_three_tuples