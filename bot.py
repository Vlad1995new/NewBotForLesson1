# Token: 5633259704:AAHgYgPAdBYXR-uSSVaUz4UotQbuJ82nbTU
import time
import logging
from aiogram import Bot, Dispatcher, executor, types
proxy_url = 'http://proxy.server:3128'
TOKEN = '5633259704:AAHgYgPAdBYXR-uSSVaUz4UotQbuJ82nbTU'
MESSAGE ="Давай, {}, начни уже работать наконец!!!"


bot = Bot(token=TOKEN, proxy=proxy_url)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_hendler(messege: types.Message):
    user_id = messege.from_user.id
    user_name = messege.from_user.first_name
    user_full_name = messege.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await messege.reply(f"Привет, {user_full_name}")

    for i in range(7):
        time.sleep(86400)

        await bot.send_message(user_id, MESSAGE.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)
