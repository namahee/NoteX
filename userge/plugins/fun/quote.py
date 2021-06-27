# Rewrote with experimental bleck magik
# code-rgb

import asyncio

from pyrogram.errors import YouBlockedUser

from userge import Message, userge
from userge.utils.exceptions import StopConversation

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@userge.on_cmd(
    "q",
    about={
        "header": "Quote a message",
        "flags": {"-l": "limit, for multiple messages"},
        "usage": "Reply {tr}q -l[message limit]",
        "examples": ["{tr}q", "{tr}q -l3"],
    },
    allow_via_bot=False,
    del_pre=True,
)
async def quotecmd(message: Message):
    """quotecmd"""
    reply = message.reply_to_message
    quote_list = []
    self_mid = False
    args = ""
    if reply:
        if "l" in message.flags:
            limit = message.flags.get("l", 1)
            if not limit.isdigit():
                await message.err("give valid no. of message to quote", del_in=5)
                return
            num_ = min(int(limit), 24)
            async for msg in userge.iter_history(
                message.chat.id, limit=num_, offset_id=reply.message_id, reverse=True
            ):
                if msg.message_id != message.message_id:
                    quote_list.append(msg.message_id)
            if message.filtered_input_str:
                self_mid = True
                await message.edit(message.filtered_input_str)
        else:
            quote_list.append(reply.message_id)
            if message.input_str:
                self_mid = True
                await message.edit(message.input_str)
    else:
        args = message.input_str
    if self_mid:
        quote_list.append(message.message_id)
    else:
        await message.delete()
    if not args and len(quote_list) == 0:
        await message.err("Reply to a message or provide an input to quote !", del_in=5)
        return
    try:
        async with userge.conversation("QuotLyBot", timeout=100) as conv:
            try:
                if quote_list:
                    await userge.forward_messages(
                        "QuotLyBot", message.chat.id, quote_list
                    )
                    if self_mid:
                        await message.delete()
                elif args:
                    await conv.send_message(args)
            except YouBlockedUser:
                await message.edit("first **unblock** @QuotLyBot")
                return
            quote = await conv.get_response(mark_read=True)
            if not (quote.sticker or quote.document):
                await message.err("something went wrong!")
                return
            message_id = reply.message_id if reply else None
            if quote.sticker:
                await userge.send_sticker(
                    chat_id=message.chat.id,
                    sticker=quote.sticker.file_id,
                    reply_to_message_id=message_id,
                )
            else:
                await userge.send_document(
                    chat_id=message.chat.id,
                    document=quote.document.file_id,
                    reply_to_message_id=message_id,
                )
    except StopConversation:
        await message.err(
            "@QuotLyBot Didn't respond in time\n:(  please try again later...", del_in=5
        )


@userge.on_cmd(
    "kkk",
    about={"header": "fun"},
)
async def kfun(message: Message):
    """kkk fun"""
    kkk = [
        "kkkk",
        "kkkkkk",
        "kkkkkkkk",
        "kkkkkkkkkk",
        "kkkkkkkkkkkk",
        "kkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
    ]
    for k in kkk:
        if (
            k
            == "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
        ):
            break
        await message.edit(k)


@userge.on_cmd(
    "Kkk$",
    about={
        "header": "execute .kkk",
    },
    trigger="",
    allow_via_bot=False,
)
async def kkk_(message: Message):
    kkk = "!kkk"
    await message.try_to_edit(kkk, del_in=1)


async def check_and_send(message: Message, *args, **kwargs):
    replied = message.reply_to_message
    if replied:
        await asyncio.gather(message.delete(), replied.reply(*args, **kwargs))
    else:
        await message.edit(*args, **kwargs)
        
        
@userge.on_cmd(
    "t",
    about={
        "header": "iter_history",
    },
)
async def send_inline(message: Message):
   bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "afk")
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=x.query_id, result_id=x.results[0].id
    )
    await message.delete()

async def tt(message: Message):
    await message.edit_text("ooi", reply_markup=idk.buttons())
    
class idk:
    def buttons() -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton(text="oi", url="https://google.com"),
            ]
        ]
        