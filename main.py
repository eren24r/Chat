import logging
import openai
from aiogram import Bot, Dispatcher, executor, types

openai.api_key = "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"

API_TOKEN = '6199059179:AAFkrVf-ZodYxya1vIz0v35hl5ld3VnhxmM'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi!\nI'm Ai Chat Bot!\nPowered by @eren24r.")

@dp.message_handler()
async def queries(message: types.Message):
    await bot.send_message(message.chat.id, "Думаю...")
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=str(message.text),
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
    )
    print(response)
    await bot.send_message(message.chat.id, "ok!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
