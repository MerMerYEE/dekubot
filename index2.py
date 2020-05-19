import discord 
from discord.ext import commands
import asyncio
import youtube_dl
import youtube_search


client = commands.AutoShardedBot(command_prefix = '데쿠야 ')



@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', (f"{int(client.latency *1000)}ms")]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(3)


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = [ ]
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f' banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    user=ctx.mentions[0]
    try:
        await ctx.guild.unban(user)
    except:
            await ctx.send("언벤을 실패했어....")
    else:
            await ctx.send(f' 언벤 {user.mention}')
            return

@client.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "뮤트":
            await member.add_roles(role)
            await ctx.send("{} 얘를 {} 얘가 뮤트 시켰어" .format(member.mention, ctx.author.mention))
            return

            overwrite = discord.permissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="뮤트")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole, overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} 얘를 {} 얘가 뮤트 시켰어" .format(member.mention, ctx.author.mention))


@client.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "뮤트":
            await member.remove_roles(role)
            await ctx.send("{} 이사람을 {} 얘가 언뮤트했어" .format(member.mention, ctx.author.mention))
            return

@client.command(aliases=["echo"])
async def say(ctx, *, words):
    await ctx.send(words)

@client.command()
async def 사진(ctx):
    embed = discord.Embed()
    file = discord.File("미도리야.jpg")
    embed.set_image(file=file)
    await ctx.send(embed=embed)



client.run("NzA0NjE5MDI1MjU4NTEyNDQ0.Xqj2Lw.m8BfAv8ZQlMDDcxnnDb4Grnbxsc")