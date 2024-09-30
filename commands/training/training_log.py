import interactions
import sqlite3
from datetime import datetime
import pytz
from ..tools.trainings.submit_log import submit_log


utc_timezone = pytz.UTC

@interactions.slash_command(name="training_log", description="Log a user's training", dm_permission=False)

@interactions.slash_option(name="student", description="The student you trained", required=True, opt_type=interactions.OptionType.USER)

@interactions.slash_option(name="training", description="The training completed", required=True, opt_type=interactions.OptionType.STRING, 
    choices=[
        interactions.SlashCommandChoice(name="ATC Lesson 0 (Intro)", value="Controller Lesson 0 (Intro to ATC)"),
        interactions.SlashCommandChoice(name="ATC Lesson 1 (NAS)", value="Controller Lesson 1 (National Airspace System)"),
        interactions.SlashCommandChoice(name="ATC Lesson 2 (CRAFT)", value="Controller Lesson 2 (CRAFT IFR Clearances)"),
        interactions.SlashCommandChoice(name="ATC Lesson 3 (GND)", value="Controller Lesson 3 (Introduction to DEL+GND)"),
        interactions.SlashCommandChoice(name="ATC Lesson 4 (DEL+GND)", value="Controller Lesson 4 (Clearance and Ground)"),
        interactions.SlashCommandChoice(name="ATC Lesson 5 (Pre-OTS)", value="Controller Lesson 5 (Practice Over-The-Shoulder Exam)")
    ]
)
@interactions.slash_option(name="grade", description="Whether the student passed or failed", required=True, opt_type=interactions.OptionType.STRING, 
    choices=[
        interactions.SlashCommandChoice(name="Pass",value="1"),
        interactions.SlashCommandChoice(name="Fail", value="0")
     ]
)

async def handle_training_log(ctx: interactions.SlashContext, student: str, training: str, grade: str):
    print("Command run: /training_log")
    grade_int = int(grade)
    student_mention = student.mention
    student_id = student.id
    command_time = datetime.now(utc_timezone).strftime("%Y-%m-%d %H:%M:%SZ")
    auth_mention = ctx.author.mention
    auth_id = ctx.author.id
    embed = interactions.Embed(
        description=f"Successfully logged {student_mention}'s {training}",
        color= interactions.Color.from_rgb(0, 57, 153))
    await ctx.send(embed = embed)
    submit_log(student_id,training,auth_id,command_time,grade_int)
    
def setup(bot):
    print("Registered /training_log successfully")
    bot.add_command(handle_training_log)