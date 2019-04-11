import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
from discord import Game

client = commands.Bot(command_prefix='/')
client.remove_command('help')

@client.event
async def on_ready():
  print('Der Bot erfolgreich eingelogt als')
  print(client.user.name)
  
  await client.change_presence(game=discord.Game(name='die Alpha Version | /help'))

@client.event
async def on_member_join(member):
  print('Ich habe erfahren,dass der User' + member.name + 'gejoint ist')
  await client.send_message(member, 'Vielen Dank, dass du dem Server  gejoint bist._. Schaue doch auch mal in die Regeln, um dir sie genau durchzulesen! Wenn du dies gemacht hast, kannst du mit anderen Leuten chatten. Viel Spaß wünscht dir das Server Team.')
  print('Send message to ' + member.name)

@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(
      colour = discord.Colour.red()
  )

  embed.set_author(name='Befehlsliste:')
  embed.add_field(name='/ban', value='Bannt einen User von dem Netzwerk!', inline=False)
  embed.add_field(name='/kick', value='Kickt einen User von dem Netzwerk!', inline=False)
  embed.add_field(name='/warn', value='Sendet eine Warnungsnachricht an den User', inline=False)
  embed.add_field(name='/meme1', value='Sendet ein Meme', inline=False)
  embed.add_field(name='/meme2', value='Sendet ein Meme', inline=False)
  embed.add_field(name='/meme3', value='Sendet ein Meme', inline=False)
  embed.add_field(name='/invite', value='Sendet einen Link vom Bot', inline=False)
  embed.add_field(name='/version', value='Zeigt die Version des Bots', inline=False)

  await client.send_message(author, embed=embed)
  await client.say('Ich habe dir eine Nachricht per PN gesendet :pencil:')
  
@client.command()
async def version():
  await client.say('Der Bot befindet sich noch in der Version Alpha|v 0.2.1')
  
@client.command()
async def invite():
  await client.say('Hier kannst du mich auf deinen Server holen: https://discordapp.com/api/oauth2/authorize?client_id=563114625500053505&permissions=8&scope=bot')
  
@client.command(pass_context=True)
async def warn(ctx,target:discord.Member):
  await client.send_message(target,'Du wurdest so eben verwarnt, da du offensichtlich gegen eine Regel des Servers verstoßen hast!')

@client.command(pass_context=True)
async def ban(ctx,target:discord.Member):
  await client.ban(target)
  await client.say('Der User wurde erfolgreich von diesem Netzwerk gebannt!')

@client.command(pass_context=True)
async def kick(ctx,target:discord.Member):
  await client.kick(target)
  await client.say('Der User wurde erfolgreich von diesem Netzwerk gekickt!')

@client.command()
async def meme1():
  await client.say('https://imgflip.com/i/2y5w24')

@client.command()
async def meme2():
  await client.say('https://imgflip.com/i/2y5yhn')

@client.command()
async def meme3():
  await client.say('https://imgflip.com/i/2y62nb')
  
@client.command()
async def meme4():
  await client.say('**Es werden weitere Memes mit den folgenden Updates kommen!**')

client.run(str(os.environ.get('BOT_TOKEN')))
