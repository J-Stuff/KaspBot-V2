import discord
from typing import Union
from redbot.core import commands
from redbot.core import Config
from redbot.core import modlog
from redbot.core.bot import Red as Bot

class AttachmentLogging(commands.Cog):
    def __init__(self, bot:Bot, *args, **kwargs):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=221123001)
        super().__init__(*args, **kwargs)

    @classmethod
    async def getModlogChannel(cls, guild:discord.Guild) -> Union[discord.TextChannel, discord.VoiceChannel, discord.StageChannel, None]:
        try:
            return await modlog.get_modlog_channel(guild)
        except:
            return None
        
    @staticmethod
    def checkIfAttachmentCanBeReuploaded(attachment:discord.Attachment, guild:discord.Guild) -> bool:
        if attachment.is_spoiler():
            return False
        if attachment.size > guild.filesize_limit:
            return False
        return True



    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        if await self.bot.cog_disabled_in_guild(self, message.guild):
            return
        if message.guild.me.is_timed_out():
            return
        
        logChannel = await self.getModlogChannel(message.guild)
        if logChannel is None:
            return
        
        try:
            isNSFW = message.channel.is_nsfw() #type:ignore
        except:
            isNSFW = False
        

        channel = message.channel
        if type(channel) in [discord.DMChannel, discord.PartialMessageable, discord.GroupChannel]:
            return
        
        attachments = message.attachments
        if len(attachments) == 0:
            return
        
        embed = discord.Embed(title="Attachment(s) Uploaded", description=f"**{len(attachments)}** attachment(s) uploaded in {channel.mention}", color=discord.Color.from_rgb(255,255,255)) #type:ignore
        embed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
        embed.set_footer(text=f"User ID: {message.author.id}")
        embed.timestamp = message.created_at
        embed.add_field(name="Message Content", value=message.content, inline=False)
        embed.add_field(name="Message URL", value=f"[Click Here]({message.jump_url})", inline=False)
        if message.reference is not None:
            try:
                referenced_message = await message.channel.fetch_message(message.reference.message_id) #type:ignore
                referenced_author = referenced_message.author
                embed.add_field(name="Replying To", value=f"[{referenced_author.global_name}]({referenced_message.jump_url})", inline=False)
            except:
                pass
        
        for attachment in attachments:
            if self.checkIfAttachmentCanBeReuploaded(attachment, message.guild) and not isNSFW:
                await logChannel.send(embed=embed, file=await attachment.to_file())
            elif not self.checkIfAttachmentCanBeReuploaded(attachment, message.guild) and not isNSFW:
                errorEmbed = discord.Embed(title="Attachment(s) Uploaded", description=f"**{len(attachments)}** attachment(s) uploaded in {channel.mention}", color=discord.Color.from_rgb(255,255,255)) #type:ignore
                errorEmbed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
                errorEmbed.set_footer(text=f"User ID: {message.author.id}")
                errorEmbed.timestamp = message.created_at
                errorEmbed.add_field(name="Message Content", value=message.content, inline=False)
                errorEmbed.add_field(name="Message URL", value=f"[Click Here]({message.jump_url})", inline=False)
                errorEmbed.add_field(name="Error", value=f"Attachment {attachment.filename} was not reuploaded because it was too large", inline=False)
                await logChannel.send(embed=errorEmbed)
            elif self.checkIfAttachmentCanBeReuploaded(attachment, message.guild) and isNSFW:
                errorEmbed = discord.Embed(title="Attachment(s) Uploaded", description=f"**{len(attachments)}** attachment(s) uploaded in {channel.mention}", color=discord.Color.from_rgb(255,255,255)) #type:ignore
                errorEmbed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
                errorEmbed.set_footer(text=f"User ID: {message.author.id}")
                errorEmbed.timestamp = message.created_at
                errorEmbed.add_field(name="Message Content", value="`NSFW CHANNEL, CONTENT HIDDEN`", inline=False)
                errorEmbed.add_field(name="Message URL", value=f"[Click Here]({message.jump_url})", inline=False)
                errorEmbed.add_field(name="Error", value=f"Attachment [||{attachment.filename}||] was not reuploaded because the channel is NSFW", inline=False)
                await logChannel.send(embed=errorEmbed)
            else:
                pass