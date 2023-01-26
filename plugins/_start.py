# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍Search YouTube", switch_inline_query_current_chat="")
        ]
    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    reply_markup = START_BUTTONS
    await message.reply(
        f"السلام عليكم يا {message.from_user.first_name}!\n\n  أنا بوت أقوم بتحميل قوائم يوتيوب , فقط أرسل رابط قائمة تشغيل \n\n البوت لا يدعم تحميل قوائم تشغيل في صورة صوتية للأسف \n\n لبقية البوتات هنا  \n\n https://t.me/ibnAlQyyim/1120 \n\n لدعم استمرار المشروع هنا \n\n http://paypal.me/kelectronic89 "
      
