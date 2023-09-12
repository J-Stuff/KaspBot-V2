from redbot.core import commands
from discord.ext import tasks
import discord, random, logging

STATUSES = [
    discord.Activity(name='the cries of the locked up children', type=discord.ActivityType.listening),
    discord.Activity(name='the screams of the damned', type=discord.ActivityType.listening),
    discord.Activity(name='the sound of silence', type=discord.ActivityType.listening),
    discord.Activity(name='games with the devil', type=discord.ActivityType.playing),
    discord.Activity(name='with the devil', type=discord.ActivityType.playing),
    discord.Activity(name='nuclear warhead testing', type=discord.ActivityType.streaming),
    discord.Activity(name='zoomies', type=discord.ActivityType.playing),
    discord.Activity(name='with the FBI', type=discord.ActivityType.playing),
    discord.Activity(name='fortunate son', type=discord.ActivityType.listening),
    discord.Activity(name='Kasper\'s financial crisis', type=discord.ActivityType.watching),
    discord.Activity(name='guess the speed limit', type=discord.ActivityType.playing),
    discord.Activity(name='you call Kasper stimky', type=discord.ActivityType.listening),
    discord.Activity(name='with my tail', type=discord.ActivityType.playing),
    discord.Activity(name='your every move', type=discord.ActivityType.watching),
    discord.Activity(name='... no wait I\'m not listening to you', type=discord.ActivityType.listening),
    discord.Activity(name='your conversations', type=discord.ActivityType.watching),
    discord.Activity(name='with my paw beans', type=discord.ActivityType.playing),
    discord.Activity(name='to Kasper yell at his Truck', type=discord.ActivityType.listening),
    discord.Activity(name='Kasper\'s latest TikTok', type=discord.ActivityType.watching),
    discord.Activity(name='you', type=discord.ActivityType.watching),
    discord.Activity(name='with my toys', type=discord.ActivityType.playing),
    discord.Activity(name='with my food', type=discord.ActivityType.playing),
    discord.Activity(name='with my megaphone', type=discord.ActivityType.playing),
    discord.Activity(name='with my squeaky toys', type=discord.ActivityType.playing),
    discord.Activity(name='in my daydreams', type=discord.ActivityType.playing),
]


class RotatingStatus(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.status_loop.start()
        super().__init__()


    @tasks.loop(minutes=5)
    async def status_loop(self):
        logging.info("Changing status")
        await self.bot.change_presence(activity=random.choice(STATUSES))

    @status_loop.before_loop
    async def before_status_loop(self):
        logging.info("Waiting for bot to be ready (likely awaiting an open connection to Discord)")
        await self.bot.wait_until_ready()
