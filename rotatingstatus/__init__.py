from .rotatingStatus import AboutCommand
from redbot.core import commands



async def setup(bot:commands.Bot):
    await bot.add_cog(AboutCommand(bot))