import discord
from discord.ext import commands
import requests
from PIL import Image
import mojang

bot = commands.Bot(command_prefix='+')

@bot.command()
async def cape(ctx, username = None):
    if username == None:
        profileurl = ctx.message.author.avatar_url
        r = requests.get(profileurl)
        open('profile.png', 'wb').write(r.content)
        Image1 = Image.open('template.png')
        Image1copy = Image1.copy()
        Image2 = Image.open('profile.png')
        Image2copy = Image2.copy().resize((80, 127))
        Image1copy.paste(Image2copy, (8, 8))
    else:
        uuid = mojang.api.MojangAPI.get_uuid(username)
        if not uuid:
            ctx.message.reply('pls enter a valid username')
        else:
            renderurl = "https://crafatar.com/renders/body/" + str(uuid) + "?overlay"
            r = requests.get(renderurl)
            open('skinrender.png', 'wb').write(r.content)
            Image1 = Image.open('skintemplate.png')
            Image1copy = Image1.copy()
            Image2 = Image.open('skinrender.png')
            Image2copy = Image2.copy()
            Image2copy.thumbnail((80,128))
            Image1copy.paste(Image2copy, (19, 8), Image2copy)




    Image1copy.save('out.png')

    await ctx.message.reply('by adsgniD#2006', mention_author=True, file=discord.File('out.png'))

bot.run('TAKKO PIZZZZZAAAAA APFELTUTSCHE LASAGNEEEEEE')