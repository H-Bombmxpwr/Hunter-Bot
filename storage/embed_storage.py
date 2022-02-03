import discord
import os




#The embeds for the about page of the bot
def make_list():

  color = 0x280137
  
  embedVar1 = discord.Embed(title="Smrt Bot", description="[Invite Smrt Bot](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=color)
  

  embedVar1.add_field(name= "Commands", value = '`•Page 2: ` API Commands\n`•Page 3: ` Local Commands\n`•Page 4: ` Music Commands\n`•Page 5: ` Moderation Commands\n`•Page 6: ` Games',inline = False)
  
  embedVar2 = discord.Embed(title="Smrt Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=color)
  embedVar2.add_field(name = "API Commands", value = "`          gif: ` + a query to pul the top GIF from tenor\n`         joke: ` Generate a (sometimes nsfw) joke\n  `         xkcd: ` to pull the latest/random xkcd comic\n `         meme: ` to generate a random meme\n `        query: ` Answer virtually any question\n`       trivia: ` to play trivia\n `       animal: ` + an animal to pull a picture of a given animal\n`       insult: ` Generate insults\n`      twitter: ` to interact with twitter \n`    wikipedia: ` + a query to get a wikipedia link\n`   compliment: ` Generate compliments \n`lichess daily: ` Grab the lichess daily puzzle\n")

  embedVar3 = discord.Embed(title="Smrt Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=color)

  embedVar3.add_field(name = "Local Commands", value = " `     bug: ` to spam a user x number of times\n`    bits: ` convert decimal/hex/binary/ascii\n `    help: ` will return more info for every command\n  `    ping: ` Get the latency of the bot\n`   ascii: ` + a < 16 string will print a ascii string of the text\n`userinfo: ` return info of a server member\n")

  
  embedVar4 = discord.Embed(title="Smrt Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=color)
  
  embedVar4.add_field(name = "Music Commands", value = "` music: ` to bring up a list of commands for the music player\n`lyrics: ` pull the lyrics to a requested song")

  embedVar5 = discord.Embed(title="Smrt Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=color)

  embedVar5.add_field(name = "Moderation Commands" , value =  "`help moderation: ` for a list of moderation commands\n•Moderation commands require special permissions to use")

  embedVar6 = discord.Embed(title="Smrt Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=color)

  embedVar6.add_field(name = "Games" , value =  '`fizzbuzz: ` to play fizzbuzz\n -- `fizzbuzz rules` to get the rules of the game', inline = False)

  embeds = [embedVar1,embedVar2,embedVar3,embedVar4,embedVar5,embedVar6]

  return embeds
  