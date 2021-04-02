import discord
from discord.ext import commands
import requests
from PIL import Image

bot = commands.Bot(command_prefix='+')

@bot.command()
async def cape(ctx):
    profileurl = ctx.message.author.avatar_url

    r = requests.get(profileurl)
    open('profile.png', 'wb').write(r.content)

    Image1 = Image.open('template.png')

    Image1copy = Image1.copy()
    Image2 = Image.open('profile.png')
    Image2copy = Image2.copy()

    Image2copy.thumbnail((80, 80))

    Image1copy.paste(Image2copy, (8, 42))

    Image1copy.save('out.png')

    await ctx.message.reply('by adsgniD#2006', mention_author=True, file=discord.File("out.png"))

bot.run('HEHEHE als ob ich dir meinen token verrate xD')
