import interactions
import data

@interactions.slash_command(
    name="unlock_exam",
    description="Unlock the pilot exam.",
    dm_permission=False
)

async def handle_p_exam(ctx: interactions.SlashContext):
    print("Command run: /p_exam")
    sent_channel = ctx.channel.id
    sent_user = ctx.author.id
    if sent_channel != data.ccmd_channel_id:
        error_embed = interactions.Embed( 
            description=f"You cannot perform this action in this channel. Please try again in https://discord.com/channels/1172659238120738996/1257053360285159534 (where you can obtain ATIS).",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True)
        return
    
    interactions.Modal(
        interactions.ParagraphText(
            label="What is the difference between *IFR* and *VFR* and what does each abbreviation stand for?",
            custom_id="p_ifr_vfr",
            placeholder="Answer here",
            required=True
            max_length=
        )
    )


def setup(bot):
    print("Registered /p_exam successfully")
    bot.add_command(handle_p_exam)