import interactions
from ..tools.controllers.check_leaderboard import check_leaderboard
from ..tools.time.get_time import get_time
from ..tools.time.get_time_abv import get_time_abv
import data


@interactions.slash_command(
    name="controller_leaderboard",
    description="See the leaderboard of controllers",
    dm_permission=False)
async def handle_controller_leaderboard(ctx: interactions.SlashContext):
    print("Command run: /controller_leaderboard")    
    sent_channel = ctx.channel.id
    if sent_channel != data.cmd_channel_id and sent_channel != data.scmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1172662600216096778 (where you can interact with bots).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        return
    leaderboard = check_leaderboard()
    if len(leaderboard) >= 3:
        embed = interactions.Embed(
            description=f"## Controller Leaderboard:\n \n1st: <@{leaderboard[0][0][0]}>\n*Total Time Controlled: {get_time(leaderboard[0][1])}*\n- *DEL/GND: {get_time_abv(leaderboard[0][0][1])}*\n- *TWR: {get_time_abv(leaderboard[0][0][2])}*\n- *CTR: {get_time_abv(leaderboard[0][0][3])}*\n\n2nd: <@{leaderboard[1][0][0]}>\n*Total Time Controlled: {get_time(leaderboard[1][1])}*\n- *DEL/GND: {get_time_abv(leaderboard[1][0][1])}*\n- *TWR: {get_time_abv(leaderboard[1][0][2])}*\n- *CTR: {get_time_abv(leaderboard[1][0][3])}*\n\n3rd: <@{leaderboard[2][0][0]}>\n*Total Time Controlled: {get_time(leaderboard[2][1])}*\n- *DEL/GND: {get_time_abv(leaderboard[2][0][1])}*\n- *TWR: {get_time_abv(leaderboard[2][0][2])}*\n- *CTR: {get_time_abv(leaderboard[2][0][3])}*",
            color= interactions.Color.from_rgb(0, 57, 153))
        await ctx.send(embed=embed)
    else:
        error_embed = interactions.Embed( 
            description=f"Not enough controller data found",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        
def setup(bot):
    print("Registered /controller_leaderboard successfully")
    bot.add_command(handle_controller_leaderboard)