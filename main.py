from Classes import Config
from Classes.AMBot import AMBOT
from Classes.DocumentBot import DocumentBot
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="created by taewoo kim")
bot.add_cog(AMBOT(bot))
bot.add_cog(DocumentBot(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = '{0.mention} 어서와요! {1.name}에!'.format(member, guild)
        await guild.system_channel.send(to_send)


@bot.listen()
async def on_message(message):
    # 메시지가 봇 자신이면 처리 안함.
    if message.author == bot.user:
        return

if __name__ == '__main__':
    config = Config.Configs()

    bot.run(config.discord_token)

