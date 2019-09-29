import discord
import random

client = discord.Client()  # 接続に使用するオブジェクト

# BOTを起動したときのイベントハンドラ
@client.event
async def on_ready():
    print('ログイン')
    print(client.user.name)  # BOTの名前
    print('------')


# メッセージを受信したときのイベントハンドラ
@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボット自身のメッセージは処理なし
        return

    if message.content == "/こんにちは":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんにちは") 

    elif message.content == "/調子":
        # 埋め込みメッセージ送信
        embed = discord.Embed(title="調子", description=f"BOT{client.user.name}の調子は",
                              color=discord.Colour.red())
        embed.set_thumbnail(url=message.author.avatar_url)
        # Embedにフィールドを追加
        embed.add_field(name="[調子] ", value=random.choice(('最高です', '普通です', '最悪です')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == '/メンバー':
        await message.channel.send(message.guild.members)

    elif message.content == "/ダイレクトメッセージ":
        # ダイレクトメッセージの送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")


# 接続と起動
client.run("NjA1MzI2NzIwNTY4MDAwNTIz.XYnG1g.4FmiJ7zIXy2CkFgdkJw_7YLN6_I")