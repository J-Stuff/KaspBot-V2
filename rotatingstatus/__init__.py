from .rotatingStatus import RotatingStatus
from redbot.core import commands



async def setup(bot:commands.Bot):
    await bot.add_cog(RotatingStatus(bot))