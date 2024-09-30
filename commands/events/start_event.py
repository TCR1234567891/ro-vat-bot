import interactions
import data
from datetime import datetime
import pytz
from ..tools.atis.fetch_atis import fetch_atis
from ..tools.atis.fetch_metar import fetch_metar
from ..tools.atis.event_start import event_start
from..tools.flight.file_fplan import file_fplan
import functools

utc_timezone = pytz.UTC



# [BUTTON] flight plan

fplan_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="File a Flight Plan",
    custom_id="fplan_button"
)

async def handle_fplan(ctx: interactions.ComponentContext):
    modal = interactions.Modal(
        interactions.ShortText(
            label="In-Game Callsign",
            custom_id="igcallsign",
            placeholder="e.g. Raider-1234",
            required=True,
            max_length=30
            ),
        interactions.ShortText(
            label="Callsign",
            custom_id="callsign",
            placeholder="e.g. N123AB",
            required=True,
            max_length=30
            ),
        interactions.ShortText(
            label="Aircraft Type (ICAO)",
            custom_id="actype",
            placeholder="e.g. B739",
            required=True,
            max_length=10
            ),
        interactions.ParagraphText(
            label="Route",
            custom_id="route",
            placeholder="e.g. PPH > RENDR > ANYMS1J.ANYMS > LAR",
            required=True,
            max_length=200
            ),
        interactions.ShortText(
            label="Cruise Altitude",
            custom_id="cruise",
            placeholder="e.g. 050",
            required=True,
            max_length=3
            ),
        title="File a Flight Plan",
        custom_id="fplan_modal")
    await ctx.send_modal(modal)
    modal_ctx: interactions.ModalContext = await ctx.bot.wait_for_modal(modal)
    igcallsign = modal_ctx.responses["igcallsign"]
    callsign = modal_ctx.responses["callsign"]
    actype = modal_ctx.responses["actype"]
    route = modal_ctx.responses["route"]
    cruise = modal_ctx.responses["cruise"]
    global bot_instance
    user_id = ctx.user.id
    user_mention = ctx.user.mention
    if route[0:3] in data.airports and route[-3:] in data.airports:
        command_time = datetime.now(utc_timezone).strftime("%Y-%m-%d %H:%M:%SZ")
        file_fplan(user_id, igcallsign, callsign, actype, route, cruise, command_time)
        embed = interactions.Embed(
                description="Flight Plan has been successfully filed",
                color= interactions.Color.from_rgb(0, 57, 153))
        await modal_ctx.send(embed=embed, ephemeral=True)
        channel = await bot_instance.fetch_channel(data.fplan_channel_id)
        embed = interactions.Embed(
                description=f"**Username:**\n{user_mention}\n \n**In-Game Callsign:**\n{igcallsign}\n \n**Callsign:**\n{actype}\n \n**Route:**\n{route}\n \n**Cruise:**\n{cruise}\n \n**Timestamp:**\n{command_time}",
                color= interactions.Color.from_rgb(0, 57, 153))
        await channel.send(embed=embed)
    else:
        error_embed = interactions.Embed( 
            description=f"Airports filed under 'route' were incorrect, please try again and insert an ICAO code for both arrival and departure airports (e.g. ***PPH***, ***TKO***)",
            color= interactions.Color.from_rgb(221, 53, 53))
        await modal_ctx.send(embed=error_embed, ephemeral = True)
        


# [BUTTON] metar_button

metar_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="METAR",
    custom_id="metar_button"
    )

async def handle_metar(ctx: interactions.ComponentContext):
    found_metar = fetch_metar()
    if found_metar[4] == "CLR":
            cloud_info = ""
    else:
        cloud_info = f"SCT{found_metar[3]} "
    atis_info = f"METAR {found_metar[0]}{found_metar[1]}KT {found_metar[2]}SM {cloud_info}{found_metar[5]}/{found_metar[6]} A{found_metar[7]}"
    embed = interactions.Embed(
        description=atis_info.upper(),
        color= interactions.Color.from_rgb(0, 57, 153))
    await ctx.send(embed=embed, ephemeral=True)
        

# [BUTTON] atis_button

atis_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="View ATIS/METAR",
    custom_id="atis_button"
    )

