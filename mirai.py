import discord
import logging

import asyncio
import os
import random
 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler) 
logger.addHandler(handler)

from discord.ext.commands import Bot
my_bot = Bot(command_prefix="★")
@my_bot.event
async def on_read():
    print("Client logged in")
@my_bot.event
async def on_message(message):
	if(message.content.startswith("slap")):
		imgList = os.listdir("./Slapping")
		imgString = random.choice(imgList)
		path = "./Slapping/" + imgString
		msg = await my_bot.send_file(message.channel, path) 
@my_bot.event
async def on_message(message):
	if(message.content.startswith("blanc")):
		imgList = os.listdir("./howaito")
		imgString = random.choice(imgList)
		path = "./howaito/" + imgString
		msg = await my_bot.send_file(message.channel, path) 
my_bot.run("-")
