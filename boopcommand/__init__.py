from .boopCommand import BoopCommand
from redbot.core import commands



async def setup(bot:commands.Bot):
    await bot.add_cog(BoopCommand(bot))