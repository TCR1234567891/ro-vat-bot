import interactions
import data
from datetime import datetime
from ..tools.controllers.update_con_active import update_con_active
import pytz

utc_timezone = pytz.UTC


@interactions.slash_command(
    name="log_on",
    description="Log on as a controller",
    dm_permission=False)
@interactions.slash_option(
    name="position",
    description="The airport position you would like to start controlling",
    required=True,
    opt_type=interactions.OptionType.STRING,
    choices=data.airport_options_pos)
async def handle_log_on(ctx: interactions.SlashContext, position: str):
    print("Command run: /log_on")
    sent_channel = ctx.channel.id
    sent_user = ctx.author.id
    if sent_channel != data.ccmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1257053360285159534 (where you can obtain ATIS).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        return
    if data.event_active == True:
        con_success = update_con_active(position, sent_user)
        if con_success == 2:
            current_time = datetime.now(utc_timezone).strftime("%H:%MZ")
            embed = interactions.Embed(
                description=f"Successfully logged on as {position} at {current_time}",
                color= interactions.Color.from_rgb(0, 57, 153))
            await ctx.send(embed=embed)
            channel = await ctx.bot.fetch_channel(data.event_channel_id)
            event_message = await channel.fetch_message(data.event_message_id)
            updated_embed = event_message.embeds[0]
            updated_embed.description += f"\n- {position} ({ctx.author.mention}) since {current_time}"
            await event_message.edit(embed=updated_embed)
        elif con_success == 1:
            error_embed = interactions.Embed( 
            description=f"Already logged on as another position, please log off before continuing",
            color= interactions.Color.from_rgb(221, 53, 53))
            await ctx.send(embed=error_embed,ephemeral=True)
        else:
            error_embed = interactions.Embed( 
            description=f"Position already claimed, you cannot log onto the same position",
            color= interactions.Color.from_rgb(221, 53, 53))
            await ctx.send(embed=error_embed,ephemeral=True)
    else:
        error_embed = interactions.Embed( 
            description=f"There is no active event, please try again during an event",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        
def setup(bot):
    print("Registered /log_on successfully")
    bot.add_command(handle_log_on)