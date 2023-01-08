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

FunFactVariable = [
    "This Bot's code name is EnceBot. It's short for Enceladus Bot.",
    "The owner of the game actually added this to the offical discord, don't believe me? Join the server and look in the list."
]

ToothpasteVariable = [
    "i dont feel so good",
    ".. that tasted iffy. not good.",
    "how real is everything anyway? ..... .. things like these make me want to cry. .....",
    "what has happened to me..?",
    "you're not here."
]
TrashedOreoVariable = [
    "why'd you do that?",
    "... why?",
    "you threw a perfectly good oreo away!"
]
MadnessLevel = 0

TeaVariable = [
    "..tea? sure, why not.",
    "you want me to drink tea? okay.",
    "you want me to drink that? okay"
]


BinEncePlushVar = [
    "would you like it if i threw you away instead?",
    "but.. he was my friend though.",
    "thats mean. very mean.",
    "why would you do something like that to someone?"
]

owoVar = [
    "why would you say something like that?",
    "... owo? what is an owo?",
    "what is an owo anyway? i'm confused. it confuses me."
]
#Intents, needed to read messages.
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='e!', intents=intents)

#Join Embed.        
@bot.event
async def on_guild_join(guild):
    channel = discord.utils.get(guild.channels, name="general")
    embedHi = discord.Embed(
            title = "Hello Friends! I can't wait to meet all of you!",
            description = "I use the Prefix e! to talk to you! e!help for all the things I can do! Looking forward to meeting everyone!",
            colour = discord.Colour.light_grey())
    embedHi.set_thumbnail(
            url = "https://media.discordapp.net/stickers/1007808445606527067.webp?size=320"
            )
    embedHi.set_footer(
                text=random.choice(FooterVariable))
    await channel.send(embed=embedHi)

#Bot status randomized.
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(random.choice(StatusVariable)))
    bot.sync_commands
    

