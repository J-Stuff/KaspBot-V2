from redbot.core import commands, app_commands
from discord.ext import tasks
import discord, random, logging, requests, io


MEDIA = [ # <!> Make sure the size of a file is no larger than 5MB, As the bot has to upload it. Additionally, the file needs to be loaded as a byte object into memory, so large files will cause memory flooding.
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077805682931281941/IMG_9773.gif",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077805699242934364/IMG_9772.gif",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077806051296030720/image0.gif"
]

class BoopCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="boop")
    @commands.guild_only()
    async def boop(self, i: discord.Interaction, target:discord.Member):
        """Boop someone!"""
        await i.response.defer(ephemeral=False, thinking=True)
        try:
            image = requests.get(random.choice(MEDIA))
        except:
            logging.error("Failed to fetch image.")
            logging.exception("Exception:")
            return await i.followup.send("Failed to fetch image. `BOOPSLASH-FAIL-FETCHEXCEPTION`", ephemeral=False)
        
        with io.BytesIO(image.content) as file:
            file = discord.File(file, 'boop.gif')
            
        try:
            await i.followup.send(content=f"{i.user.mention} *boops* {target.mention}", file=file, ephemeral=False)
        except:
            logging.error("Failed to send image.")
            logging.exception("Exception:")
            return await i.followup.send("Failed to send image. `BOOPSLASH-FAIL-SENDEXCEPTION`", ephemeral=False)

        