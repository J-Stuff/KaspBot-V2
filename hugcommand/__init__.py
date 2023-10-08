from .boopCommand import HugCommand
from redbot.core import commands



async def setup(bot:commands.Bot):
    await bot.add_cog(HugCommand(bot))