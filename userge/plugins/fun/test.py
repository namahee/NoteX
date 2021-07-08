""" Módulo de testes para o @NoteZV com fins de aprendizado """

import asyncio
import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConverimport


@userge.on_cmd(
    "nbot",
    about={
        "header": "criar um bot",
        "como usar": "{tr}nbot [nome] | [username_bot] ou [usernameBot]", 
    },
    allow_via_bot=False,
    allow_channels=False,
)
async def nbot_(message: Message):
    name = message.input_str.split(" | ", maxsplit=1)
    if not name:
        await message.err("Coloque um nome e um username.")
        return
    try:
        async with userge.conversation("BotFather") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message("/newbot")
            await conv.send_message(name[0])
            await conv.send_message(name[1])
            # oi = await conv.get_response(mark_read=True)
        # await message.edit(f"Aqui:\n\n{oi}")
        await message.edit(f"Prontinho, bot criado. [Aqui](t.me/{name[1]})")
  
    except YouBlockedUser:
        await message.edit("Desbloqueie o **@BotFather**")
    except StopConversation:
        await message.err("O Bot está morto...")
        

@userge.on_cmd(
    "cname",
    about={
        "header": "muda o nome do bot.",
        "como usar": "{tr}cname [@UsernameDoBot] | [nome]",
    },
    allow_via_bot=False,
    allow_channels=False,
)
async def cname_(message: Message):
    both = message.input_str.split(" | ", maxsplit=1)
    if not both:
        await message.err("Coloque um username e um nome.")
        return
    try:
        async with userge.conversation("BotFather") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message("/setname")
            await conv.send_message(both[0])
            await conv.send_message(both[1])
        await message.edit("Pronto! O nome do seu bot foi alterado.")
    except YouBlockedUser:
        await message.edit("Desbloqueie o **@BotFather**")
    except StopConversation:
        await message.err("O bot morreu...")
        

@userge.on_cmd(
    "sdescription",
    about={
        "header": "Coloca ou altera a descrição do bot.",
        "como usar": "{tr}sdescription [@UsernameDoBot] | [description]",
    },
    allow_via_bot=False,
    allow_channels=False,
)
async def sdescription_(message: Message):
    both = message.input_str.split(" | ", maxsplit=1)
    if not both:
        await message.err("Coloque um username e uma descrição.")
        return
    try:
        async with userge.conversation("BotFather") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message("/setdescription")
            await conv.send_message(both[0])
            await conv.send_message(both[1])
        await message.edit("Pronto! Foi alterada/colocada uma descrição do seu bot.")
    except YouBlockedUser:
        await message.edit("Desbloqueie o **@BotFather**")
    except StopConversation:
        await message.err("O bot morreu...")
        
        
@userge.on_cmd(
    "atext",
    about={
        "header": "Coloca ou altera o texto sobre o bot",
        "como usar": "{tr}atext [@UsernameDoBot] | [texto]",
    },
    allow_via_bot=False,
    allow_channels=False,
)
async def atext_(message: Message):
    both = message.input_str.split(" | ", maxsplit=1)
    if not both:
        await message.err("Coloque um username e um nome.")
        return
    try:
        async with userge.conversation("BotFather") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message("/setabouttext")
            await conv.send_message(both[0])
            await conv.send_message(both[1])
        await message.edit("Pronto! Foi alterada/colocada um texto sobre o seu bot")
    except YouBlockedUser:
        await message.edit("Desbloqueie o **@BotFather**")
    except StopConversation:
        await message.err("O bot morreu...")
        

@userge.on_cmd(
    "spick",
    about={
        "header": "Coloca uma foto no perfil do bot",
        "como usar": "{tr}atext [@UsernameDoBot] | [LinkDaFoto]",
    },
    allow_via_bot=False,
    allow_channels=False,
)
async def spick_(message: Message):
    both = message.input_str.split(" | ", maxsplit=1)
    if not both:
        await message.err("Coloque um username e um link.")
        return
    try:
        async with userge.conversation("BotFather") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message("/setpick")
            await conv.send_message(both[0])
            await conv.send_message(
                message.client.send_photo(
                    message.chat.id,
                    photo=both[1],
                )
            )
        await message.edit("Pronto! Foi colocada uma foto no perfil do seu bot.")
    except YouBlockedUser:
        await message.edit("Desbloqueie o **@BotFather**")
    except StopConversation:
        await message.err("O bot está morto...")
    