import interactions
import data
from ..tools.trainings.check_profile import check_profile
from ..tools.time.get_time import get_time as get_time
from ..tools.time.get_time_abv import get_time_abv as get_time_abv

@interactions.slash_command(
        name="profile",
        description="View user training and administrative logs",
        dm_permission=False)
@interactions.slash_option(
    name="username",
    description="The user you would like to look up",
    required=True,
    opt_type=interactions.OptionType.USER)

async def handle_profile(ctx: interactions.SlashContext, username: str):
    print("Command run: /profile")
    sent_channel = ctx.channel.id
    if sent_channel != data.cmd_channel_id and sent_channel != data.scmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1172662600216096778 (where you can interact with bots).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        return
    user_id = username.id
    found_data = check_profile(user_id)
    found_username = found_data[0]
    found_history = found_data[1]
    if found_username:
        found_mention = username.mention
        found_history.append(found_history[1]+found_history[2]+found_history[3])
        record_string = ""
        training_num = 0
        str_username = str(username)
        for record in found_username:
            if record[4] == 0:
                passorfail="Fail"
            elif record[4]==1:
                passorfail="Pass"
            training_num += 1
            record_string += f"\n**Training #{training_num}:**\n- *Training:* {record[1]}\n- *Grade:* {passorfail}\n- *Trainer:* <@{record[2]}>\n- *Timestamp:* {record[3]}\n"
        final_embed = interactions.Embed(
            title=f"{str_username[1:-1]}'s Profile",  
            description=f"**User:**\n{found_mention}\n{record_string}\n**Total Time Controlled: {get_time(found_history[4])}**\n- *CTR: {get_time_abv(found_history[3])}*\n- *TWR: {get_time_abv(found_history[2])}*\n- *DEL/GND: {get_time_abv(found_history[1])}*",
            color= interactions.Color.from_rgb(0, 57, 153))
        await ctx.send(embed=final_embed)
    else:
        error_embed = interactions.Embed( 
        description="No user records found",
        color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        
def setup(bot):
    print("Registered /profile successfully")
    bot.add_command(handle_profile)