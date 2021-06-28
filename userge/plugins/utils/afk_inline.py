from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from userge import Message, userge
from userge.plugins.custom.afk import _TELE_REGEX, REASON
from userge.utils import time_formatter


async def send_inline_afk(message: Message):
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "afk")
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=x.query_id, result_id=x.results[0].id
    )


async def send_inline_afk_(message: Message):
    bot_ = await userge.bot.get_me()
    x_ = await userge.get_inline_bot_results(bot_.username, "afk_")
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=x_.query_id, result_id=x_.results[0].id
    )


async def _send_inline_afk(message: Message):
    _bot = await userge.bot.get_me()
    _x = await userge.get_inline_bot_results(_bot.username, "_afk")
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=_x.query_id, result_id=_x.results[0].id
    )


class _afk_:
    def out_str() -> str:
        _afk_time = time_formatter(round(time.time() - TIME))
        _r = REASON.split(" | ", maxsplit=1)
        _STATUS = _r[0]
        out_str = (
            f"⚡️ **Auto Reply** ⒶⒻⓀ \n ╰•  **Last Check:** {_afk_time} ago\n\n"
            f"▫️ **I'm not here because:**\n {_STATUS}"
        )
        return out_str

    def _out_str() -> str:
        afk_time_ = time_formatter(round(time.time() - TIME))
        out_str = (
            f"⚡️ **Auto Reply** ⒶⒻⓀ \n ╰•  **Last Check:** {afk_time_} ago.\n\n"
            f"▫️ **I'm not here because:**\n {REASON}"
        )
        return out_str

    def link() -> str:
        _match_ = _TELE_REGEX.search(REASON)
        if _match_:
            link = _match_.group(0)
            return link

    async def check_media_link(media_link: str):
        match_ = _TELE_REGEX.search(media_link.strip())
        if not match_:
            return None, None
        if match_.group(1) == "i.imgur.com":
            link = match_.group(0)
            link_type = "url_gif" if match_.group(3) == "gif" else "url_image"
        elif match_.group(1) == "telegra.ph/file":
            link = match_.group(0)
            link_type = "url_gif" if match_.group(3) == "gif" or "mp4" else "url_image"
        else:
            link_type = "tg_media"
            if match_.group(2) == "c":
                chat_id = int("-100" + str(match_.group(3)))
                message_id = match_.group(4)
            else:
                chat_id = match_.group(2)
                message_id = match_.group(3)
            link = [chat_id, int(message_id)]
        return link_type, link

    def afk_buttons() -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton(
                    "My Repo", url="https://github.com/samuca78/NoteX"
                ),
                InlineKeyboardButton("Github", url="https://github.com"),
            ],
            [
                InlineKeyboardButton("My Git", url="https://github.com/samuca78"),
            ],
        ]
        return InlineKeyboardMarkup(buttons)
