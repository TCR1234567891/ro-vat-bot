import sqlite3
import interactions
from ..tools.atis.fetch_atis import fetch_atis
import data
import pytz
from datetime import datetime

utc_timezone = pytz.UTC


def event_end():
    global atis_updated
    conn = sqlite3.connect('serverdata.db')
    c = conn.cursor()
    c.execute('DELETE FROM atisdata;')
    c.execute('DELETE FROM wxdata;')
    c.execute('DELETE FROM con_active')
    conn.commit()
    conn.close()
    atis_updated = False

@interactions.slash_command(
    name="end_event",
    description="End the currently active event",
    dm_permission=False)
async def hande_end_event(ctx: interactions.SlashContext):
    print("Command run: /end_event")
    global bot_instance
    current_atis = fetch_atis()
    if data.event_active == True or fetch_atis is not None:
        data.event_active = False
        event_end()
        current_time = datetime.now(utc_timezone).strftime("%H:%MZ")
        embed = interactions.Embed(
            description=f"Event successfully ended at {current_time}",
            color= interactions.Color.from_rgb(0, 57, 153))
        await ctx.send(embed=embed)
        channel = await bot_instance.fetch_channel(data.event_channel_id)
        messages = channel.history(limit=1)
        async for message in messages:
            await message.delete()
    else:
        error_embed = interactions.Embed( 
            description=f"There is no active event to end, please try again during an event",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        
def setup(bot):
    global bot_instance
    bot_instance = bot
    print("Registered /end_event successfully")
    bot.add_command(hande_end_event)