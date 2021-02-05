import discord

client = discord.Client()

@client.event
async def on_ready():
    print("루사봇이 성공적으로 실행되었습니다.")
    game = discord.Game('루사야 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    if message.content.startswith('루사야 나봇'):
        embed = discord.Embed(title="우루사 나이트봇 명령어 X 디스코드 루사봇", description="https://nightbot.tv/t/vlg_urs4/commands", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="수정은 K.G#9820로 디엠주세요! • ❌:메세지 삭제") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("❌")

    if message.content.startswith('루사야 스펙'):
        embed = discord.Embed(title="우루사 스펙 보러가기", description="파란 글씨를 클릭해주세요!", url="https://specs.gg/vlg_urs4", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="수정은 K.G#9820로 디엠주세요! • ❌:메세지 삭제") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.  
        await msg.add_reaction("❌")

    if message.content.startswith('루사야 대회'):
        embed = discord.Embed(title="최신 배틀그라운드 E스포츠 알림", description="개발자 : K.G#9820", url="https://youtu.be/Da1yoCdl1sY", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://i.ytimg.com/vi/9lCuKKvjikY/maxresdefault.jpg")
        embed.set_footer(text="수정은 K.G#9820로 디엠주세요! • ❌:메세지 삭제") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('루사야 우손실'):
        embed = discord.Embed(title="우손실 방지 위원회입니다", description="개발자 : K.G#9820", url="https://youtu.be/Da1yoCdl1sY", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="우손실 방지 방법", value="루싸가 **배틀그라운드 프로스크림 하이라이트**라는 영상을 추천드려요! 한번보면 당분간 우손실 방지!      ***파란색 글을 클릭하시면 영상으로 이동됩니다***", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/798708827851718656/807128983497343006/mqdefault_6s.png")
        embed.set_footer(text="수정은 K.G#9820로 디엠주세요! • ❌:메세지 삭제") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("❌")

    if message.content.startswith('루사야 도움말'):
        embed = discord.Embed(title="우루사 디스코드 봇 명령어 사용방법", description="개발자 : K.G#9820", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="루사야 나봇", value="우루사가 나이트봇에 추가한 명령어들을 모두 봇에게 불러와서 나이트봇 명령어들을 루사에게도 만나보세요", inline=True)
        embed.add_field(name="루사야 우손실", value="우루사가 나이트봇에 추가한 명령어들을 모두 봇에게 불러와서 나이트봇 명령어들을 루사에게도 만나보세요", inline=True)
        embed.set_footer(text="다음페이지는 1️⃣:1번 페이지, 2️⃣:2번 페이지,❌:메세지 삭제 • 1/2 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('codenameurs4helppage1'):
        await message.delete()
        embed = discord.Embed(title="우루사 디스코드 봇 명령어 사용방법", description="개발자 : K.G#9820", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="루사야 나봇", value="우루사가 나이트봇에 추가한 명령어들을 모두 봇에게 불러와서 나이트봇 명령어들을 루사에게도 만나보세요", inline=True)
        embed.add_field(name="루사야 우손실", value="우루사가 나이트봇에 추가한 명령어들을 모두 봇에게 불러와서 나이트봇 명령어들을 루사에게도 만나보세요", inline=True)
        embed.set_footer(text="다음페이지는 1️⃣:1번 페이지, 2️⃣:2번 페이지, ❌:메세지 삭제 • 1/2 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("❌")
        
    if message.content.startswith('codenameurs4esportspage2'):
        await message.delete()
        embed = discord.Embed(title="최신 배틀그라운드 E스포츠 알림", description="2021 PGI.S 일정 총정리", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.akamai.steamstatic.com/steamcommunity/public/images/clans/27971017/ab660f580cc0f1d0811ae7c3b0f8bbd56d5e9437.jpg")
        embed.set_footer(text="수정은 K.G#9820로 디엠주세요! • ❌:메세지 삭제") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("❌")

    if message.content.startswith('codenameurs4helppage2'):
        await message.delete()
        embed = discord.Embed(title="우루사 디스코드 봇 명령어 사용방법", description="개발자 : K.G#9820", color=0xff9a00) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="루사야 스펙", value="우루사의 배그 설정, 컴퓨터 사양까지, 그리고 아주 은밀한거 까지 ^V^", inline=True)
        embed.add_field(name="루사야 대회", value="최신 배틀그라운드 E스포츠 정보, 일정까지 알려드려요!", inline=True)
        embed.set_footer(text="다음페이지는 1️⃣:1번 페이지, 2️⃣:2번 페이지, ❌:메세지 삭제 • 1/2 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("❌")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    
    if str(reaction.emoji) == "1️⃣":
        await reaction.message.channel.send("codenameurs4helppage1")
        await reaction.message.delete()

    if str(reaction.emoji) == "2️⃣":
        await reaction.message.channel.send("codenameurs4helppage2")
        await reaction.message.delete()

    if str(reaction.emoji) == "3️⃣":
        await reaction.message.channel.send("codenameurs4esportspage2")
        await reaction.message.delete()

    if str(reaction.emoji) == "❌":
        await reaction.message.delete()


client.run('TOKEN')
