#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from discord.ext import commands
from .. import utils


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(
        name="help",
        usage="[command]",
        description="Shows all the commands of the Saturn selfbot.",
        aliases=["?", "h", "commands", "cmds"]
    )
    async def help(self, message):
        prefix = utils.config.get("commands", "prefix")
        commands = len(self.bot.commands)
        cogs = self.bot.cogs.items()

        text = f"""
>>> ```ini
[ prefix ] : {prefix}
[ commands ] : {commands}
```
        """
        text += "```python\n"
        for cog_name, cog in cogs:
            command_names = [command.name for command in cog.get_commands()]
            commands_list = " ".join([command for command in command_names])
            if commands_list:
                text += f'"{cog_name.title()}": ( {commands_list} )\n'

        text += """
```
## saturn selfbot
        """
        await utils.answer(message, text)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
