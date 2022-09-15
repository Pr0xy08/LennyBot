import discord
import random
from discord.ext import commands
from lenny import lenny
import os
bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())
bot.remove_command("help")

########################################################################################################################
#when the bot is online it will send this verification message.
@bot.event 
async def on_ready():
  print("===========================")
  print("Logged in as: {0.user}".format(bot))
  print("===========================")
  
########################################################################################################################
#This is the equivalent of a !help command.  
@bot.command()
async def noob(ctx):
  embed=discord.Embed(title="__**Help**__", description="***Here are all of my commands:***", color=0xeaade2)
  embed.add_field(name="```!hello```", value="***-I will greet you!***", inline=False)
  embed.add_field(name="```!sadlenny```", value="***-You will make me sad!***", inline=False)
  embed.add_field(name="```!happylenny```", value="***-You will make me sad!***", inline=False)
  embed.add_field(name="```!rlenny```", value="***-Picks a random lenny!***", inline=False)
  embed.add_field(name="```!meetmymaker```", value="***-I'll show you who made me!***", inline=False)
  await ctx.send(embed=embed)
  await ctx.message.delete()
  
########################################################################################################################
#replies with a random hello message.  
@bot.command()
async def hello(ctx):
  ls_hello = ("Hi!", "Wassup!", "Wagwan my G!", "Howdy!", "Greetings", "I recognise you!", "Hey!", "‘Ello, gov'nor!", "‘Sup, homeslice?", "How you doin'?", "Hey, boo.", "Bonjour!", "Yo yo yo!", "Whaddup bro?")
  r_hello = random.choice(ls_hello)
  await ctx.send("( ͡° ͜ʖ ͡°) " + str(r_hello))
  
########################################################################################################################
#similar to the !noob command, although it embeds links to all my social accounts.
@bot.command()
async def meetmymaker(ctx):
  embed=discord.Embed(title="__**My Maker**__", description="***Check out my Socials***", color=0xeaade2)
  embed.add_field(name="***Github***", value="https://github.com/Pr0xy08", inline=False)
  embed.add_field(name="***Linkedin***", value="https://www.linkedin.com/in/drew-wandless-8b2a97205/?originalSubdomain=uk", inline=False)
  embed.add_field(name="***Replit***", value = "https://replit.com/@drewwandless1", inline=False)
  await ctx.send(embed=embed)
  await ctx.message.delete()

########################################################################################################################
#generates a random lenny from the lenny library
@bot.command()
async def rlenny(ctx):
  await ctx.send(lenny())
  await ctx.message.delete()

#######################################################################################################################
#generates a sad lenny from the list.
@bot.command()
async def sadlenny(ctx):
  ls_sadlenny = ("(つ﹏<。)", "(◞д◟)", "(´°ω°`)", "(っ◞‸◟c)", "( ・⌓・｀)", "(ᗒᗣᗕ)՞", ">⌓<｡", "（>﹏<）", "(ಥ﹏ಥ)", "ཀ ʖ̯ ཀ", "(⋟﹏⋞)", "╥﹏╥", "ಠ_ಠ", "(⩺_⩹)", "ʕ ͡° ʖ̯ ͡°ʔ")
  sadlenny = random.choice(ls_sadlenny)
  await ctx.send(str(sadlenny))
  await ctx.message.delete()

#########################################################################################################################
#generated a happy lenny from the list.
@bot.command()
async def happylenny(ctx):
  ls_happylenny = ("(◕ᗜ◕)", "( ͡°з ͡°)", "(͡• ͜ʖ ͡•)", "(͡• ͜໒ ͡• )", "( ͡^ ͜ʖ ͡^ )", "( ͡° ل͜ ͡°)", "( ͡°ω ͡°)", "( ͡° ᴥ ͡°)", "ヽ(•‿•)ノ", "（〜^∇^ )〜", "(｢• ω •)｢", "╰( ^o^)╮╰( ^o^)╮", "☜(⌒▽⌒)☞")
  happylenny = random.choice(ls_happylenny)
  await ctx.send(str(happylenny))
  await ctx.message.delete()    

#########################################################################################################################
token = os.environ['TOKEN']
bot.run(token)
