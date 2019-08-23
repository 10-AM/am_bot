import discord
from discord.ext import commands
from Classes.BotBase import BotBase

class DocumentBot(BotBase):
    def __init__(self, bot):
        super(DocumentBot, self).__init__(bot)

    @commands.command(pass_context=True)
    async def onboarding(self, ctx):
        await self.send_ignore(ctx)