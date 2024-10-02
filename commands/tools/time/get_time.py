from datetime import datetime

def get_time(secs):
    mins, secs = divmod(secs, 60)
    hrs, mins = divmod(mins, 60)
    return f"{int(hrs)} hrs, {int(mins)} mins, {secs:.2f} secs"