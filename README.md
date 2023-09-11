# KaspBot-V2


## This is a fork of [Cog-Creators/Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) customised for [Kaspers TikTok Community](https://discord.gg/wVsvB3XMWP)



# Credits:

- [J Stuff](https://github.com/J-Stuff) - Head development





---





## Installation
<!-- TODO -->
<!-- Will probably use this: https://github.com/PhasecoreX/docker-red-discordbot -->

### Docker
Run the following command in a directory with another directory named `data` inside it:
```bash
docker run -v ./data:/data -e TOKEN=bot_token -e PREFIX=. -e CUSTOM_REDBOT_PACKAGE=git+https://github.com/J-Stuff/KaspBot-V2.git phasecorex/red-discordbot
```