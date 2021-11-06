"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "👋🏻 **Merhaba [{}](tg://user?id={})**, Ben **Radyo Çalar Botuyum** Kanallarda ve Gruplarda 24x7 Kesintisiz Radyo/Akış Müziği Çalabilirim. ❤"
HELP = """🏷️ **Yardıma İhtiyacım var?** 🤔
__(Destek için @Sonymusicdeveloper )__

🏷️ **Ortak Komutlar**:
\u2022 `/play` Bir sesi çalmak veya sıraya koymak için yanıtlama
\u2022 `/help` Komutları için yardım gösterir
\u2022 `/playlist` Çalma listesini gösterir
\u2022 `/current` Geçerli parçanın çalma süresini gösterir
\u2022 `/song` [şarkı adı] Şarkıyı ses olarak indir

🏷️ **Admin 🏷 ️ Komutları**:
\u2022 `/skip` Geçerli sesli Akımı atla 
\u2022 `/join` Geçerli grubun sesli sohbetine katıl
\u2022 `/leave` Geçerli sesli sohbeti bırak
\u2022 `/vc` Hangi vc'nin katıldığını kontrol edin
\u2022 `/stop` Müzik çalmayı durdur
\u2022 `/radio` Radyo akışını başlat
\u2022 `/stopradio` Radyo akışını durdur
\u2022 `/replay` Baştan oynat
\u2022 `/clean` Kullanılmayan RAW PCM dosyalarını kaldır
\u2022 `/pause` Müzik çalmayı duraklat
\u2022 `/resume` Müzik çalmaya devam et
\u2022 `/mute` VC kullanıcısının sesini kapatma
\u2022 `/unmute` VC kullanıcı botunun sesini aÇ
\u2022 `/restart` Botu yeniden başlat

🏷️ **Developer ** Geliştirici: @Sonymusicdeveloper* * Developer** 👑
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('KANAL', url='https://t.me/MazimFmOnline'),
        InlineKeyboardButton('DESTEK', url='https://t.me/Sonymusicdeveloper'),
    ],
    [
        InlineKeyboardButton('⚙️ HELP ⚙️', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
