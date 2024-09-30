from datetime import datetime

def get_time(seconds):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{int(hrs)} hrs, {int(mins)} mins, {secs:.2f} secs"