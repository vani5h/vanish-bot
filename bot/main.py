import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound
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

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
    botactivity = discord.Activity(type=discord.ActivityType.streaming,
                                   name="prefix = !")
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
                handle = msg_2.created_at
                #print(msg_time)
                #created = datetime.strptime(created_1, "%d/%m/%Y %H:%M:%S")
                await ctx.send(f"handle dropped at: {handle} UTC")
                print(handle)
                return


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
        await message.channel.send('W')
    if any(y in message.content for y in [
            "unlocked Necron Dye"
    ]):
        await message.channel.send('massive L')
    if "avanish unlocked Necron's Handle" in message.content:
        await message.channel.send('nice rng')
    if "psychosaur unlocked Necron's Handle" in message.content:
        await message.channel.send('nice hype')
    if "dce88 unlocked Necron's Handle" in message.content:
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/993910132478058599/1003477088105402478/Badlion_Client_2022.07.31_-_21.02.26.27.DVR_Trim_Trim_Trim.mp4'
        )
    if "RMV6 unlocked Necron's Handle" in message.content:
        await message.channel.send('foxy is a furry btw')
    if "heykms unlocked Necron's Handle" in message.content:
        await message.channel.send('abubu')
    if "nicejc123 unlocked Necron's Handle" in message.content:
        await message.channel.send('no.  no.  no.')
    if "LOadjoinDyou unlocked Necron's Handle" in message.content:
        await message.channel.send('omg 1b profit fr!!!')
    if "3is3 unlocked Necron's Handle" in message.content:
        await message.channel.send('dce88: omg you are so rng cairied')
    if "Shqckwave unlocked Necron's Handle" in message.content:
        await message.channel.send(
            'i cant believe you dropped necrons handle in teraria')
    if "widealex unlocked Necron's Handle" in message.content:
        await message.channel.send('monkey')
    if "kirtricky unlocked Necron's Handle" in message.content:
        await message.channel.send('quagmire')
    if "notoli unlocked Necron's Handle" in message.content:
        await message.channel.send('nice slayer')
    if "orjiin unlocked Necron's Handle" in message.content:
        await message.channel.send('idk gg ig') 
    formats = ['jpg', 'png', 'gif', 'svg', 'jpeg', 'imgur']
    attachments = [f for f in message.attachments if f.filename.split('.')[-1] in formats]
    if message.author.id == 259729734420791298 and attachments:
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
