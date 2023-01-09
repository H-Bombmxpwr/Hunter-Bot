# Overview
This is a discord bot that does a whole assortment of different tasks. It is by far my biggest coding project ever. 


It is still a work in progress but as of 12/19/2022 it interacts with over a dozen apis, has a plethora moderation commands, has 
an assortment of local commands, has some games to play within the chat, and is able to play music within a voice channel. 

# Usage
Add it to your server [here](https://discord.com/api/oauth2/authorize?client_id=877014219499925515&permissions=8&scope=bot)
Use the $help command to see all commands, or $list to 
see a neater spread of the commands. 

## Warning
The word.txt text file is full of over 1000 swear words from an online source, so if you are sensitive to that I would recommend not opening it.
The profanity filter is all implemented locally and is done using a search trie algorithm that can be found in trie.py and implemented in the client event on_message() of main.py. 

## Current state
The profanity filter is currently turned off and under maintence. The $q command and $coin commands are also under maintence and will not work as intended, but will not effect any other part of the bot


This is my first major coding project that interacts with the greater internet. As a result the code may not be organized the best, but as I learn more I keep changing and evolving the code. 