async def handle_atis_req(ctx, icao, found_atis):
    atis_data = next(item for item in found_atis if item[0] == icao)
    wx_data = fetch_metar()
    if wx_data[4] == "CLR":
        cloud_info = ""
    else:
        cloud_info = f"SCT{wx_data[3]} "
    str_alt = wx_data[7]
    altimeter = ""
    for number in str_alt:
        number = int(number)
        altimeter += data.wordnum[number] + " "
    atis_info = f"{atis_data[0]} AIRPORT ATIS INFORMATION {atis_data[1][0]}. {atis_data[4]}. {wx_data[0]}{wx_data[1]}KT {wx_data[2]}SM {cloud_info}{wx_data[5]}/{wx_data[6]} A{wx_data[7]} ({altimeter}). {atis_data[2][0]} IN USE, DEPTG {atis_data[2][1]}. {atis_data[3]}"
    embed = interactions.Embed(
        description=atis_info.upper(),
        color=interactions.Color.from_rgb(0, 57, 153))
    await ctx.send(embed=embed, ephemeral=True)


async def handle_atis(ctx: interactions.ComponentContext, bot):
    found_atis = fetch_atis()
    if found_atis is None:
        embed = interactions.Embed(
            description="No active ATIS information found, however you can still view the METAR",
            color=interactions.Color.from_rgb(0, 57, 153))
        await ctx.send(embed=embed, components=[metar_button], ephemeral=True)
    else:
        atis_buttons = []
        for item in found_atis:
            icao = item[0]
            icao_button = interactions.Button(style=interactions.ButtonStyle.PRIMARY, label=item[0], custom_id=icao)
            atis_buttons.append(icao_button)
            bot._component_callbacks[icao] = lambda ctx, icao=icao: handle_atis_req(ctx, icao, found_atis)
        embed = interactions.Embed(
            description="Please select one of the available ATIS or METAR",
            color=interactions.Color.from_rgb(0, 57, 153))
        components = [[metar_button] + atis_buttons]
        await ctx.send(embed=embed, components=components, ephemeral=True)
        
        

# /start_event



@interactions.slash_command(
    name="start_event",
    description="Start an event or recover a previously lost event",
    dm_permission=False)
@interactions.slash_option(
    name="link",
    description="Link to Roblox private server",
    required=True,
    opt_type=interactions.OptionType.STRING)
async def handle_start_event(ctx: interactions.SlashContext, link: str):
    print("Command run: /start_event")
    global bot_instance
    if data.event_active == False:
        data.event_active = True
        hosted_success = event_start()
        if hosted_success:
            current_time = datetime.now(utc_timezone).strftime("%H:%MZ")
            user_id = ctx.author.id
            embed = interactions.Embed(
                description=f"Event successfully started at {current_time}",
                color= interactions.Color.from_rgb(0, 57, 153))
            await ctx.send(embed=embed)
            channel = await bot_instance.fetch_channel(data.event_channel_id)
            join_button = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label="Join Event",
                url=link
                )
            embed = interactions.Embed(
                title="Event",
                description=f"An event is currently being hosted, we hope to see you there!\n \nActive Controllers:",
                color= interactions.Color.from_rgb(0, 57, 153))
            host_embed = await channel.send(embed=embed,components=[fplan_button, atis_button, join_button])
            data.event_message_id = host_embed.id
        else:
            current_time = datetime.now(utc_timezone).strftime("%H:%MZ")
            embed = interactions.Embed(
                description=f"Previously active event recovered at {current_time}",
                color= interactions.Color.from_rgb(0, 57, 153))
            await ctx.send(embed=embed)
    else:
        error_embed = interactions.Embed( 
            description=f"There is already an active event",
            color= interactions.Color.from_rgb(221, 53, 53))
        await ctx.send(embed=error_embed,ephemeral=True) 


def setup(bot):
    global bot_instance
    bot_instance = bot
    print("Registered /start_event successfully")
    bot._component_callbacks[metar_button.custom_id] = handle_metar
    bot._component_callbacks[fplan_button.custom_id] = handle_fplan
    bot._component_callbacks[atis_button.custom_id] = lambda ctx: handle_atis(ctx, bot)
    bot.add_command(handle_start_event)
