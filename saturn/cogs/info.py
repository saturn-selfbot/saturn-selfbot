#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from discord.ext import commands
from .. import utils

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @commands.command(
        name="info",
        description="Get information about this selfbot.",
        aliases=["selfbot", "saturn", "information"]
    )
    async def info(self, message):
        extensions = len(self.bot.cogs.items())
        commands = len(self.bot.commands)
        
        update = "Update available!" if utils.check_update() else "Latest"
        
        text = f"""
>>> ```ini
[ selfbot ]
account = {self.bot.user}
version = {utils.version}  ({update})

extensions = {extensions}
commands = {commands}

uptime = {utils.get_uptime()}
```
## saturn selfbot
        """
        await utils.answer(message, text)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Info(bot))