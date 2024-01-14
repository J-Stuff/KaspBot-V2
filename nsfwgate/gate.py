from redbot.core import commands, Config
import discord
from datetime import datetime, timezone, timedelta

class Gate(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=984984)
        default_guild = {
            "nsfw_role": None
        }
        self.config.register_guild(**default_guild)
        self.bot.add_view(self.Button(self.bot, self.config))
        super().__init__()

    
    

    class Button(discord.ui.View):
        def __init__(self, bot:commands.Bot, config:Config):
            self.bot = bot
            self.config = config
            super().__init__(timeout=None)

        async def is_allowed_nsfw(self, i:discord.Interaction) -> bool:
            now = datetime.now(timezone.utc)
            min_age = 7 # Days
            min_join = 1 # Days

            if now - i.user.created_at < timedelta(days=int(min_age)):
                return False
            elif now - i.user.joined_at < timedelta(days=int(min_join)):
                return False
            else:
                return True

        @discord.ui.button(label="Toggle Access", style=discord.ButtonStyle.red, custom_id="nsfw_button", emoji="🔞")
        async def toggle_access(self, interaction:discord.Interaction, button:discord.ui.Button):
            guild = interaction.guild
            nsfw_role_id = await self.config.guild(guild).nsfw_role()
            nsfw_role = guild.get_role(nsfw_role_id)
            if not type(guild) == discord.Guild: return
            if not nsfw_role: 
                await interaction.response.send_message("The NSFW Role is not set up correctly. Please contact the server owner.", ephemeral=True)
                return
            if [role for role in interaction.user.roles if role.id == nsfw_role_id]:
                await interaction.user.remove_roles(nsfw_role)
                await interaction.response.send_message("You no longer have access to NSFW channels.", ephemeral=True)
            else:
                if await self.is_allowed_nsfw(interaction):
                    await interaction.user.add_roles(nsfw_role)
                    await interaction.response.send_message("You now have access to NSFW channels.", ephemeral=True)
                else:
                    await interaction.response.send_message("⚠️ You do not meet this server's prerequisites for obtaining this role!", ephemeral=True)
            
    
    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def nsfwgate(self, ctx:commands.Context):
        """NSFW Gate Configuration"""
        
    
    @nsfwgate.command(aliases=["info"])
    async def settings(self, ctx:commands.Context) -> None:
        """Display current settings."""
        if not ctx.guild: return
        nsfw_channel_id = await self.config.guild(ctx.guild).nsfw_channel()
        nsfw_role_id = await self.config.guild(ctx.guild).nsfw_role()
        min_account_age = await self.config.guild(ctx.guild).min_account_age()
        min_account_join = await self.config.guild(ctx.guild).min_account_join()
        embed = discord.Embed(title="NSFW Gate Settings", color=discord.Color.blurple())
        if nsfw_role_id:
            embed.add_field(name="NSFW Role", value=f"<@&{nsfw_role_id}>")
        else:
            embed.add_field(name="NSFW Role", value="Not Set")
        
        embed.add_field(name="Minimum Account Age", value=f"{min_account_age} Days")
        embed.add_field(name="Minimum Account Join", value=f"{min_account_join} Days")
        embed.set_footer(text="Self-destructs in 20 seconds.")
        await ctx.reply(embed=embed, delete_after=20)

    @nsfwgate.command()
    async def setrole(self, ctx:commands.Context, role:discord.Role) -> None:
        """Set the NSFW Role."""
        if not ctx.guild: return
        await self.config.guild(ctx.guild).nsfw_role.set(role.id)
        await ctx.reply(f"Set the NSFW Role to {role.mention}.")

    @nsfwgate.command()
    async def setup(self, ctx:commands.Context) -> None:
        """Setup the NSFW Gate."""
        if not ctx.guild: return
        nsfw_role_id = await self.config.guild(ctx.guild).nsfw_role()
        if not nsfw_role_id:
            await ctx.reply("You must set the NSFW Role before you can use this command.")
            return

        nsfw_role = ctx.guild.get_role(nsfw_role_id)
        if not nsfw_role:
            await ctx.reply("The NSFW Channel or Role is not set up!.")
            return
        
        embed = discord.Embed(title="NSFW Gate", description="""
                                                            Use this button to toggle access to the NSFW channels in this server. Please note that ***YOU MUST BE OVER 18 TO VIEW THESE CHANNELS AND PRESS THIS BUTTON.*** Anyone found to be accessing them while under the age specified will face the possibility of being banned from this server. To gain access to the degenerate channels you must open a ticket in <#1151727115553738792> and ask a moderator.
                                                            """, color=discord.Color.red())
        
        await ctx.send(embed=embed, view=self.Button(self.bot, self.config))
        await ctx.message.delete()
        
