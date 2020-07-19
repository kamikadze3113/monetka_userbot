import asyncio
from .. import loader
import random


@loader.tds
class МонеткаMod(loader.Module):
    strings = {"name": "Монетка"}
    async def монеткаcmd(self, message):
        monet = random.randint(1,2)
        if monet == 1:
            await message.edit("Орел.")
        else:
            await message.edit("Решка.")