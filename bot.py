from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import BoundFilter

API_TOKEN = '6432695102:AAFgw8IcBv9PYLLG98oCaHRYMY3NMhwJ0BQ'
# API_TOKEN = 'another bot token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ADMINS = [5374970910,837251184,1233658877]

generate_link_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="🔗 Link olish")
    ]], resize_keyboard=True
)


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


@dp.message_handler(IsPrivate(), chat_id=ADMINS, commands="start")
async def admin_start_handler(message: types.Message):
    text = "Bir marttalik link olish uchun pastdagi tugmadan foydalaning"
    await message.answer(text=text, reply_markup=generate_link_button)


@dp.message_handler(IsPrivate(), chat_id=ADMINS, text="🔗 Link olish")
async def create_invite_link(message: types.Message):
    try:
        # chat_id = -1002140470690 # test version
        chat_id = -1001922060151
        result = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=1)
        invite_link = result.invite_link

        await message.reply(text=invite_link)
    except Exception as e:
        await message.reply(f"Qaytadan urinib ko'ring: {e}")


if __name__ == '__main__':
    dp.filters_factory.bind(IsPrivate)
    executor.start_polling(dp, skip_updates=True)
