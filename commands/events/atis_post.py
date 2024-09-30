import interactions
import data
import json
from datetime import datetime
import pytz
from ..tools.atis.publish_atis import publish_atis


utc_timezone = pytz.UTC

@interactions.slash_command(
    name="atis_post",
    description = "Update the ATIS information of an airport",
    dm_permission=False)
@interactions.slash_option(
    name="airport",
    description="The airport you wish to update the ATIS of",
    opt_type=interactions.OptionType.STRING,
    required = True,
    choices=data.airport_options_str)
@interactions.slash_option(
    name="identifier",
    description="The letter identifying your ATIS version",
    opt_type=interactions.OptionType.STRING,
    required = True,
    choices=[interactions.SlashCommandChoice(name="Alpha", value="Alpha"), interactions.SlashCommandChoice(name="Bravo", value="Bravo"), interactions.SlashCommandChoice(name="Charlie", value="Charlie"), interactions.SlashCommandChoice(name="Delta", value="Delta"), interactions.SlashCommandChoice(name="Echo", value="Echo"), interactions.SlashCommandChoice(name="Foxtrot", value="Foxtrot"), interactions.SlashCommandChoice(name="Golf", value="Golf"), interactions.SlashCommandChoice(name="Hotel", value="Hotel"), interactions.SlashCommandChoice(name="India", value="India"), interactions.SlashCommandChoice(name="Juliet", value="Juliet"), interactions.SlashCommandChoice(name="Kilo", value="Kilo"), interactions.SlashCommandChoice(name="Lima", value="Lima"), interactions.SlashCommandChoice(name="Mike", value="Mike"), interactions.SlashCommandChoice(name="November", value="November"), interactions.SlashCommandChoice(name="Oscar", value="Oscar"), interactions.SlashCommandChoice(name="Papa", value="Papa"), interactions.SlashCommandChoice(name="Quebec", value="Quebec"), interactions.SlashCommandChoice(name="Romeo", value="Romeo"), interactions.SlashCommandChoice(name="Sierra", value="Sierra"), interactions.SlashCommandChoice(name="Tango", value="Tango"), interactions.SlashCommandChoice(name="Uniform", value="Uniform"), interactions.SlashCommandChoice(name="Victor", value="Victor"), interactions.SlashCommandChoice(name="Whiskey", value="Whiskey"), interactions.SlashCommandChoice(name="X-ray", value="X-ray"), interactions.SlashCommandChoice(name="Yankee", value="Yankee")])
@interactions.slash_option(
    name="config",
    description="Traffic flow direction",
    opt_type=interactions.OptionType.INTEGER,
    required = True,
    choices=[])
@interactions.slash_option(
    name="remarks",
    description="NOTAMS and other remarks",
    opt_type = interactions.OptionType.STRING,
    required = True)

async def handle_atis_post(ctx: interactions.SlashContext, airport: str, identifier: str, config: str, remarks: str):
    print("Command run: /atis_post")
    sent_channel = ctx.channel.id
    if sent_channel != data.ccmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1257053360285159534 (where you can obtain and post ATIS).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        return
    if data.event_active == False:
        error_embed = interactions.Embed( 
            description=f"There is no active event, please try again during an event",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        return
    direction = data.runways_avail[airport]
    json_data = json.dumps(direction)
    current_utc_time = datetime.now(utc_timezone)
    time_str = current_utc_time.strftime("%H:%MZ")
    publish_atis(airport, identifier, json_data, remarks, time_str)
    updated_str = f"{airport} ATIS information successfully updated at {time_str}"
    embed = interactions.Embed(
        description=updated_str,
        color=interactions.Color.from_rgb(0, 57, 153))
    await ctx.send(embed=embed)
    
    
def setup(bot):
    print("Registered /atis_post successfully")
    bot.add_command(handle_atis_post)