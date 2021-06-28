from userge import Message, userge


async def _send_inline_afk(message: Message):
    _bot = await userge.bot.get_me()
    _x = await userge.get_inline_bot_results(_bot.username, "_afk")
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=_x.query_id, result_id=_x.results[0].id
    )
