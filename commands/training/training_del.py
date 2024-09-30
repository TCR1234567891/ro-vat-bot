import interactions
import data
from ..tools.trainings.check_profile import check_profile
from ..tools.trainings.delete_log import delete_log


@interactions.slash_command(name="training_del", description="Delete a user's training record", dm_permission=False)

@interactions.slash_option(name="user", description="The user whose trainings you wish to modify", required = True, opt_type=interactions.OptionType.USER)

@interactions.slash_option(name="training_num", description="The number of the training you'd like to delete", required = True, opt_type=interactions.OptionType.INTEGER)

async def handle_training_del(ctx: interactions.SlashContext, user = str,training_num=int):
    print("Command run: /training_del")
    sent_channel = ctx.channel.id
    str_training_num = str(training_num)
    if sent_channel != data.cmd_channel_id and sent_channel != data.scmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1172662600216096778 (where you can interact with bots).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)            
        return
    user_id = user.id
    found_username = check_profile(user_id)
    if found_username[0]:
        username = found_username[0][0][0]
        del_result = delete_log(training_num, username)
        user_mention = user.mention
        if del_result == False:
            embed=interactions.Embed(
            description=f"{user_mention}'s {found_username[0][0][1]} logged by <@{found_username[0][0][2]}> has been deleted.",
            color= interactions.Color.from_rgb(0, 57, 153))
            await ctx.send(embed=embed)
        else:
            error_embed = interactions.Embed( 
            description="No such training was found, please double-check you have inserted the correct training number.",
            color= interactions.Color.from_rgb(221, 53, 53))
            await ctx.send(embed=error_embed,ephemeral=True)  
    else:
        error_embed = interactions.Embed( 
        description="No user records found",
        color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        
def setup(bot):
    print("Registered /training_del successfully")
    bot.add_command(handle_training_del)