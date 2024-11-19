import interactions
from commands import setup
import data
from commands.databases import init as db_init
import bot_token

bot = interactions.Client(token=bot_token.bot_token)

db_init()
print("\nInitialized Database\n ")

setup(bot)

print("Finalizing Initialization\n \n")

print("Hello World")

bot.start()