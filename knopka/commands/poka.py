from vkbottle.bot import BotLabeler, Message

bl = BotLabeler()

@bl.message(text=["пока", "до свидания" , "пока" , ""])
async def greeting(message: Message):
    await message.answer("До новых встреч")