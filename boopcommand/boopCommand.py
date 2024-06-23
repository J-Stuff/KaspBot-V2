from redbot.core import commands, app_commands
import discord, random, logging, requests, io


MEDIA = [ # <!> Make sure the size of a file is no larger than 5MB, As the bot has to upload it. Additionally, the file needs to be loaded as a byte object into memory, so large files will cause memory flooding.
    "https://cdn.j-stuff.net/kaspbot/boop_command/1.gif",
    "https://cdn.j-stuff.net/kaspbot/boop_command/2.gif",
    "https://cdn.j-stuff.net/kaspbot/boop_command/3.gif",
]

class BoopCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="boop")
    @app_commands.checks.cooldown(1, 30, key=lambda i: (i.guild_id, i.user.id))
    @app_commands.describe(target="The user to hug.")
    @commands.guild_only()
    async def boop(self, i: discord.Interaction, target:discord.Member):
        """Boop someone!"""
        if target == i.user:
            return await i.response.send_message("You can't boop yourself!", ephemeral=True)
        if target == self.bot.user:
            return await i.response.send_message("You can't boop me!", ephemeral=True)
        try:
            image = requests.get(random.choice(MEDIA))
            image.raise_for_status()
        except:
            logging.error("Failed to fetch image.")
            logging.exception("Exception:")
            return await i.response.send_message("Failed to fetch image. `BOOPSLASH-FAIL-FETCHEXCEPTION`", ephemeral=False)
        
        with io.BytesIO(image.content) as file:
            file = discord.File(file, 'boop.gif')
            
        try:
            await i.response.send_message(content=f"{i.user.mention} *boops* {target.mention}", file=file, ephemeral=False)
        except:
            logging.error("Failed to send image.")
            logging.exception("Exception:")
            return await i.response.send_message("Failed to send image. `BOOPSLASH-FAIL-SENDEXCEPTION`", ephemeral=False)
        