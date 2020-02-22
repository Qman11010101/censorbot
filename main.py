import configparser
import discord
import re

with open("config.ini", mode="r", encoding="utf-8_sig") as cfg:
    config = configparser.ConfigParser()
    config.read_file(cfg)

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

def replaceNgWord(text, replacedText="[検閲済]"):
    for ngword in NGWORDS:
        text = re.sub(ngword, replacedText, text).strip()
    return text

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if checkNgWord(message.content):
        await message.delete()
        await message.channel.send(f"{message.author.display_name}が発言しました:\n {replaceNgWord(message.content, config['main'].get('replacetext'))}")


client.run(config["main"]["token"])
