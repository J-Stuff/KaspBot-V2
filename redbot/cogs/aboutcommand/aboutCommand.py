from redbot.core import commands, app_commands
import discord

VERSION = "2.0.0"

class AboutCommand(commands.Cog):


    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.bot

    @commands.command(name="about")
    async def about(self, ctx:commands.Context):
        embed = discord.Embed(title="KaspBot - About", description=f"KaspBot Version {VERSION}\nUses a fork of [Red Bot](https://github.com/Cog-Creators/Red-DiscordBot) and is modified by `jstuff`", color=discord.Color.blue())
        embed.add_field(name="LICENSE", value="KaspBot is licensed under the [GNU General Public License v3.0](https://github.com/J-Stuff/KaspBot-V2/blob/main/LICENSE)\nIt also pays respect to the [Redbot License](https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/LICENSE)\nThe original Red Bot Source Code can be found [HERE](https://github.com/Cog-Creators/Red-DiscordBot)", inline=False)
        embed.add_field(name="Source Code", value="KaspBot is an open source project. Think you got what it takes to contribute to the project? [Check out it's source code!](https://github.com/J-Stuff/KaspBot-V2)", inline=False)
        await ctx.reply(embed=embed)

    @app_commands.command(name="about")
    async def about_slash(self, i:discord.Interaction):
        embed = discord.Embed(title="KaspBot - About", description=f"KaspBot Version {VERSION}\nUses a fork of [Red Bot](https://github.com/Cog-Creators/Red-DiscordBot) and is modified by `jstuff`", color=discord.Color.blue())
        embed.add_field(name="LICENSE", value="KaspBot is licensed under the [GNU General Public License v3.0](https://github.com/J-Stuff/KaspBot-V2/blob/main/LICENSE)\nIt also pays respect to the [Redbot License](https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/LICENSE)\nThe original Red Bot Source Code can be found [HERE](https://github.com/Cog-Creators/Red-DiscordBot)", inline=False)
        embed.add_field(name="Source Code", value="KaspBot is an open source project. Think you got what it takes to contribute to the project? [Check out it's source code!](https://github.com/J-Stuff/KaspBot-V2)", inline=False)
        await i.response.send_message(embed=embed, ephemeral=False)


    @app_commands.command(name="credits")
    async def credits_slash(self, i:discord.Interaction):
        embed = discord.Embed(title="KaspBot - Credits", description=f"KaspBot Version {VERSION} - Credits", color=discord.Color.blue())
        embed.add_field(name="Original Red Bot", value="Red Bot is a project by [Cog Creators](https://github.com/Cog-Creators/Red-DiscordBot)", inline=False)
        embed.add_field(name="KaspBot", value="KaspBot is a fork of Red Bot, and is modified by `jstuff`", inline=False)
        embed.add_field(name="3rd party addons to KaspBot", value="KaspBot uses 3rd party addons to enhance the bot. A list of these addons can be found [HERE](https://github.com/J-Stuff/KaspBot-V2/blob/main/ADDONS.md)")
        await i.response.send_message(embed=embed, ephemeral=False)
