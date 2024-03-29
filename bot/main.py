import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from datetime import datetime
#import psycopg2

load_dotenv()

my_secret = os.environ['TOKEN']
#DATABASE_URL = os.environ['DATABASE_URL']

client = discord.Client(intents=discord.Intents.all())
intents=discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents, help_command=None)
get = discord.utils.get
#conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
from datetime import datetime

def getDuration(then, now = datetime.now(), interval = "default"):

    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds() 
    
    def years():
      return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
      if seconds != None:
        return divmod(seconds, 1)   
      return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "{} years, {} days, {} hours, {} minutes, and {} seconds".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]


@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
    botactivity = discord.Activity(type=discord.ActivityType.streaming,
                                   name="brain rot simulator")
    await client.change_presence(activity=botactivity)

@client.command(pass_context=True)
async def handle(ctx, user: discord.Member):
    role = get(ctx.message.guild.roles, name="CURRENT HANDLE HOLDER")
    if role in user.roles:
        await ctx.send("he is already rng carried retard")
    else:
        for member in ctx.message.guild.members:
            if role in member.roles:
                await member.remove_roles(role)
                await user.add_roles(role)
                msg_2 = await ctx.send(
                    f"<@!{user.id}> is now officially the rng carried shitter keep yourself safe"
                )
                global handle
                handle = msg_2.created_at
                #print(msg_time)
                #created = datetime.strptime(created_1, "%d/%m/%Y %H:%M:%S")
                await ctx.send(f"handle dropped at: {handle} UTC")
                print(handle)
                return



@client.command(pass_context=True)
async def duration(ctx):
    global handle
    then = handle
    now = datetime.now()    
    await ctx.send(
        f"it's been {getDuration(then, now)} since a handle"
    )

@client.command(pass_context=True)
async def help(ctx):
    await ctx.send(
        "```!handle @user when they are rng carried\n!m7 to ping all m7 players\n!m6 to ping all m6 players```"
    )


@client.command(pass_context=True)
async def m7(ctx):
    await ctx.send(
        f"<@&1017553353145856032> <@&1017553432065871892> <@&1017553483743899658> <@&1017553555474894889> <@&1017553610160226345>"
    )
    return

@client.command(pass_context=True)
async def m6(ctx):
    await ctx.send(
        f"<@&1017532448684396604> <@&1017532717807710349> <@&1017532798904586321> <@&1017532908237496402> <@&1017532971303043154>"
    )
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if any(x in message.content for x in [
            "unlocked Shadow Warp", "unlocked Implosion",
            "unlocked Wither Shield"
    ]):
        await message.channel.send('W now apparently')
    if any(y in message.content for y in [
            "unlocked Necron Dye"
    ]):
        await message.channel.send('massive L')
    if "vanishcc unlocked Necron's Handle" in message.content:
        await message.channel.send('rng carried account')
    if "cceli unlocked Necron's Handle" in message.content:
        await message.channel.send('nice overflux')
    if "dce88 unlocked Necron's Handle" in message.content:
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/993910132478058599/1003477088105402478/Badlion_Client_2022.07.31_-_21.02.26.27.DVR_Trim_Trim_Trim.mp4'
        )
    if "RMV6 unlocked Necron's Handle" in message.content:
        await message.channel.send('foxy is a furry btw')
    if "heykms unlocked Necron's Handle" in message.content:
        await message.channel.send('abubu')
    if "JayceeSochi unlocked Necron's Handle" in message.content:
        await message.channel.send('bring back nicejc123')
    if "LOadjoinDyou unlocked Necron's Handle" in message.content:
        await message.channel.send('omg 1b profit fr!!!')
    if "3is3 unlocked Necron's Handle" in message.content:
        await message.channel.send('dce88: omg you are so rng cairied')
    if "Shqckwave unlocked Necron's Handle" in message.content:
        await message.channel.send(
            'idk good job')
    if "widealex unlocked Necron's Handle" in message.content:
        await message.channel.send('monkey')
    if "kirtricky unlocked Necron's Handle" in message.content:
        await message.channel.send('Nice Bro')
    if "FactorialTime unlocked Necron's Handle" in message.content:
        await message.channel.send('regular ppl 1 furries 0')
    if "orjiin unlocked Necron's Handle" in message.content:
        await message.channel.send('idk gg ig') 
    #formats = ['jpg', 'png', 'gif', 'svg', 'jpeg', 'imgur', 'webp']
    #attachments = [f for f in message.attachments if f.filename.split('.')[-1] in formats]
    attachments = message.attachments
    embeds = message.embeds
    if message.author.id == 259729734420791298 and attachments:
        await message.delete()
        await message.channel.send('furry tax')
    if message.author.id == 259729734420791298 and embeds:
        await message.delete()
        await message.channel.send('furry tax')
    #links = ['imgur.com']
    #link = [word for word in message.content.lower() if word in links]
    if message.author.id == 259729734420791298 and any(z in message.content for z in [
            "imgur.com", "https"
    ]):
        await message.delete()
        await message.channel.send('furry tax')
    for file in message.attachments:
        if file.filename.endswith((".txt")) and message.author.id == 259729734420791298:
            await message.delete()
            await message.channel.send('furry tax')
    if "!!" in message.content:
        pass
    else:
        await client.process_commands(message)


@handle.error
async def handle_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ping someone that dropped a handle or !help")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("that command doesn't exist nice try zzzz")

client.run(my_secret)
