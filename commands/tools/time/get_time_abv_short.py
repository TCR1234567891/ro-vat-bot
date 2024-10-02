from datetime import datetime

def get_time_abv_short(secs):
    mins, secs = divmod(secs, 60)
    hrs, mins = divmod(mins, 60)
    return f"{int(hrs)}h {int(mins)}m"