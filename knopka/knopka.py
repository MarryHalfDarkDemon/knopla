from vkbottle import Bot
from routes import labelers

bot = Bot("a199290aafe7429e25efc57d7c6fa78aa713e23e45f2e439f8917ae40038e95a2a85a6c0dd90e160d744f")

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

bot.run_forever()