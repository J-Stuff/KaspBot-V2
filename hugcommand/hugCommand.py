from redbot.core import commands, app_commands
from discord.ext import tasks
import discord, random, logging, requests, io


MEDIA = [ # <!> Make sure the size of a file is no larger than 5MB, As the bot has to upload it. Additionally, the file needs to be loaded as a byte object into memory, so large files will cause memory flooding.
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841663394861126/db426e94329aa0abda9ab24fec33c7b2.jpg",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841663680057354/images.jpg?",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841663898165330/n6ccaoxhebh91.jpg",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841664166613032/qg5y0uyo2wr91.png",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841664464392302/qjmvb0b22yl81.jpg",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841664749608971/Screenshot_2023-01-23_131627.png",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841665009668106/Screenshot_20221128_213135.png",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841665273897010/Screenshot_20221208_133404.png",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841665643008010/Screenshot_20221208_133414.png",
    "https://cdn.discordapp.com/attachments/1077805633249742879/1077841665961758800/Screenshot_20221211_113729.png"
]

class HugCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hug")
    @commands.guild_only()
    async def hug(self, i: discord.Interaction, target:discord.Member):
        """Hug someone!"""
        await i.response.defer(ephemeral=True, thinking=True)
        try:
            image = requests.get(random.choice(MEDIA))
        except:
            logging.error("Failed to fetch image.")
            logging.exception("Exception:")
            return await i.followup.send("Failed to fetch image. `HUGSLASH-FAIL-FETCHEXCEPTION`", ephemeral=False)
        
        with io.BytesIO(image.content) as file:
            file = discord.File(file, 'hug.jpg')
            
        try:
            await i.followup.send(content=f"{i.user.mention} *hugs* {target.mention}", file=file, ephemeral=False)
        except:
            logging.error("Failed to send image.")
            logging.exception("Exception:")
            return await i.followup.send("Failed to send image. `HUGSLASH-FAIL-SENDEXCEPTION`", ephemeral=False)
        