# import discord
# from discord.ext import commands
#
# TOKEN = 'OTU4MzI5NDY4NDQ1OTE3MjA0.YkLv3g.QJjheYPAOA_yZfhZXN8L2mVHJkc'
#
# bot = commands.Bot(command_prefix='!')
#
# @bot.command(pass_context=True)
# async def test(ctx, arg):
#     await ctx.send(arg)
#
# bot.run(TOKEN)

import discord

TOKEN = 'OTU4MzI5NDY4NDQ1OTE3MjA0.YkLv3g.QJjheYPAOA_yZfhZXN8L2mVHJkc'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Миша начни работать'):
        await message.channel.send('')
client.run(TOKEN)