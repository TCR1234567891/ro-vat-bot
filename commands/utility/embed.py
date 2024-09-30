import interactions

@interactions.slash_command(
    name="embed",
    dm_permission=False)
@interactions.slash_default_member_permission(interactions.Permissions.ADMINISTRATOR)
@interactions.slash_option(
    name="title",
    description="Title of your announcement",
    opt_type=interactions.OptionType.STRING,
    required=True)
@interactions.slash_option(
    name="text",
    description="Text in your announcement",
    opt_type=interactions.OptionType.STRING,
    required=True)
@interactions.slash_option(
    name="color",
    description="The highlight color of the post",
    opt_type=interactions.OptionType.INTEGER,
    required=True,
    choices=[
        interactions.SlashCommandChoice(name="Red", value=0),
        interactions.SlashCommandChoice(name="Blue", value=1),
        interactions.SlashCommandChoice(name="White", value=2)
    ]
)    
async def handle_announce(ctx: interactions.SlashContext, title: str, text: str, color:int):
    print("Command run: /embed")
    if color == 0:
        colortup=(221, 53, 53)
    elif color == 1:
        colortup=(0, 57, 153)
    else:
        colortup=(255, 255, 255)
    embed=interactions.Embed(
        title=title,
        description=text,
        color= interactions.Color.from_rgb(colortup[0],colortup[1],colortup[2]))        
    await ctx.send(embed=embed) 
    
def setup(bot):
    print("Registered /embed successfully")
    bot.add_command(handle_announce)