#bot qui fait des graphiques ds meilleurs notes

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
NDEL = "no title"

scoresDict = {}
scoresList = []


@bot.event
async def on_ready():
    print("im ready")


@bot.command()
async def new(ctx):
    global NDEL
    await ctx.send("What's the name of the exam?")

    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    NDE = await bot.wait_for("message", timeout=10, check=check)
    print(NDE.content)
    NDEL = NDE.content
    await look(ctx)
    await rebirth(ctx)


@bot.command()
async def look(ctx):
    try:
     embed = discord.Embed(title=NDEL, description="classement")
     embed.add_field(name="top1", value=scoresList[0], inline=False)
     embed.add_field(name="top2", value=scoresList[1], inline=False)
     embed.add_field(name="top3", value=scoresList[2], inline=False)
     #embed.add_field(name= "top4", value= scoresList[3], inline=False)
     #embed.add_field(name= "top5", value= scoresList[4], inline=False)
     await ctx.send(embed=embed)
    except:
     await ctx.send("Add at least 3 grades to see the classment")


#changer les value pour des variables


@bot.command()
async def addscore(ctx):
    tusername = ctx.author
    await ctx.send("what is your grade")

    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    NewScore = await bot.wait_for("message", timeout=10, check=check)
    print(tusername)
    print(NewScore.content)
    #modifier
    scoresDict[tusername.name] = NewScore.content
    print(scoresDict)
    await sortlist()
    print(scoresList)
    return NewScore


@bot.command()
async def rebirth(ctx):
    scoresDict.clear()
    scoresList.clear()


@bot.command()
async def sortlist():
    global scoresList
    scoresList = sorted(scoresDict.items(), key=lambda t: t[1], reverse=True)


bot.run("nonononono")


#ajouter un systeme de communication pour dire que le titre a changer et de suppriemer le classement

#ajourter une commande qui prend le nom de lutilisateur, demande sa notes et la prend
#ajouter une function qui va prendre les resultats et les placer un ordre decroissant dans les variables top1, top2, top3

#assembler le tableau (creer)
