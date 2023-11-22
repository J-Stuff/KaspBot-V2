from .attachmentLogger import AttachmentLogging
from redbot.core.bot import Red as Bot


async def setup(bot:Bot):
    await bot.add_cog(AttachmentLogging(bot))