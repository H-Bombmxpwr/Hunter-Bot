import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive
from Lists_Storage import *
from functions import *
import music,services,games,mod #import the cogs
from functions import check_carrot,punish_user
import time
from trie import Trie


cogs = [music,services,mod,games]

client = commands.Bot(command_prefix='$',intents = discord.Intents.all())


for i in range(len(cogs)):
  cogs[i].setup(client)


trie = Trie()
table = {
    "\"": None,
    "'": None,
    "-": None,
    "`": None,
    "~": None,
    ",": None,
    ".": None,
    ":": None,
    ";": None,
    "_": None
}



def buildTrie():
    file = open("words.txt", 'r')

    for line in file:
        line = line.strip()
        trie.insert(line)
    file.close()



@client.event
async def on_ready():
  print("Trie is building......")
  buildTrie()
  print("Trie is built. Ready to read messages.\n")
  print('It is still working probably \n{0.user} do be online'.format(client))
  print('=------------------------------=')
  



@client.event 
async def on_command_error(ctx, error): #detects if a command is valid
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Error", description=f"Command \'" + ctx.message.content + "   \' not found. \nUse $about or $help for a list of commands", color=0xff0000) 
        await ctx.send(embed=em)



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  text = message.content.lower()
  text = text.translate(str.maketrans(table))
  author_id = message.author.id

  if author_id != 239605426033786881: #profanity filter
        isClean = True
        message_word_list = text.split()
        for word in message_word_list:
            if trie.search(word):
                isClean = False
                break
        if not isClean:
            await message.channel.send(punish_user(author_id))



  # thursday!!!
  if any(word in text for word in days):
    time_zone = -6
    
    if int((int(time.time()) + (time_zone * 3600))/86400) % 7 == 0:
      await message.channel.send("```\nIt's Thursday, Happy Thursday!\n    \nhttp://isitthursday.org/\n```")
    else:
      await message.channel.send("```\nIt's not Thursday\n    \nYou bozo\n```")
 
  
  #the dan
  if any(word in text for word in thedan):
    emojis = ['🎸','🎹','🎷','🥁', '🎤']
    for emoji in emojis:
      await message.add_reaction(emoji)
    await message.channel.send("```\nI LOVE STEELY DAN!\n```")

  
  #Carrot agree function
  if check_carrot(text) == 1: 
    await message.channel.send(message.content + '^')

  
  await client.process_commands(message)



keep_alive()
client.run(os.getenv('token'))