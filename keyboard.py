from aiogram.types import *

# Translate btn
async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("🀄️ Переводчик"),
        KeyboardButton("📲 Калькулятор"),
        KeyboardButton("📢 Обратная связь")
    )

    return btn


async def translate_back_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("📄 О переводчике"),
        KeyboardButton("⬅️ Назад")
    )

    return btn


async def calculate_back_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("📄 О калькуляторе"),
        KeyboardButton("⬅️ Назад")
    )

    return btn


async def inline_btn():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("🇦🇫 Afrikaans", callback_data="lan:af"),
        InlineKeyboardButton("🇸🇦 Arabic", callback_data="lan:ar"),
        InlineKeyboardButton("🇦🇲 Armenian", callback_data="lan:hy"),
        InlineKeyboardButton("🇦🇿 Azerbaijani", callback_data="lan:az"),
        InlineKeyboardButton("🇧🇾 Belarusian", callback_data="lan:be"),

        InlineKeyboardButton("🇨🇳 Chinese", callback_data="lan:zh-tw"),
        InlineKeyboardButton("🇩🇰 Danish", callback_data="lan:da"),
        InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="lan:en"),
        InlineKeyboardButton("🇵🇭 Filipino", callback_data="lan:tl"),
        InlineKeyboardButton("🇫🇷 French", callback_data="lan:fr"),

        InlineKeyboardButton("🇩🇪 German", callback_data="lan:de"),
        InlineKeyboardButton("🇬🇷 Greek", callback_data="lan:el"),
        InlineKeyboardButton("🇮🇳 Hindi", callback_data="lan:hi"),
        InlineKeyboardButton("🇮🇩 Indonesian", callback_data="lan:id"),
        InlineKeyboardButton("🇮🇹 Italian", callback_data="lan:it"),

        InlineKeyboardButton("🇯🇵 Japanese", callback_data="lan:ja"),
        InlineKeyboardButton("🇰🇳 Kannada", callback_data="lan:kn"),
        InlineKeyboardButton("🇰🇿 Kazakh", callback_data="lan:kk"),
        InlineKeyboardButton("🇰🇷 Korean", callback_data="lan:ko"),
        InlineKeyboardButton("🇰🇬 Kyrgyz", callback_data="lan:ky"),

        InlineKeyboardButton("🇱🇦 Latin", callback_data="lan:la"),
        InlineKeyboardButton("🇱🇻 Latvian", callback_data="lan:lv"),
        InlineKeyboardButton("🇲🇳 Mongolian", callback_data="lan:mn"),
        InlineKeyboardButton("🇳🇪 Nepali", callback_data="lan:ne"),
        InlineKeyboardButton("🇳🇴 Norwegian", callback_data="lan:no"),

        InlineKeyboardButton("🇮🇷 Persian", callback_data="lan:fa"),
        InlineKeyboardButton("🇵🇱 Polish", callback_data="lan:pl"),
        InlineKeyboardButton("🇵🇹 Portuguese", callback_data="lan:pt"),
        InlineKeyboardButton("🇷🇴 Romanian", callback_data="lan:ro"),
        InlineKeyboardButton("🇷🇺 Russian", callback_data="lan:ru"),

        InlineKeyboardButton("🇷🇸 Serbian", callback_data="lan:sr"),
        InlineKeyboardButton("🇸🇰 Slovak", callback_data="lan:sk"),
        InlineKeyboardButton("🇸🇮 Slovenian", callback_data="lan:sl"),
        InlineKeyboardButton("🇪🇸 Spanish", callback_data="lan:es"),
        InlineKeyboardButton("🇹🇯 Tajik", callback_data="lan:tg"),

        InlineKeyboardButton("🇹🇷 Turkish", callback_data="lan:tr"),
        InlineKeyboardButton("🇺🇦 Ukrainian", callback_data="lan:uk"),
        InlineKeyboardButton("🇺🇬 Uyghur", callback_data="lan:ug"),
        InlineKeyboardButton("🇺🇿 Uzbek", callback_data="lan:uz"),
        InlineKeyboardButton("🇻🇳 Vietnamese", callback_data="lan:vi"),
    )

    return btn


async def choice_lang_btn():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("🔁 Поменять язык", callback_data="choice")
    )

    return btn


# Calculator btn
async def calc_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn.add(
        InlineKeyboardButton("©️", callback_data="clear"),

        InlineKeyboardButton("🔙", callback_data="back"),

        InlineKeyboardButton("%", callback_data="equ:%"),

        InlineKeyboardButton("➗", callback_data="equ:/"),

        InlineKeyboardButton("7️⃣", callback_data="num:7"),
        InlineKeyboardButton("8️⃣", callback_data="num:8"),
        InlineKeyboardButton("9️⃣", callback_data="num:9"),

        InlineKeyboardButton("✖️", callback_data="equ:*"),

        InlineKeyboardButton("4️⃣", callback_data="num:4"),
        InlineKeyboardButton("5️⃣", callback_data="num:5"),
        InlineKeyboardButton("6️⃣", callback_data="num:6"),

        InlineKeyboardButton("➖", callback_data="equ:-"),

        InlineKeyboardButton("1️⃣", callback_data="num:1"),
        InlineKeyboardButton("2️⃣", callback_data="num:2"),
        InlineKeyboardButton("3️⃣", callback_data="num:3"),

        InlineKeyboardButton("➕", callback_data="equ:+"),

        InlineKeyboardButton(".", callback_data="."),

        InlineKeyboardButton("0️⃣", callback_data="num:0"),

        InlineKeyboardButton("**", callback_data="equ:**"),

        InlineKeyboardButton("🟰", callback_data="result"),
    )

    return btn