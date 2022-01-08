import discord
import os



#The embeds for the about page of the bot
def make_about():

  embedVar1 = discord.Embed(title="Hunter's Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=0xb00b69).set_footer(text = "Page 1/6 - Made by: H-Bombmxpwr#2243",icon_url = os.getenv('icon'))

  embedVar1.add_field(name= "About", value = 'The Bot is [open sourced](https://replit.com/@HBombmxpwr/Troll-Bot) on replit\n\n=-= `Table of Contents` =-=\n`•Page 2: ` API Commands\n`•Page 3: ` Local Commands\n`•Page 4: ` Music Commands\n`•Page 5: ` Moderation Commands\n`•Page 6: ` Games',inline = False)
  
  embedVar2 = discord.Embed(title="Hunter's Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=0xb00b69).set_footer(text = "Page 2/6 - Made by: H-Bombmxpwr#2243",icon_url = os.getenv('icon'))

  embedVar2.add_field(name = "API Commands", value = "`$i: ` Generate insults\n`$c: ` Generate compliments \n`$j: ` Generate a (sometimes nsfw) joke\n`$lichess daily: ` Grab the lichess daily puzzle\n`$q: ` Answer virtually any question\n`$twitter: ` to interact with twitter \n -- `twitter list commands: ` to get a list of twitter commands.\n`$trivia: ` to play trivia that will track \n -- `$trivia list: ` to get a list of commands\n `$animal: ` + an animal to pull a picture of a given animal\n -- `$animal about: ` to see the suported animals\n `$xkcd: ` to pull the latest/random xkcd comic\n `$meme: ` to generate a random meme\n `$gif: ` + a query to pul the top GIF from tenor")

  embedVar3 = discord.Embed(title="Hunter's Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=0xb00b69).set_footer(text = "Page 3/6 - Made by: H-Bombmxpwr#2243",icon_url = os.getenv('icon'))

  embedVar3.add_field(name = "Local Commands", value = " `$ping: ` to spam a user in the form \'$ping <user_name> <number_of_pings>\' ex. \'$ping @H-Bombmxpwr 13\' \n`$userinfo: ` will return the info for the sender of the message. Takes an optional arguement to get info of a specific user\n`$help: ` will return more info for every command\n`$status: ` will change the status of the bot if given the correct permissions\n `$ascii: ` + a < 16 string will print a ascii string of the text")

  
  embedVar4 = discord.Embed(title="Hunter's Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=0xb00b69).set_footer(text = "Page 4/6 - Made by: H-Bombmxpwr#2243",icon_url = os.getenv('icon'))
  
  embedVar4.add_field(name = "Music Commands", value = "`$music: ` to bring up a list of commands for the music player\n`$lyrics: ` pull the lyrics to a requested song")

  embedVar5 = discord.Embed(title="Hunter's Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=0xb00b69).set_footer(text = "Page 5/6 - Made by: H-Bombmxpwr#2243",icon_url = os.getenv('icon'))


  embedVar5.add_field(name = "Moderation Commands" , value =  "•See `$help moderation` for a list of moderation commands\n•Moderation commands require special permissions to use")

  embedVar6 = discord.Embed(title="Hunter's Bot", description="[Invite](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)", color=0xb00b69).set_footer(text = "Page 6/6 - Made by: H-Bombmxpwr#2243",icon_url = os.getenv('icon'))

  embedVar6.add_field(name = "Games" , value =  '`$fizzbuzz: ` to play fizzbuzz\n -- `$fizzbuzz rules` to get the rules of the game', inline = False)

  embeds = [embedVar1,embedVar2,embedVar3,embedVar4,embedVar5,embedVar6]

  return embeds