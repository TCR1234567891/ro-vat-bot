import interactions
import data
from datetime import datetime
import pytz
from ..tools.controllers.check_con_active import check_con_active
from ..tools.controllers.del_con_active import del_con_active

utc_timezone = pytz.UTC


@interactions.slash_command(
    name="log_off",
    description="Log off from a controller position")
async def handle_log_off(ctx: interactions.SlashContext):
    print("Command run: /log_off")
    sent_channel = ctx.channel.id
    sent_user = ctx.author.id
    if sent_channel != data.ccmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1257053360285159534 (where you can obtain ATIS).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        return
    if data.event_active == True:
        con_data = check_con_active(sent_user)
        current_time = datetime.now(utc_timezone).strftime("%H:%MZ")
        if con_data:
            del_con_active(sent_user, con_data[1])
            embed = interactions.Embed(
                description=f"Successfully logged off from {con_data[1]} at {current_time}",
                color= interactions.Color.from_rgb(0, 57, 153))
            await ctx.send(embed=embed)
            channel = await ctx.bot.fetch_channel(data.event_channel_id)
            event_message = await channel.fetch_message(data.event_message_id)
            updated_embed = event_message.embeds[0]
            username_to_remove = ctx.author.mention
            description_lines = updated_embed.description.split('\n')
            updated_lines = [line for line in description_lines if username_to_remove not in line]
            updated_description = '\n'.join(updated_lines)
            updated_embed.description = updated_description
            await event_message.edit(embed=updated_embed)
        else:
            error_embed = interactions.Embed( 
            description=f"You aren't currently logged on as a controller, please log on before logging off",
            color= interactions.Color.from_rgb(221, 53, 53))
            await ctx.send(embed=error_embed,ephemeral=True)
    else:
        error_embed = interactions.Embed( 
            description=f"There is no active event, please try again during an event",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        
def setup(bot):
    print("Registered /log_off successfully")
    bot.add_command(handle_log_off)