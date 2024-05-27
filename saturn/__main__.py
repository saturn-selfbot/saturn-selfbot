#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from colored import Fore, Style
from .utils import (
    config,
    motds,
    client,
    clear,
    package_dir_path,
    package_dir_name,
    version,
    check_update,
)
from .logger import logger

from discord.ext import commands
from discord.errors import LoginFailure
import discord

import random
import base64
import fade
import time
import os


@client.event
async def on_ready():
    clear()
    print(
        fade.pinkred(
            random.choice(motds)
        )
    )

    prefix = config.get("commands", "prefix")
    print(
        f"{Fore.MAGENTA}[+]{Style.RESET} Connected: {client.user.name}\n".center(
            os.get_terminal_size().columns
        )
    )
    
    update = "Update available!" if check_update() else "Latest"
        
    logger.info(f"Current version: {version} ({update})")

    success_extensions = 0
    failed_extensions = 0

    for file in os.listdir(f"{package_dir_path}/cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await client.load_extension(f"{package_dir_name}.cogs.{extension}")
                success_extensions += 1
            except commands.ExtensionAlreadyLoaded:
                success_extensions += 1
            except Exception as e:
                logger.error(e)
                failed_extensions += 1

    logger.info(f"Loaded {success_extensions} extensions")
    if failed_extensions:
        logger.warning(f"Failed to import {failed_extensions} extensions")

if __name__ == "__main__":
    try:
        client.run(
            base64.b64decode(
               config.get("token").encode('ascii')
            ).decode("utf-8", errors='ignore'),
            log_handler=None, reconnect=True)
    except LoginFailure:
        logger.error("invalid token!")
        exit()
