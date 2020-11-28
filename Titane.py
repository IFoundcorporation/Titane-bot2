#bot qui fait des graphiques ds meilleurs notes

import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("im ready")


@bot.command()
async def getilte(ctx):
     await ctx.send("Quel est le nom de l'examin?")

     def check(message):
         return message.author == ctx.message.author and ctx.message.channel == message.channel

     NDEC = await bot.wait_for("message", timeout = 10, check = check)
     print(NDEC.content)
     NDE = NDEC.content
     return NDE

    
@bot.command()
async def Make(ctx):
    NDE = await getilte(ctx)
    embed = discord.Embed(title = NDE, description ="classement")
    embed.add_field(name = "top1", value = "im first", inline = False )
    embed.add_field(name = "top2", value = "im second", inline = False)
    embed.add_field(name = "top3", value = "im third", inline = False) 
    embed.add_field(name = "top4", value = "im fourth", inline = False)
    embed.add_field(name = "top5", value = "im fifth", inline = False)
    await ctx.send(embed = embed)
#changer les value pour des variables


@bot.command()
async def addscore(ctx):
    await ctx.send("what is your grade")

    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    NewScore = await bot.wait_for("message", timeout=10, check=check)
    print(NewScore.content)
    return NewScore


bot.run("NzgxMjAxNjk4ODMxNDY2NTE3.X76Mxw.OoVlZ2STGqanIormm-7nEHIPcHY")



#ajouter un systeme de communication pour dire que le titre a changer et de suppriemer le classement

#ajourter une commande qui prend le nom de lutilisateur, demande sa notes et la prend
#ajouter une function qui va prendre les resultats et les placer un ordre decroissant dans les variables top1, top2, top3

#assembler le tableau (creer)
