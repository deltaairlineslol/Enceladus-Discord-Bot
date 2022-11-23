import discord
import random
import asyncio
from discord.utils import find
from discord.ext import commands

#Variables needed for commmands/statuses
HelloVariable = [
    'Hello!',
    'Hi!',
    'Hello there!',
    'Hello friend!',
    'Hi Friend!'
]

StatusVariable = [
    'Oreo Simulator',
    'Wii Sports',
    'OG Game by Valerist',
    'with friends',
    'The Stanley Parable: Ultra Deluxe Edition',
    'Half-Life 3: Deluxe Edition'
]

FooterVariable = [
    "Hi Chat!!!",
    "This was an automated task.. Ofc it was, why wouldn't it be?",
    "Enceladus, But he's a discord Bot.",
    "Enceladus became real."
]

FeedOreoVariable = [
    'do you have more?',
    'do you happen to have more..?',
    'delicious, but more is appreciated!'
]
#Intents, needed to read messages.
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='e!', intents=intents)

#Join Embed.        
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embedHi = discord.Embed(
                title = "Hello Friends! I can't wait to meet all of you!",
                description = "I use the Prefix e! to talk to you! e!help for all the things I can do! Looking forward to meeting everyone!",
                url = "https://sites.google.com/view/enceladus-bot/home",
                colour = discord.Colour.light_grey())
            embedHi.set_thumbnail(
                url =
                "https://media.discordapp.net/stickers/1007808445606527067.webp?size=320"
            )
            embedHi.set_footer(
                text=random.choice(FooterVariable))
            await channel.send(embed=embedHi)

#Bot status randomized.
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(random.choice(StatusVariable)))

#Hello Command    
@bot.command()
async def hello(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.send(random.choice(HelloVariable))

#Random Command S3P Requested.
@bot.command()
async def garkalmabdildbajbloug(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.send("what..?")

#Ping Test command
@bot.command()
async def ping(ctx):
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send('Pong')

#A class setup for discord's dropdown UI
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Yellow Guy"),
            discord.SelectOption(label = "Too Many Oreos"),
            discord.SelectOption(label = "The Random Guy"),
            discord.SelectOption(label = "Dream #1")
        ]
        super().__init__(placeholder = "Select a story. **This Feature is in Beta**", max_values=1,min_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Yellow Guy":
            await interaction.response.send_message("oh him? that guy who promised me a truck full of oreos and never gave me it? i dont remember much about him... i think his name was s3p or something?",ephemeral=True)
        elif self.values[0] == "Too Many Oreos":
            await interaction.response.send_message("oh yeah once i ate too many oreos. i wouldnt recommend it. you feel terrible the whole day. it sucks.",ephemeral=True)
        elif self.values [0] == "The Random Guy":
            await interaction.response.send_message("theres this guy who i see every few days. that guy mindlessly goes around searching for stuff i guess. perhaps he has something on his mind other than oreos. he likes to feed me tea.",ephemeral=True)
        elif self.values [0] == "Dream #1":
            await interaction.response.send_message("i had this dream once. i was walking around waiting for a person to come by to see me. i tripped on a rock and fell. next thing i know im in the air. then i woke up. bad dream i know, but it was interesting.",ephemeral=True)
        
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

#The actual command itself. Stories command.
@bot.command()
async def stories(ctx):
    await ctx.send("Here's some stories!",view=SelectView())

#Commands Command.
@bot.command()
async def commands(ctx):
            embedCommands = discord.Embed(
                title = "Here's the commands!",
                description = "You can find all of the commands at: https://sites.google.com/view/enceladus-bot/commands",
                url = "https://sites.google.com/view/enceladus-bot/commands",
                colour = discord.Colour.light_grey())
            embedCommands.set_thumbnail(
                url =
                "https://media.discordapp.net/stickers/1007808445606527067.webp?size=320"
            )
            embedCommands.set_footer(
                text=random.choice(FooterVariable))
            await ctx.send(embed=embedCommands)

# Feed Oreo command.
@bot.command()
async def feedoreo(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.send(random.choice(FeedOreoVariable))




bot.run('[Your Token Goes Here]')
