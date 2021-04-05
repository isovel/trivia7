__authors__ = 'toastythetoaster'

import discord
from discord.ext import commands
from discord_slash import SlashCommand
import traceback
import sys


initial_extensions = ['cog', 'trivia']


def gettoken():
    token_file = open("token.txt", "r")
    token_string = token_file.read()
    token_token = token_string.split("\n")
    token = str(token_token[0])
    return token


bot_token = gettoken()

description = "trivia!"
bot = commands.Bot(command_prefix="t7!")
slash = SlashCommand(bot, override_type = True)

if __name__ == '__main__':
    for extension in initial_extensions:
        # noinspection PyBroadException
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Failed to load" + extension, file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('That command does not exist, or the cog did not properly load.')
#         await ctx.message.add_reaction('\N{CROSS MARK}')
#     else:
#         await ctx.message.add_reaction('\N{CROSS MARK}')
#         raise error


def log(string, debug = False):
    timestamp = time.ctime();
    log_string = '[%s] [%s] %s'%(timestamp, script_name, string);
    if not debug == True:
        print(log_string);
        log_file.write('%s\n'%log_string);
    else: 
        open('debug.log', 'a').write('%s\n'%log_string);

bot.run(bot_token)