#Hello Command    
@bot.slash_command(description="Say hi to the boy!")
async def hello(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel - 1
    print("Ence's Madness Level is " + str(MadnessLevel) + " Right now!")
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond(random.choice(HelloVariable))
    

#Random Command S3P Requested.
@bot.slash_command(description="Some random command S3P requested.")
async def garkalmabdildbajbloug(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond("what..?")

#Ping Test command
@bot.slash_command(description="Test command, just tells you if the bot is working or not")
async def ping(ctx):
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.respond('Pong')

#A class setup for discord's dropdown UI
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "yellow guy"),
            discord.SelectOption(label = "too many oreos"),
            discord.SelectOption(label = "the random guy"),
            discord.SelectOption(label = "dream #1"),
            discord.SelectOption(label = "crayons"),
            discord.SelectOption(label = "malware"),
            discord.SelectOption(label = "alone"),
            discord.SelectOption(label = "memories"),
            discord.SelectOption(label = "local area"),
            discord.SelectOption(label = "secret"),
            discord.SelectOption(label = "antares"),
            discord.SelectOption(label = "antares 2/1"),
            discord.SelectOption(label = "something else"),
            discord.SelectOption(label = "relatives"),
            discord.SelectOption(label = "sun")
        ]
        super().__init__(placeholder = "Select a story. **This Feature is in Beta**", max_values=1,min_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "yellow guy":
            await interaction.response.send_message("oh him? that guy who promised me a truck full of oreos and never gave me it? i dont remember much about him... i think his name was s3p or something?",ephemeral=True)
        elif self.values[0] == "too many oreos":
            await interaction.response.send_message("oh yeah once i ate too many oreos. i wouldnt recommend it. you feel terrible the whole day. it sucks.",ephemeral=True)
        elif self.values [0] == "the random guy":
            await interaction.response.send_message("theres this guy who i see every few days. that guy mindlessly goes around searching for stuff i guess. perhaps he has something on his mind other than oreos. he likes to feed me tea.",ephemeral=True)
        elif self.values [0] == "dream #1":
            await interaction.response.send_message("i had this dream once. i was walking around waiting for a person to come by to see me. i tripped on a rock and fell. next thing i know im in the air. then i woke up. bad dream i know, but it was interesting.",ephemeral=True)
        elif self.values [0] == "crayons":
            await interaction.response.send_message("yknow, someone was once kind enough to leave me a gift, it was a strange little gift, it was all colorful, and in pieces. they even left marks on my hands!so i tried them out on some walls and.. it left marks on there too! that's okay though. i think some of these walls look prettier now.",ephemeral=True)
        elif self.values [0] == "malware":
            await interaction.response.send_message("you probably won't believe me, but sometimes when i'm just chilling, there's a figure that sometimes appears and scare me. it really is scary. maybe one day you'll se here too? if you even believe me, that is.",ephemeral=True)
        elif self.values [0] == "alone":
            await interaction.response.send_message("i get... a little scared when you leave. sometiems the lights go out randomly. sometimes i can swear i just saw a figure dashing, and sometimes it really does feel like the sky had red eyes within.",ephemeral=True )
        elif self.values [0] == "memories":
            await interaction.response.send_message("i realized something. i'm actually starting to remember some things again! some memories are cool, i missed them dearly. some other make me wish i forgot again. but it's fine! a friend got me.. what were they again? i don't know anymore. but i can draw with them! isn't that cool? now i'll never forget again.", ephemeral=True)
        elif self.values [0] == "local area":
            await interaction.response.send_message("its's nice here, isn't it? sometimes people feel the heat. or just the cold.  .. am i people? i mean. others don't think so. they tell me i'm not human. but then what am i? i don't know. they never told me. that's another addition to the things i've missed out on.", ephemeral=True)   
        elif self.values [0] == "secret":
            await interaction.response.send_message("a little secret, but i don't actually live here. i've seen the outside before. that's where i live, actually! until i went to sleep one day. i kept waking up, over and over again.. only to stay here no matter what i tried. maybe someday someone will help me out? although i don't mind talking to you either!", ephemeral=True)   
        elif self.values [0] == "antares story #1":
            await interaction.response.send_message(".. did you know that antares was here?  i don't know why that is. so i went ahead and tried to talk to her! .. she almost attacked me. told me i was a disgrace i think it's better i don't go there now. .. you wanted a happy story? i wish i had one to give you but, not all stories are happy.", ephemeral=True) 
        elif self.values [0] == "antares story #2":
            await interaction.response.send_message(".. you know, there was a time that antares didn't hate me. we're siblings. i can remember that much. and then.. she turned around. resenting humans. ..i know. times sometimes were scary, but.. i tried to convince her that it wasn't all that bad! it didn't work. now she doesn't like me either. atleast you do, right?", ephemeral=True)
        elif self.values [0] == "something else":
            await interaction.response.send_message("a story? i have something better. you know how it sometimes gets scary here? well, thinking of you helps. you sure are a friend! .. i just wish you could come by more", ephemeral=True)
        elif self.values [0] == "relatives":
            await interaction.response.send_message("you know, i'm not the only one. apart from antares, i guess. i had other brothers and sisters too! .. had. the place didn't tell us what happened. confidential or something.. and that too, was times when i wasn't here. i just miss them sometimes. and the outside world.", ephemeral=True) 
        elif self.values [0] == "sun":
            await interaction.response.send_message("did you know the sun never moves here? why are you looking at me? it's strange, isn't it? like, how back in the outside.. you get to watch it set and rise.. and if you catch the moment right, the sky will be orange! sometimes even pink, is the sun really that powerful? .. probably is.", ephemeral=True) 
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

#The actual command itself. Stories command.
@bot.slash_command(description="Stories!")
async def stories(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel - 1
    print("Ence's Madness Level is " + str(MadnessLevel) + " Right now!")
    await ctx.respond("Here's some stories!",view=SelectView())


# Feed Oreo command.
@bot.slash_command(description="Feed the boy an oreo!")
async def feedoreo(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel - 1
    print("Ence's Madness Level is: " + str(MadnessLevel) + " Right now!")
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond(random.choice(FeedOreoVariable))

@bot.slash_command(description="Fun facts about the bot!")
async def funfact(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond(random.choice(FunFactVariable))

@bot.slash_command(description="Throw away an Oreo.")
async def throwawayoreo(ctx):
    global MadnessLevel
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond(random.choice(TrashedOreoVariable))
    MadnessLevel = MadnessLevel + 1

@bot.slash_command(description="Feed him a toothpaste oreo.")
async def toothpasteoreo(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel + 1
    print("Ence's Madness Level is " + str(MadnessLevel) + " Right now!")
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond(random.choice(ToothpasteVariable))


@bot.slash_command(description="Yell bad at him.")
async def bad(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel + 1
    print("Ence's Madness Level is " + str(MadnessLevel) + " Right now!")
    async with ctx.typing():
        await asyncio.sleep(2)
    if MadnessLevel < 10:
        await ctx.respond("SYSTEM: You have added 1 more madness level to Enceladus. Either Feed him an oreo, ask a story, or just say hi to lower his level!")
    elif MadnessLevel >= 10:
        await ctx.respond("your gonna regret that...")


@bot.slash_command(description="Calm him.")
async def calm(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel - 1
    print("Ence's Madness Level is " + str(MadnessLevel) + " Right now!")
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond("Thanks.")

@bot.slash_command(description="Give the boy tea!")
async def givetea(ctx):
    global MadnessLevel
    MadnessLevel = MadnessLevel - 1
    print("Ence's Madness Level is: " + str(MadnessLevel) + " Right now!")
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.respond(random.choice(TeaVariable))


@bot.slash_command(description="Check his mood, sometimes the people in the public server can make him angry...")
async def checkmood(ctx):
    global MadnessLevel
    print("Ence's Madness Level is " + str(MadnessLevel) + " Right now!")
    if MadnessLevel < 0:
        await ctx.respond(f"He is calm, and happy! Madness level = {MadnessLevel}")
    elif MadnessLevel == 0:
        await ctx.respond(f"He is neutral. Madness level = {MadnessLevel}")
    elif MadnessLevel >= 10:
        await ctx.respond(f"He is Mad, Calm him before interacting with him. Madness Level = {MadnessLevel}")
    elif MadnessLevel >= 5:
        await ctx.respond(f"He is annoyed. Getting really close to getting mad at anyone. Madness level = {MadnessLevel}")
    elif MadnessLevel >= 2:
        await ctx.respond(f"He isn't really that happy at the moment.")
    

@bot.slash_command(description = "Send Feedback to the dev!")
async def feedback(ctx, feedback):
    await ctx.respond("Feedback sent! I hope to read your idea and add it!")
    print("Someone sent feedback! The feedback is: " + feedback)
    f = open("feedbacklog.txt", "a")
    f.write(feedback + "\n")
    f.close()

@bot.slash_command(description = "View the Latest Update!")
async def updatelog(ctx):
    await ctx.respond("""Latest Update log:
    
**EnceBot Update V1.0.3**
*The community made me make this one.*
• Added new commands, `/owo`, `/binplush`, and `/trello`
• Removed `/note`
• Fixed issues with the `/checkmood` command always saying `He is calm, and happy! Madness level = x`

Hopefully I will be learning MongoDB soon and allow you guys to get items! This will be before/after midterms week, but it will be a great update if possible!""", ephemeral=True)


@bot.slash_command(description = "Say owo to Enceladus")
async def owo(ctx):
    await ctx.respond(random.choice(owoVar))

@bot.slash_command(description = "Trello for development!")
async def trello(ctx):
    embed = discord.Embed(title= "Development Trello",
    description= """We have a trello you can follow to see development progress! 
    Just click the text that says 'Development Trello' to go to it!""",
    color= discord.Colour.light_gray(),
    url = "https://trello.com/b/lWL8tMZn/encebot-development-progress"
    )    
    await ctx.respond(embed = embed)

@bot.slash_command(description = "Throw away an Ence Plush")
async def binplush(ctx):
    await ctx.respond(random.choice(BinEncePlushVar))

bot.run('[Your Token Goes Here]')
