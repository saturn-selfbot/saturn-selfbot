#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from discord.ext import commands
from .. import utils
import discord


class AdminTools(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(
        name="purge",
        usage="(messages)",
        description="Deleting the required number of messages",
        aliases=["clear"],
    )
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, message, amount: int):
        if amount > 2000:
            await utils.answer(message, f"**Too many messages to delete!**")
            return

        await message.channel.purge(limit=(amount))
        msg = f"""
>>> ```
Deleted {amount+1} messages!
```
## saturn selfbot
        """
        await utils.answer(message, msg)

    @commands.command(
        name="mute",
        usage="(@member) [reason]",
        description="Block access to the users sending messages.",
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, message, user: discord.Member, *, reason: str = None):
        role = discord.utils.get(message.guild.roles, name="muted")

        if not role:
            role = await message.guild.create_role(name="muted")

            for channel in message.guild.channels:
                await channel.set_permissions(role, send_messages=False)

        await user.add_roles(role)
        msg = f"""
>>> ```
Muted {user.name}#{user.discriminator}.
{reason}
```
## saturn selfbot
        """
        await utils.answer(message, msg)

    @commands.command(
        name="unmute",
        usage="(@member) [reason]",
        description="Unblock access to the users sending messages.",
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unmute(message, user: discord.User):
        role = discord.utils.get(message.guild.roles, name="muted")
        if not role:
            await utils.answer(message, "**No muted role!**")
            return
        await user.remove_roles(role)
        msg = """
>>> ```
Unmuted {user.name}#{user.discriminator}.
```
## saturn selfbot
        """
        await utils.answer(message, msg)

    @commands.command(
        name="kick",
        usage="(@member) [reason]",
        description="To kick the user out of the server.",
    )
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(message, user: discord.User, *, reason: str = None):
        await user.kick(reason=reason)
        msg = """
>>> ```
{user.name}#{user.discriminator} has been kicked from the server.
{reason}
```
## saturn selfbot
        """
        await utils.answer(message, msg)

    @commands.command(
        name="ban",
        usage="(@member) [reason]",
        description="ban user.",
    )
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(message, user: discord.User, *, reason: str = None):
        await user.ban(reason=reason)
        msg = """
>>> ```
{user.name}#{user.discriminator} has been banned.
{reason}
```
## saturn selfbot
        """
        await utils.answer(message, msg)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AdminTools(bot))
