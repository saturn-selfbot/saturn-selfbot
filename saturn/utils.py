#    ⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     ______     ______     ______   __  __     ______     __   __
#    ⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  ___\   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \
#    ⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \___  \  \ \  __ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \
#    ⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\
# ⠀    ⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/   \/_/ \/_/
# ⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀

from discord.ext import commands
import discord
from .database import Database

import asyncio
import base64
import time
import git
import re
import os

import datetime

init_time = time.perf_counter()

def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


async def _get_build_number(session) -> int:
    default_build_number = 9999
    try:
        login_page_request = await session.get("https://discord.com/login", timeout=7)
        login_page = await login_page_request.text()
        for asset in re.compile(r"(\w+\.[a-z0-9]+)\.js").findall(login_page)[-1:]:
            build_url = f"https://discord.com/assets/{asset}.js"
            build_request = await session.get(build_url, timeout=7)
            build_file = await build_request.text()
            build_find = re.findall(r'Build Number:\D+"(\d+)"', build_file)
            if build_find:
                return int(build_find[0]) if build_find else default_build_number
    except asyncio.TimeoutError:
        return default_build_number

discord.utils._get_build_number = _get_build_number  # type: ignore

motds = ["""
⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀     __     __     __          __            
⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁    /\  _\   /\   \   /\__  _\ /\ \/\ \   /\  == \   /\ "-.\ \   
⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀    \ \_  \  \ \   \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \ \-.  \  
⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢     \/\_\  \ \_\ \_\    \ \_\  \ \_\  \ \_\ \_\  \ \_\\"\_\ 
⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐      \/_/   \/_/\/_/     \/_/   \/_/   \/_/ /_/   \/_/ \/_/ 
    """,
         """
              _               _                    
         ,d88b,)    ___  __ _| |_ _   _ _ __ _ __  
         88888%    / __|/ _` | __| | | | '__| '_ \ 
         >?8jY'    \__ \ (_| | |_| |_| | |  | | | |
         `-"       |___/\__,_|\__|\__,_|_|  |_| |_|
    """,
         """
     _______.     ___   .___________. __    __  .______      .__   __. 
    /       |    /   \  |           ||  |  |  | |   _  \     |  \ |  | 
   |   (----`   /  ^  \ `---|  |----`|  |  |  | |  |_)  |    |   \|  | 
    \   \      /  /_\  \    |  |     |  |  |  | |      /     |  . `  | 
.----)   |    /  _____  \   |  |     |  `--'  | |  |\  \----.|  |\   | 
|_______/    /__/     \__\  |__|      \______/  | _| `._____||__| \__| 
    """,
         """
 _______  _______  _______  __   __  ______    __    _ 
|       ||   _   ||       ||  | |  ||    _ |  |  |  | |
|  _____||  |_|  ||_     _||  | |  ||   | ||  |   |_| |
| |_____ |       |  |   |  |  |_|  ||   |_||_ |       |
|_____  ||       |  |   |  |       ||    __  ||  _    |
 _____| ||   _   |  |   |  |       ||   |  | || | |   |
|_______||__| |__|  |___|  |_______||___|  |_||_|  |__|
    """,
         """
 ::::::::      ::: ::::::::::: :::    ::: :::::::::  ::::    ::: 
:+:    :+:   :+: :+:   :+:     :+:    :+: :+:    :+: :+:+:   :+: 
+:+         +:+   +:+  +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+ 
+#++:++#++ +#++:++#++: +#+     +#+    +:+ +#++:++#:  +#+ +:+ +#+ 
       +#+ +#+     +#+ +#+     +#+    +#+ +#+    +#+ +#+  +#+#+# 
#+#    #+# #+#     #+# #+#     #+#    #+# #+#    #+# #+#   #+#+# 
 ########  ###     ### ###      ########  ###    ### ###    #### 
    """
         ]
         
config = Database("./json/config.json")

NitroSniper = Database("./json/snipers/nitro.json")
SelfbotSniper = Database("./json/snipers/selfbot.json")

client = commands.Bot(
    command_prefix=config.get("commands", "prefix"),
    self_bot=True,
    help_command=None,
    request_guilds=False,
    chunk_guilds_at_startup=False
)

if not config.get("token"):
    token = input("account token: ")
    
    base64_token = base64.b64encode(
        token.encode("ascii")
    )
    
    config.set("token", base64_token.decode("utf-8"))
    config.save()

package_path = os.path.abspath(__file__)  # /root/project/package/__main__.py
package_dir_path = os.path.dirname(
    os.path.abspath(__file__)
)  # /root/project/package/
package_dir_name = os.path.basename(
    os.path.dirname(os.path.abspath(__file__))
)  # package


async def answer(
    ctx,
    message: str,
    delete: bool = True,
    **kwargs,
) -> str:
    responses = []
    if len(message) > 2000:
        chunks = [message[i: i + 2000] for i in range(0, len(message), 2000)]
        for chunk in chunks:
            responses.append(await ctx.reply(chunk))
    else:
        try:
            responses.append(await ctx.message.edit(message))
        except:
            responses.append(await ctx.reply(message))

    for response in responses:
        if delete:
            await asyncio.sleep(config.get("commands", "deletetimer"))
            await response.delete()
    return responses

repo = git.Repo(
    search_parent_directories=True
)

year = datetime.datetime.now().year
branch = repo.active_branch.name

version = f"{year}.1.{branch}"

def check_update() -> bool:
    diff = repo.git.log(
        [
            f"HEAD..origin/{branch}",
            "--oneline"
        ]
    )
    
    return True if diff else False
    
def get_uptime() -> str:
    return str(
        datetime.timedelta(
            seconds=round(
                time.perf_counter() - init_time
            )
        )
    )