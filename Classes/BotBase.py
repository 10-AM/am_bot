import discord
from discord.ext import commands
from Classes.Config import Configs
from Classes.Data import Data
import json

class BotBase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.configs = Configs()
        self.data = Data()

    def get_base_embed(self, title):
        embed = discord.Embed()
        embed.title = title
        embed.colour = discord.Colour(16740859)
        return embed

    async def send_ignore(self, ctx):
        await ctx.send("NotImplementedException")