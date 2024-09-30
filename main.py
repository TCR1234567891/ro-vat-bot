import interactions
from commands import setup
import data
from commands.databases import init as db_init

bot = interactions.Client(token=data.bot_token)

db_init()
print("\nInitialized Database\n ")

setup(bot)

print("Finalizing Initialization\n \n")

bot.start()