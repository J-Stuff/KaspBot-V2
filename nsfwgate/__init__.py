from .gate import Gate
from redbot.core import commands

async def setup(bot:commands.Bot):
    await bot.add_cog(Gate(bot))