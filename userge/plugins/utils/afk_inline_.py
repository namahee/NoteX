from userge import Message, userge

async def send_inline_afk_(message: Message):
    bot_ = await userge.bot.get_me()
    x_ = await userge.get_inline_bot_results(bot_.username, "afk_")
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=x_.query_id, result_id=x_.results[0].id
    )