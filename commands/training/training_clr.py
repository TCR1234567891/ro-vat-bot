import interactions
import sqlite3
import data
from ..tools.trainings.clear_log import clear_log


@interactions.slash_command(name="training_clr", description="Clear a user's training logs", dm_permission=False)

@interactions.slash_default_member_permission(interactions.Permissions.ADMINISTRATOR)

@interactions.slash_option(name="user", description="The user who's records you wish to delete", required=True, opt_type=interactions.OptionType.USER)

async def handle_clear_log(ctx: interactions.SlashContext, user: str):
    print("Command run: /training_clr")
    userid = user.id
    clear_log(userid)
    sent_channel = ctx.channel.id
    if sent_channel != data.cmd_channel_id and sent_channel != data.scmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1172662600216096778 (where you can interact with bots).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)            
        return
    embed=interactions.Embed(
        description=f"{user.mention}'s training history has been successfully cleared",
        color= interactions.Color.from_rgb(0, 57, 153))
    await ctx.send(embed=embed)

def setup(bot):
    print("Registered /training_clr successfully")
    bot.add_command(handle_clear_log)