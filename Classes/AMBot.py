import discord
from discord.ext import commands
from Classes.BotBase import BotBase

class AMBOT(BotBase):
    def __init__(self, bot):
        super(AMBOT, self).__init__(bot)

    @commands.command(pass_context=True)
    async def status(self, ctx):
        #await self.send_ignore(ctx)
        embed = self.get_base_embed("스테이터스")
        status_dict = self.data.get_bot_status()
        f = "활동 : {time}\n신장: {line}\n무게: {size}\n"
        embed.description = f.format(time=status_dict["time"], line=status_dict["lines"], size=status_dict["size"])
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    async def info(self, ctx):
        #await self.send_ignore(ctx)
        embed = self.get_base_embed(self.data.desc_dict["title"])
        embed.description = self.data.desc_dict["content"].format(developer="<@270884515952459776>")
        embed.set_footer(text=self.data.desc_dict["footer"])
        await ctx.send(embed=embed)