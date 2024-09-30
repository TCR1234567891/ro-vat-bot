import interactions

bot_token = "MTI0OTc2NjAzMzQ3Mjg4MDc1MA.GDhEcr.aC7Z9yHk39OTQtnI1Zl49b6tUZTX2A38lGqHEs"

# Channels:
treq_channel_id = 1251588809192374323
cmd_channel_id = 1251588741383061574
scmd_channel_id = 1251588713440481341
ccmd_channel_id = 1264090675184537711
pexam_channel_id = 1268170188596056098
fplan_channel_id = 1269376551284244490
event_channel_id = 1269193355615670365
cfplan_channel_id = 1269376551284244490

# Roles:
obs_role_id = 1249962286005620799
s1_role_id = 1251589309975232553
s2_role_id = 1251589342401663088
c1_role_id = 1251589369710772340
ment_role_id = 1251589412794531981

# Status:
event_active = False
event_message_id = 0

# Server Data:
training_types = ["Controller Lesson 0 (Intro to ATC)","Controller Lesson 1 (National Airspace System)","Controller Lesson 2 (CRAFT IFR Clearances)",
                  "Controller Lesson 3 (Introduction to DEL+GND)","Controller Lesson 4 (Clearance and Ground)","Controller Lesson 5 (Practice Over-The-Shoulder Exam)"]

nato_alphabet = ("Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu")

wordnum = ("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Niner")

airports = ["RFD","PPH","TKO","LAR"]
airport_options_str = []
airport_options_int = []
airport_options_pos = []
airport_counter = 0
for airport in airports:
    airport_options_str.append(interactions.SlashCommandChoice(name = airport, value = airport))
for airport in airports:
    airport_counter += 1
    airport_options_int.append(interactions.SlashCommandChoice(name = airport, value = airport_counter))
airport_options_pos.extend([interactions.SlashCommandChoice(name = "LA_1_CTR", value = "LA_1_CTR"), interactions.SlashCommandChoice(name = "LA_2_CTR", value = "LA_2_CTR"),interactions.SlashCommandChoice(name = "CHI_1_CTR", value = "CHI_1_CTR"), interactions.SlashCommandChoice(name = "CHI_2_CTR", value = "CHI_2_CTR"),interactions.SlashCommandChoice(name = "BQ_1_CTR", value = "BQ_1_CTR"), interactions.SlashCommandChoice(name = "BQ_2_CTR", value = "BQ_2_CTR")])
for airport in airports:
    ctr_name = f"{airport}_TWR"
    airport_options_pos.append(interactions.SlashCommandChoice(name = ctr_name, value = ctr_name))
    ctr_name = f"{airport}_GND"
    airport_options_pos.append(interactions.SlashCommandChoice(name = ctr_name, value = ctr_name))
    ctr_name = f"{airport}_DEL"
    airport_options_pos.append(interactions.SlashCommandChoice(name = ctr_name, value = ctr_name))

runway_ref = {"RFD":["25L","25C","25R","7L","7C","7R"],"PPH":["15","33","29","11"],"TKO":["31","13","20","02"],"LAR":["24","06"]}
airport_names = {"RFD":"CHICAGO ROCKFORD","PPH":"PERTH","TKO":"TOKYO HANEDA","LAR":"LARNACA"}
runways_avail = {}

for airport_dict_val in runway_ref.items():
    new_runway_list = []
    app_list = []
    dep_list = []
    runway_list = airport_dict_val[1]
    for runway in runway_list:
        app_list.append("VIS RWY "+runway+" APCH")
        app_list.append("LOC RWY "+runway+" APCH")
        app_list.append("ILS RWY "+runway+" APCH")
        dep_list.append("RWY "+runway)
    new_runway_list.append(app_list)
    new_runway_list.append(dep_list)
    runways_avail[airport_dict_val[0]] = new_runway_list
    
# Commands:
command_ids = {
    "profile": "1251521330428514378",
    "con_leaderboard": "1265161319506645032",
    "help": "1266438388773425255",
    "start_event": "1262988320116314166",
    "end_event": "1262988320116314165",
    "atis_post": "1262593686550872148",
    "atis": "1262988320116314167",
    "metar": "1264086133722058834",
    "training_log": "1251512590383845406",
    "training_request": "1250075348045922315",
    "training_del": "1254206706058268802",
    "training_clr": "1260416649903870002",
    "post": "1262593927576551516",
    "embed": "1250473718598340629",
    "log_on": "1264774097326571612",
    "log_off": "1264774097838018671"
}