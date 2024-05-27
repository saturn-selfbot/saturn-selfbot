#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from discord.ext import commands
from ..utils import (
    config,
    SelfbotSniper,
    NitroSniper
)
from ..logger import logger

import re
import time

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
        self.prefixes = [
            ".", ",", "?",
            ">", "+", "-",
            "$", "%", "#",
            "^", "&", "~",
            "<", ";", ":",
            "/", "|", "="
        ]

    @commands.Cog.listener()
    async def on_command(self, message):
        if config.get("logging", "console", "status"):
            prefix = config.get("commands", "prefix")
 
            logger.info(prefix + message.command.name)
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            pass
            
        if NitroSniper.get("status"):
            if 'discord.gift/' in message.content.lower():
                code = re.search("discord.gift/(.*)", message.content).group(1)
                if NitroSniper.get("logging", "console", "status"):
                    logger.info(f"nitro code: {code}")
                    
    @commands.Cog.listener()
    async def on_delete(self, message):
        if message.author == self.bot.user:
            pass
            
        if SelfbotSniper.get("status"):
            for prefix in self.prefixes:
                if message.content.startswith(prefix):
                    if SelfbotSniper.get("logging", "console", "status"):
                        logger.info(f"selfbot: {message.author}")
                    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Events(bot))