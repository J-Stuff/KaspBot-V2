from redbot.core import commands, app_commands
import discord
class AboutCommand(commands.Cog):


    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.bot

    @commands.command(name="about")
    async def about(self, ctx:commands.Context):
        embed = discord.Embed(title="KaspBot - About", description="KaspBot Version 2.0.0\nUses a fork of [Red Bot](https://github.com/Cog-Creators/Red-DiscordBot) and is modified by `jstuff`", color=discord.Color.blue())
        embed.add_field(name="LICENSE", value="KaspBot is licensed under the [GNU General Public License v3.0](https://github.com/J-Stuff/KaspBot-V2/blob/main/LICENSE)\nIt also pays respect to the [Redbot License](https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/LICENSE)\nThe original Red Bot Source Code can be found [HERE](https://github.com/Cog-Creators/Red-DiscordBot)")
        embed.add_field(name="Source Code", value="KaspBot is an open source project. Think you got what it takes to contribute to the project? [Check out it's source code!](https://github.com/J-Stuff/KaspBot-V2)")
        await ctx.reply(embed=embed)

    @app_commands.command(name="about")
    async def about_slash(self, i:discord.Interaction):
        embed = discord.Embed(title="KaspBot - About", description="KaspBot Version 2.0.0\nUses a fork of [Red Bot](https://github.com/Cog-Creators/Red-DiscordBot) and is modified by `jstuff`", color=discord.Color.blue())
        embed.add_field(name="LICENSE", value="KaspBot is licensed under the [GNU General Public License v3.0](https://github.com/J-Stuff/KaspBot-V2/blob/main/LICENSE)\nIt also pays respect to the [Redbot License](https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/LICENSE)\nThe original Red Bot Source Code can be found [HERE](https://github.com/Cog-Creators/Red-DiscordBot)")
        embed.add_field(name="Source Code", value="KaspBot is an open source project. Think you got what it takes to contribute to the project? [Check out it's source code!](https://github.com/J-Stuff/KaspBot-V2)")
        await i.response.send_message(embed=embed, ephemeral=False)