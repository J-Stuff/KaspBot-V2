from redbot.core import commands, app_commands
from discord.ext import tasks
from discord import app_commands as d_app_commands
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
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild_id, i.user.id))
    @app_commands.describe(target="The user to hug.")
    @commands.guild_only()
    async def boop(self, i: discord.Interaction, target:discord.Member):
        """Boop someone!"""
        if target == i.user:
            return await i.response.send_message("You can't boop yourself!", ephemeral=True)
        if target == self.bot.user:
            return await i.response.send_message("You can't boop me!", ephemeral=True)
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
        
    
    @boop.error
    async def boop_error(self, i: discord.Interaction, error):
        if isinstance(error, d_app_commands.errors.CommandOnCooldown):
            await i.response.send_message(f"You're on cooldown! Try again in {round(error.retry_after, 2)} seconds.", ephemeral=True)
        else:
            logging.error("Failed to execute command.")
            logging.exception("Exception:")
            await i.response.send_message("Failed to execute command. `BOOPSLASH-FAIL-UNKNOWNEXCEPTION`", ephemeral=True)

        