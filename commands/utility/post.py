import interactions

@interactions.slash_command(
    name="post",
    dm_permission=False)
@interactions.slash_default_member_permission(interactions.Permissions.ADMINISTRATOR)
@interactions.slash_option(
    name="text",
    description="Insert the text to post/embed",
    required=False,
    opt_type=interactions.OptionType.STRING)
@interactions.slash_option(
    name="attachment",
    description="Attach a file to the post",
    required=False,
    opt_type=interactions.OptionType.ATTACHMENT)
async def handle_post(ctx: interactions.SlashContext, text: str=None, attachment: interactions.File=None):
    print("Command run: /post")
    txt_response = text if text else ""
    if attachment:
        attachment_url = attachment.url
        txt_response += f"\n {attachment_url}"
    await ctx.send(content=txt_response)
    
def setup(bot):
    print("Registered /post successfully")
    bot.add_command(handle_post)