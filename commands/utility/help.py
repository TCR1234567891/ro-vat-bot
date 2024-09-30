import interactions
import data


@interactions.slash_command(
    name="help",
    description="Learn about this bot and included commands", 
    dm_permission=False)
        
async def help_command(ctx: interactions.SlashContext):
    print("Command run: /help")
    sent_channel = ctx.channel.id
    if sent_channel != data.cmd_channel_id and sent_channel != data.scmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1172662600216096778 (where you can interact with bots).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 
        return
    embed = interactions.Embed(
        description=f"Here's a list of commands *(note: some commands may not be available to all users)*:",
        color= interactions.Color.from_rgb(0, 57, 153))
    embed.add_field(
        name="General",
        value=f"</profile:{data.command_ids['profile']}>, </con_leaderboard:{data.command_ids['con_leaderboard']}>, </help:{data.command_ids['help']}>",
        inline=False)
    embed.add_field(
        name="Event",
        value=f"</start_event:{data.command_ids['start_event']}>, </end_event:{data.command_ids['end_event']}>, </atis_post:{data.command_ids['atis_post']}>, </atis:{data.command_ids['atis']}>, </metar:{data.command_ids['metar']}>, </log_on:{data.command_ids['log_on']}>, </log_off:{data.command_ids['log_off']}>",
        inline=False)
    embed.add_field(
        name="Training",
        value=f"</training_log:{data.command_ids['training_log']}>, </training_request:{data.command_ids['training_request']}>, </training_del:{data.command_ids['training_del']}>, </training_clr:{data.command_ids['training_clr']}>",
        inline=False)
    embed.add_field(
        name="Utility",
        value=f"</post:{data.command_ids['post']}>, </embed:{data.command_ids['embed']}>",
        inline=False)
    await ctx.send(embed=embed)
    
def setup(bot):
    print("Registered /help successfully")
    bot.add_command(help_command)
