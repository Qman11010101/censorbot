import configparser
import discord
import re
import os

if os.path.isfile("config.ini"):
    with open("config.ini", mode="r", encoding="utf-8_sig") as cfg:
        config = configparser.ConfigParser()
        config.read_file(cfg)

        replacetext = config["main"].get("replacetext")
        token = config["main"]["token"]
else:
    replacetext = os.environ.get("replacetext")
    token = os.environ.get("token")

client = discord.Client()

with open("NGWORDS.txt", mode="r", encoding="utf-8_sig") as nfs:
    NGWORDS = []
    for ngw in nfs.readlines():
        ngwWoC = re.sub('#.*', '', ngw).strip()
        if ngwWoC != '':
            NGWORDS.append(ngwWoC)

def checkNgWord(text):
    for ngword in NGWORDS:
        if re.search(ngword, text):
            return True
    return False

def replaceNgWord(text, replacedText):
    for ngword in NGWORDS:
        text = re.sub(ngword, replacedText, text).strip()
    return text

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if checkNgWord(message.content):
        await message.delete()
        await message.channel.send(f"{message.author.display_name}が発言しました:\n {replaceNgWord(message.content, replacetext)}")


client.run(token)
