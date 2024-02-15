import logging
from googletrans import Translator

from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from keyboard import *
from state import *
from config import BOT_TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_bot_command(message: Message):
    btn = await start_btn()
    await message.answer(f"<b>Здравствуйте {message.from_user.first_name}! </b>\n"
                        "Пожалуйста, <u><b>выберите опцию:</b></u> ", reply_markup=btn)
    

@dp.message_handler()
async def text_bot(message: Message):
    text = message.text
    if text == "🀄️ Переводчик":
        in_btn = await inline_btn()
        btn1 = await translate_back_btn()
        await message.answer("На какой язык вы хотите <u><b>перевести</b></u>?", reply_markup=in_btn)        
        await message.answer("Чтобы увидеть информацию о переводчике нажмите кнопку <u><b>О переводчике</b></u>", reply_markup=btn1)

    elif text == "📲 Калькулятор":
        btn = await calc_btn()
        btn1 = await calculate_back_btn()
        await message.answer("Калькулятор: \n\n", reply_markup=btn1)
        await message.answer("0", reply_markup=btn)

    elif text == "📢 Обратная связь":
        await message.answer("Чтобы связаться с <b>администратором</b> бота \nнапишите сюда: https://t.me/MukhamedovK")

    elif text == "⬅️ Назад":
        btn = await start_btn()
        await message.answer("<b>Выберите опцию:</b>", reply_markup=btn)

    elif text == "📄 О переводчике":
        await message.answer(f"Здравствуйте {message.from_user.first_name}!\n"
                             "Этот бот может переводить ваши фразы на <u><b>40</b></u> разных языков, которые представлены выше.\n"
                             "И им пользоваться очень просто!\nВыбираете язык, на который хотите <b>перевести</b> и пишете свои фразы.\n"
                             "<b>Всё!</b>\n"
                             "Пользуйтесь на здоровье и спасибо за внимание! :-)")

    elif text == "📄 О калькуляторе":
        await message.answer(f"Здравствуйте {message.from_user.first_name}!\n"
                             "Здесь написан <b>список символов и какую работу они выполняют</b>:\n\n"
                             "©️ - Очищение выражения\n🔙 - Удаление одного знака(символа)\n% - Выделение процентов\n➗ - Деление\n"
                             "✖️ - Умножение\n➖ - Разность(минус)\n➕ - Сумма(плюс)\n. - Чтобы сделать дробные числа\n** - Возведение в степень\n\n"
                             "Надеюсь я вам помог и спасибо за внимение! :-)")


# TRANSLATOR CODE

@dp.callback_query_handler(text_contains='lan')
async def translate_callback(call: CallbackQuery, state: FSMContext):
    selected_lang_code = call.data.split(':')[-1]
    btn = await choice_lang_btn()

    await state.update_data(selected_lang_code=selected_lang_code)
    await call.message.answer("Чтобы изменить язык нажмите на кнопку ниже 👇", reply_markup=btn)
    await call.message.edit_text("Введите <u><b>текст</b></u>, который хотите <u><b>перевести.</b></u>")
    await Continue.text.set()

    

@dp.message_handler(state=Continue.text)
async def translate_result(message: Message, state: FSMContext):
    translator = Translator()
    text = message.text
    data = await state.get_data()
    if text not in ["⬅️ Назад", "📄 О переводчике"]:
        result = translator.translate(text=text, dest=data['selected_lang_code'])
        await message.answer(result.text)

    if text == "⬅️ Назад":
        btn = await start_btn()
        await message.answer("<b>Выберите опцию:</b>", reply_markup=btn)
        await state.finish()

    elif text == "📄 О переводчике":
        await message.answer(f"Здравствуйте {message.from_user.first_name}!\n"
                             "Здесь написан <b>список символов и какую работу они выполняют</b>:\n\n"
                             "©️ - Очищение выражения\n🔙 - Удаление одного знака(символа)\n% - Выделение процентов\n➗ - Деление\n"
                             "✖️ - Умножение\n➖ - Разность(минус)\n➕ - Сумма(плюс)\n. - Чтобы сделать дробные числа\n** - Возведение в степень\n\n"
                             "Надеюсь я вам помог и спасибо за внимение! :-)")
         


@dp.callback_query_handler(state=Continue.text, text='choice')
async def choice_lang(call: CallbackQuery, state: FSMContext):
    btn = await inline_btn()
    await state.finish()
    await call.message.edit_text("На какой язык вы хотите <u><b>перевести</b></u>?", reply_markup=btn)




# CALCULATOR CODE

@dp.callback_query_handler(text_contains='num')
async def calc_num_callback(call: CallbackQuery):
    selected_num = call.data.split(':')[-1]
    now_num = call.message.text
    if now_num != '0':
        new_num = now_num + selected_num
    else:
        new_num = selected_num
    btn = call.message.reply_markup
    await call.message.edit_text(new_num, reply_markup=btn)


@dp.callback_query_handler(text_contains='equ')
async def calc_num_callback(call: CallbackQuery):
    selected_equ = call.data.split(':')[-1]
    equ_list = ['/', '*', '+', '-', '**', '%', '.']
    now_num = call.message.text
    if now_num[-1] in equ_list:
        await call.answer('❌')
    else:
        new_num = now_num + selected_equ
        btn = call.message.reply_markup
        await call.message.edit_text(new_num, reply_markup=btn)


@dp.callback_query_handler(text='clear')
async def calc_clear_callback(call: CallbackQuery):
    now_num = call.message.text
    if now_num != '0':
        btn = call.message.reply_markup
        await call.message.edit_text('0', reply_markup=btn)


@dp.callback_query_handler(text='back')
async def calc_back_callback(call: CallbackQuery):
    now_num = call.message.text
    if now_num != '0' and len(now_num) > 1:
        new_num = now_num[:-1]
        btn = call.message.reply_markup
        await call.message.edit_text(new_num, reply_markup=btn)
    else:
        btn = call.message.reply_markup
        await call.message.edit_text('0', reply_markup=btn)


@dp.callback_query_handler(text='.')
async def calc_icol_callback(call: CallbackQuery):
    now_num = call.message.text
    equ_list = ['/', '*', '+', '-', '**', '%', '.']
    if now_num[-1] != '.' and now_num[-1] not in equ_list:
        new_num = now_num + '.'
        btn = call.message.reply_markup
        await call.message.edit_text(new_num, reply_markup=btn)


@dp.callback_query_handler(text='result')
async def calc_result_callback(call: CallbackQuery):
    now_num = call.message.text
    equ_list = ['/', '*', '+', '-', '**', '%', '.']
    if now_num[-1] in equ_list:
        await call.answer('❌')
    else:
        new_num = eval(now_num)
        btn = call.message.reply_markup
        await call.message.edit_text(new_num, reply_markup=btn)
    







if __name__ == '__main__':
    executor.start_polling(dp)
