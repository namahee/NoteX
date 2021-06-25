# Rewrote with experimental bleck magik
# code-rgb

from pyrogram.errors import YouBlockedUser
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram.raw.types import ReplyKeyboardForceReply, ReplyInlineMarkup

from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation

CHANNEL = userge.getCLogger(__name__)


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


async def send_buttons(
    message: Message, text: str, markup: InlineKeyboardMarkup
) -> None:
    await message.reply(text, disable_web_page_preview=True, reply_markup=markup)


def _info() -> str:
    _info_ = f"""
<a href="https://telegram.dog/x_xtests"><b>NoteX</a> is Up and Running.</b>

  🐍   <b>Python :</b>    <code>versão</code>
  🔥   <b>Pyrogram :</b>    <code>oversao</code>
  🧬   <b>𝑿 :</b>    <code>aversak
o</code>

<b>botalive</b>    <code>|</code>    🕔  <b>uptime</b>
"""
    return _info_


@userge.on_cmd(
    "git",
    about={"header": "test"},
)
async def git_(message: Message):
    cap = _info()
    chat_id = message.chat.id
    client = message.client
    foto = "https://telegra.ph/file/b8581802499a71ebd3f96.jpg"
    cap += (
        f"\n⚡️  <a href={Config.UPSTREAM_REPO}><b>REPO</b></a>"
        "    <code>|</code>    "
        "👥  <a href='https://t.me/useless_x'><b>SUPPORT</b></a>"
    )

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="REPO", url=Config.UPSTREAM_REPO),
            ]
        ]
    )

    buttons2 = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="MY GIT", url="https://github.com/samuca78"),
            ]
        ]
    )

    buttons3 = [
        [
            InlineKeyboardButton(text="GITHUB", url="https://github.com/"),
        ]
    ]

    await client.send_message(
        chat_id,
        caption=cap,
        reply_markup=buttons2,
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
    "kkk$",
    about={
        "header": "execute .kkk",
    },
    trigger="",
    allow_via_bot=False
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
