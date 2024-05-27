#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from discord.ext import commands
from .. import utils

import requests
import random

class NSFW(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @commands.command(
        name="hentai",
        description="Get a random hentai image.",
        aliases=["hent"]
    )
    async def hentai(self, message):
        response = requests.get("https://nekobot.xyz/api/image?type=hentai")
        await utils.answer(message, response.json()["message"])
        
    @commands.command(
        name="thigh",
        description="Get a random thigh image."
    )
    async def thigh(self, message):
        response = requests.get("https://nekobot.xyz/api/image?type=hthigh")
        await utils.answer(message, response.json()["message"])
        
    @commands.command(
        name="ass",
        description="Get a random ass image."
    )
    async def ass(self, message):
        response = requests.get("https://nekobot.xyz/api/image?type=hass")
        await utils.answer(message, response.json()["message"])

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(NSFW(bot))