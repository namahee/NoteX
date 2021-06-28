from userge import Message, userge


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


# class _afk:
# async def check_media_link(media_link: str):
# match_ = _TELE_REGEX.search(media_link.strip())
# if not match_:
# return None, None
# if match_.group(1) == "i.imgur.com":
# link = match_.group(0)
# link_type = "url_gif" if match_.group(3) == "gif" else "url_image"
# elif match_.group(1) == "telegra.ph/file":
# link = match_.group(0)
# link_type = "url_gif" if match_.group(3) == "gif" else "url_image"
# else:
# link_type = "tg_media"
# if match_.group(2) == "c":
# chat_id = int("-100" + str(match_.group(3)))
# message_id = match_.group(4)
# else:
# chat_id = match_.group(2)
# message_id = match_.group(3)
# link = [chat_id, int(message_id)]
# return link_type, link

# def afk_buttons() -> InlineKeyboardMarkup:
# buttons = [
# [
# InlineKeyboardButton(
# "My Repo", url="https://github.com/samuca78/NoteX"
# ),
# InlineKeyboardButton("Github", url="https://github.com"),
# ],
# [
# InlineKeyboardButton("My Git", url="https://github.com/samuca78"),
# ],
# ]
# return InlineKeyboardMarkup(buttons)
