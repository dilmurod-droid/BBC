# import logging
# import re
# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.types import Message
#
# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# CHANNEL_USERNAME = "@bbclduz"  # Kanalga post yuboriladi
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# OLD_LINKS = [
#     r'@tyxuzbek',
#     r'@BugungiGap'
# ]
#
# NEW_LINK = "@bbclduz"
#
# def replace_links(text: str) -> str:
#     for old_link in OLD_LINKS:
#         text = re.sub(old_link, NEW_LINK, text)
#     return text
#
# @dp.message(F.video)
# async def handle_text(message: Message):
#     original_text = message.text
#     modified_text = replace_links(original_text)
#
#     if original_text != modified_text:
#         await message.reply("✅ Silkalar o‘zgartirildi va kanalga yuborildi.")
#         try:
#             await bot.send_message(chat_id=CHANNEL_USERNAME, text=modified_text)
#         except Exception as e:
#             await message.reply(f"❌ Kanalga yuborishda xatolik: {e}")
#     else:
#         await message.reply("❗️Silkalar topilmadi yoki almashtirish shart emas.")
#
# async def main():
#     # Start polling with the bot instance and the Dispatcher
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import logging
# import re
# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.types import Message
# from aiogram.types import MessageEntity
# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# CHANNEL_USERNAME = "@bbclduz"  # Target channel username
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# NEW_LINK = "@bbclduz"
# # Regex to match @usernames
#
# def remove_words_with_entities(text: str, entities: list[MessageEntity]) -> str:
#     if not text or not entities:
#         return text
#
#     words = text.split()
#     # Calculate start/end indices of each word in text
#     char_pos = 0
#     word_positions = []
#     for w in words:
#         start = char_pos
#         end = start + len(w)
#         word_positions.append((start, end))
#         char_pos = end + 1  # account for space
#
#     remove_indices = set()
#     for entity in entities:
#         ent_start = entity.offset
#         ent_end = ent_start + entity.length
#         for i, (w_start, w_end) in enumerate(word_positions):
#             # If entity overlaps with word range, mark it for removal
#             if not (ent_end <= w_start or ent_start >= w_end):
#                 remove_indices.add(i)
#
#     filtered_words = [w for i, w in enumerate(words) if i not in remove_indices]
#
#     return ' '.join(filtered_words)
#
#
#
# @dp.message(F.video and F.photo)
# async def handle_video(message: Message):
#     text = message.text or message.caption or ""
#     entities = message.entities or message.caption_entities or []
#
#     modified_text = remove_words_with_entities(text, entities)
#
#     if modified_text != text:
#         # Append your new channel username at the end (optional)
#         modified_text = modified_text.strip() + " " + NEW_LINK
#
#         await message.reply("✅ Silkalar o‘chirildi va kanalga yuborildi.")
#         try:
#             if message.video:
#                 await bot.send_video(
#                     chat_id=CHANNEL_USERNAME,
#                     video=message.video.file_id,
#                     caption=modified_text
#                 )
#             elif message.photo:
#                 largest_photo = message.photo[-1]
#                 await bot.send_photo(
#                     chat_id=CHANNEL_USERNAME,
#                     photo=largest_photo.file_id,
#                     caption=modified_text
#                 )
#             else:
#                 # Just text message
#                 await bot.send_message(chat_id=CHANNEL_USERNAME, text=modified_text)
#         except Exception as e:
#             await message.reply(f"❌ Kanalga yuborishda xatolik: {e}")
#     else:
#         await message.reply("❗️Silka topilmadi yoki almashtirish shart emas.")
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
# import logging
# import asyncio
# import re
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.types import MessageEntity
#
# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# CHANNEL_USERNAME = "@bbclduz"
# NEW_LINK = "@bbclduz"
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# def remove_words_with_entities(text: str, entities: list[MessageEntity]) -> str:
#     if not text:
#         return text
#
#     if not entities:
#         # No entities - nothing to remove
#         return text
#
#     # Find words with punctuation separated (regex)
#     words = re.findall(r'\S+', text)
#     logging.info(f"Original words: {words}")
#
#     # Calculate start/end indices of each word in text
#     positions = []
#     pos = 0
#     for w in words:
#         start = text.find(w, pos)
#         end = start + len(w)
#         positions.append((start, end))
#         pos = end
#
#     logging.info(f"Word positions: {positions}")
#
#     # Mark words for removal if any entity overlaps
#     remove_indices = set()
#     for entity in entities:
#         ent_start = entity.offset
#         ent_end = ent_start + entity.length
#         logging.info(f"Entity: {entity.type} at {ent_start}-{ent_end}")
#
#         for i, (w_start, w_end) in enumerate(positions):
#             # If entity overlaps with word range
#             if not (ent_end <= w_start or ent_start >= w_end):
#                 remove_indices.add(i)
#                 logging.info(f"Marking word '{words[i]}' for removal")
#
#     # Remove words overlapping entities
#     filtered_words = [w for i, w in enumerate(words) if i not in remove_indices]
#
#     result = ' '.join(filtered_words)
#     logging.info(f"Result after removal: {result}")
#     return result
#
# @dp.message(F.TEXT and F.PHOTO and F.VIDEO)
# async def handle_message(message: types.Message):
#     text = message.text or message.caption or ""
#     entities = message.entities or message.caption_entities or []
#
#     logging.info(f"Received message text: {text}")
#     logging.info(f"Entities: {entities}")
#
#     modified_text = remove_words_with_entities(text, entities)
#
#     if modified_text != text:
#         modified_text = modified_text.strip() + " " + NEW_LINK
#
#         await message.reply("✅ Silkalar o‘chirildi va kanalga yuborildi.")
#         try:
#             if message.video:
#                 await bot.send_video(
#                     chat_id=CHANNEL_USERNAME,
#                     video=message.video.file_id,
#                     caption=modified_text
#                 )
#             elif message.photo:
#                 largest_photo = message.photo[-1]
#                 await bot.send_photo(
#                     chat_id=CHANNEL_USERNAME,
#                     photo=largest_photo.file_id,
#                     caption=modified_text
#                 )
#             else:
#                 await bot.send_message(chat_id=CHANNEL_USERNAME, text=modified_text)
#         except Exception as e:
#             await message.reply(f"❌ Kanalga yuborishda xatolik: {e}")
#     else:
#         await message.reply("❗️Silka topilmadi yoki almashtirish shart emas.")
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import re
# import asyncio
# from aiogram import Bot, Dispatcher, types, F
#
# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # Old links or mentions to detect
# OLD_LINKS = [
#     r"@tyxuzbek",
#     r"@BugungiGap",
#     r"kun\.uz",
#     r"t\.me/kunuzofficial",
#     # add more patterns if needed
# ]
#
# # Regex to find URLs (simple version)
# URL_REGEX = r"(https?://[^\s]+)"
#
# # Combine old mentions/links patterns
# OLD_LINKS_REGEX = "|".join(OLD_LINKS)
#
# def contains_old_link_or_url(text: str) -> bool:
#     if not text:
#         return False
#
#     # Check if any Telegram entity of type url or mention exists
#     # We'll also check with regex for old links or urls
#     if re.search(URL_REGEX, text, re.IGNORECASE):
#         return True
#     if re.search(OLD_LINKS_REGEX, text, re.IGNORECASE):
#         return True
#     return False
#
# @dp.message(F.TEXT and F.PHOTO and F.VIDEO)
# async def check_links(message: types.Message):
#     text = message.text or message.caption or ""
#
#     if contains_old_link_or_url(text):
#         await message.reply("✅ Link yoki mention topildi va qayta ishlanadi.")
#     else:
#         await message.reply("❗️ Link yoki mention topilmadi.")
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import MessageEntity
# import re
# import logging
#
# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# CHANNEL_USERNAME = "@bbclduz"
# NEW_LINK = "@bbclduz"
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
#
# def clean_telegram_links(text: str, entities: list[MessageEntity]) -> str:
#     if not text:
#         return text
#
#     remove_spans = []
#     for entity in entities:
#         if entity.type in ["url", "text_link", "mention"]:
#             remove_spans.append((entity.offset, entity.offset + entity.length))
#
#     for start, end in sorted(remove_spans, reverse=True):
#         text = text[:start] + text[end:]
#
#     text = re.sub(r'@[\w\d_]+', '', text)
#     text = re.sub(r'https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+', '', text)
#     return re.sub(r'\s+', ' ', text).strip()
#
#
# @dp.message()
# async def handle_message(message: types.Message):
#     text = message.text or message.caption or ""
#     entities = message.entities or message.caption_entities or []
#
#     modified_text = clean_telegram_links(text, entities)
#
#     if modified_text != text:
#         modified_text = modified_text + " " + NEW_LINK
#         await message.reply("✅ Silkalar o‘chirildi va kanalga yuborildi.")
#
#         try:
#             if message.video:
#                 await bot.send_video(CHANNEL_USERNAME, message.video.file_id, caption=modified_text)
#             elif message.photo:
#                 await bot.send_photo(CHANNEL_USERNAME, message.photo[-1].file_id, caption=modified_text)
#             else:
#                 await bot.send_message(CHANNEL_USERNAME, modified_text)
#         except Exception as e:
#             await message.reply(f"❌ Xatolik: {e}")
#     else:
#         await message.reply("❗️Silka topilmadi yoki almashtirish shart emas.")
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import asyncio
# import logging
# import re
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import MessageEntity
#
# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# CHANNEL_USERNAME = "@bbclduz"
# NEW_LINK = "@bbclduz"
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# bot.session.default_parse_mode = "HTML"  # ✅ FIX for v3.7+
# dp = Dispatcher()
#
#
# def clean_links_preserve_formatting(text: str, entities: list[MessageEntity]) -> str:
#     if not text:
#         return ""
#
#     result_parts = []
#     last_idx = 0
#
#     for entity in sorted(entities, key=lambda e: e.offset):
#         start = entity.offset
#         end = start + entity.length
#
#         if entity.type in ["url", "text_link", "mention"]:
#             result_parts.append(text[last_idx:start])  # skip link
#             last_idx = end
#         else:
#             result_parts.append(text[last_idx:end])  # keep
#             last_idx = end
#
#     result_parts.append(text[last_idx:])
#     cleaned_text = ''.join(result_parts)
#
#     # Also clean raw @username and t.me links
#     cleaned_text = re.sub(r'@[\w\d_]+', '', cleaned_text)
#     cleaned_text = re.sub(r'https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+', '', cleaned_text)
#
#     return re.sub(r'\s+', ' ', cleaned_text).strip()
#
#
# @dp.message()
# async def handle_message(message: types.Message):
#     text = message.text or message.caption or ""
#     entities = message.entities or message.caption_entities or []
#
#     modified_text = clean_links_preserve_formatting(text, entities)
#
#     if modified_text != text:
#         modified_text = modified_text.strip() + " " + NEW_LINK
#         await message.reply("✅ Silkalar o‘chirildi va kanalga yuborildi.")
#
#         try:
#             if message.video:
#                 await bot.send_video(
#                     chat_id=CHANNEL_USERNAME,
#                     video=message.video.file_id,
#                     caption=modified_text
#                 )
#             elif message.photo:
#                 largest_photo = message.photo[-1]
#                 await bot.send_photo(
#                     chat_id=CHANNEL_USERNAME,
#                     photo=largest_photo.file_id,
#                     caption=modified_text
#                 )
#             else:
#                 await bot.send_message(chat_id=CHANNEL_USERNAME, text=modified_text)
#         except Exception as e:
#             await message.reply(f"❌ Kanalga yuborishda xatolik: {e}")
#     else:
#         await message.reply("❗️Silka topilmadi yoki almashtirish shart emas.")
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import asyncio
# import json
# import logging
# import os
# import re
# import ssl  # Ensures ssl is explicitly imported
# from html.parser import HTMLParser
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.enums import ParseMode
# from aiogram.types import InputMediaPhoto, InputMediaVideo

# API_TOKEN = "8022760553:AAF-XKj3e9l_jt_wRjH5mtiN_7umauNXsEw"
# CHANNEL_USERNAME = "@bbclduz"
# ADMINS_FILE = "admins.json"

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()

# def load_json(filename, default):
#     if not os.path.exists(filename):
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(default, f)
#         return default
#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             content = f.read().strip()
#             return json.loads(content) if content else default
#     except Exception as e:
#         logging.error(f"Failed to load {filename}: {e}")
#         return default

# def save_json(filename, data):
#     try:
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4, ensure_ascii=False)
#     except Exception as e:
#         logging.error(f"Failed to save {filename}: {e}")

# ADMINS = set(load_json(ADMINS_FILE, [6667155546, 7148646716]))

# def save_admins():
#     save_json(ADMINS_FILE, list(ADMINS))

# class SafeHTMLCleaner(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.result = []

#     def handle_starttag(self, tag, attrs):
#         if tag in {"b", "i", "u", "s", "code", "pre", "a"}:
#             attr_str = ' '.join(f'{k}="{v}"' for k, v in attrs)
#             self.result.append(f"<{tag} {attr_str}>")

#     def handle_endtag(self, tag):
#         if tag in {"b", "i", "u", "s", "code", "pre", "a"}:
#             self.result.append(f"</{tag}>")

#     def handle_data(self, data):
#         data = re.sub(r'\(?(https?://[^\s()]+)\)?', '', data)
#         data = re.sub(r'\(?(t\.me/[^\s()]+)\)?', '', data)
#         data = re.sub(r'\(?(telegram\.me/[^\s()]+)\)?', '', data)
#         data = re.sub(r"@[\w_]+", "", data)
#         self.result.append(data)

#     def get_cleaned(self):
#         return ''.join(self.result)

# def clean_text_preserve_html(text: str) -> str:
#     parser = SafeHTMLCleaner()
#     parser.feed(text)
#     return parser.get_cleaned().strip()

# def insert_at_symbol(text: str, tag: str) -> str:
#     markers = ["👉", "⚡️"]
#     for mark in markers:
#         if mark in text:
#             return text.replace(mark, f"{mark} {tag}", 1)
#     return text.strip() + f" {tag}"

# @dp.message(F.text == "/start")
# async def cmd_start(message: types.Message):
#     if message.from_user.id in ADMINS:
#         await message.reply("👋 Salom, admin! Xabar yuborishingiz mumkin.")
#     else:
#         await message.reply("❗️ Ushbu bot faqat adminlar uchun mo'ljallangan.")

# media_group_buffers = {}

# @dp.message(F.from_user.id.in_(ADMINS), F.media_group_id)
# async def handle_album(message: types.Message):
#     group_id = message.media_group_id
#     media_group_buffers.setdefault(group_id, []).append(message)
#     await asyncio.sleep(1.2)

#     messages = media_group_buffers.pop(group_id, [])
#     if not messages:
#         return

#     caption_message = next((m for m in messages if m.caption), messages[0])
#     text = caption_message.caption or ""
#     cleaned = clean_text_preserve_html(text)
#     tag = f"<a href='https://t.me/{CHANNEL_USERNAME.lstrip('@')}'>{CHANNEL_USERNAME}</a>"
#     cleaned = insert_at_symbol(cleaned, tag)

#     media = []
#     for i, msg in enumerate(messages):
#         caption = cleaned if i == 0 else None
#         if msg.photo:
#             media.append(InputMediaPhoto(media=msg.photo[-1].file_id, caption=caption, parse_mode=ParseMode.HTML))
#         elif msg.video:
#             media.append(InputMediaVideo(media=msg.video.file_id, caption=caption, parse_mode=ParseMode.HTML))

#     try:
#         await bot.send_media_group(chat_id=CHANNEL_USERNAME, media=media)
#         await caption_message.reply("✅ Media guruhi kanalga yuborildi.")
#     except Exception as e:
#         await caption_message.reply(f"❌ Xatolik: {e}")

# @dp.message(F.from_user.id.in_(ADMINS))
# async def handle_admin_message(message: types.Message):
#     text = message.text or message.caption or ""
#     if not text and not (message.photo or message.video):
#         await message.reply("❗️ Matn, rasm yoki video jo'nating.")
#         return

#     cleaned = clean_text_preserve_html(text)
#     tag = f"<a href='https://t.me/{CHANNEL_USERNAME.lstrip('@')}'>{CHANNEL_USERNAME}</a>"
#     cleaned = insert_at_symbol(cleaned, tag)

#     try:
#         if message.photo:
#             await bot.send_photo(CHANNEL_USERNAME, message.photo[-1].file_id, caption=cleaned, parse_mode=ParseMode.HTML)
#         elif message.video:
#             await bot.send_video(CHANNEL_USERNAME, message.video.file_id, caption=cleaned, parse_mode=ParseMode.HTML)
#         else:
#             await bot.send_message(CHANNEL_USERNAME, cleaned, parse_mode=ParseMode.HTML)

#         await message.reply("✅ Xabar kanalga yuborildi.")
#     except Exception as e:
#         await message.reply(f"❌ Yuborishda xatolik: {e}")

# @dp.message()
# async def handle_non_admin(message: types.Message):
#     if message.from_user.id not in ADMINS:
#         logging.info(f"⛔️ Blocked message from non-admin: {message.from_user.id}")

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
# import asyncio
# import json
# import logging
# import os
# import re
# import ssl  # Ensures ssl is explicitly imported
# from html.parser import HTMLParser
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.enums import ParseMode
# from aiogram.types import InputMediaPhoto, InputMediaVideo, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# API_TOKEN = "7364378096:AAHQ14X098RshIlptl8fm7ZEepYA3dIsAQY"
# CHANNEL_USERNAME = "@bbclduz"
# ADMINS_FILE = "admins.json"

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()

# user_states = {}  # user_id: {"mode": "with"/"without", "link": str}

# def load_json(filename, default):
#     if not os.path.exists(filename):
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(default, f)
#         return default
#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             content = f.read().strip()
#             return json.loads(content) if content else default
#     except Exception as e:
#         logging.error(f"Failed to load {filename}: {e}")
#         return default

# def save_json(filename, data):
#     try:
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4, ensure_ascii=False)
#     except Exception as e:
#         logging.error(f"Failed to save {filename}: {e}")

# ADMINS = set(load_json(ADMINS_FILE, [6667155546, 7148646716]))

# def save_admins():
#     save_json(ADMINS_FILE, list(ADMINS))

# class SafeHTMLCleaner(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.result = []

#     def handle_starttag(self, tag, attrs):
#         if tag in {"b", "i", "u", "s", "code", "pre", "a"}:
#             attr_str = ' '.join(f'{k}="{v}"' for k, v in attrs)
#             self.result.append(f"<{tag} {attr_str}>")

#     def handle_endtag(self, tag):
#         if tag in {"b", "i", "u", "s", "code", "pre", "a"}:
#             self.result.append(f"</{tag}>")

#     def handle_data(self, data):
#         data = re.sub(r'\(?https?://[^\s()]+\)?', '', data)
#         data = re.sub(r'\(?t\.me/[^\s()]+\)?', '', data)
#         data = re.sub(r'\(?telegram\.me/[^\s()]+\)?', '', data)
#         data = re.sub(r"@[\w_]+", "", data)
#         self.result.append(data)

#     def get_cleaned(self):
#         return ''.join(self.result)

# def clean_text_preserve_html(text: str) -> str:
#     parser = SafeHTMLCleaner()
#     parser.feed(text)
#     return parser.get_cleaned().strip()

# def insert_at_symbol(text: str, tag: str) -> str:
#     markers = ["👉", "⚡️"]
#     for mark in markers:
#         if mark in text:
#             return text.replace(mark, f"{mark} {tag}", 1)
#     return text.strip() + f" {tag}"

# @dp.message(F.text == "/start")
# async def cmd_start(message: types.Message):
#     if message.from_user.id in ADMINS:
#         keyboard = ReplyKeyboardMarkup(
#             keyboard=[
#                 [KeyboardButton(text="With Button")],
#                 [KeyboardButton(text="Without Button")]
#             ],
#             resize_keyboard=True
#         )
#         await message.reply("👋 Salom, admin! Quyidagilardan birini tanlang:", reply_markup=keyboard)
#     else:
#         await message.reply("❗️ Ushbu bot faqat adminlar uchun mo'ljallangan.")

# @dp.message(F.text.in_(["With Button", "Without Button"]))
# async def handle_choice(message: types.Message):
#     choice = message.text
#     user_id = message.from_user.id
#     mode = "with" if choice == "With Button" else "without"
#     user_states[user_id] = {"mode": mode, "link": None}
#     if mode == "with":
#         await message.reply("🔗 Iltimos, tugma uchun havolani yuboring:", reply_markup=ReplyKeyboardRemove())
#     else:
#         await message.reply("✉️ Endi xabar, rasm yoki video yuboring:", reply_markup=ReplyKeyboardRemove())

# @dp.message(F.text.startswith("http"))
# async def handle_link(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in user_states and user_states[user_id]["mode"] == "with" and not user_states[user_id]["link"]:
#         user_states[user_id]["link"] = message.text.strip()
#         await message.reply("✅ Endi xabar, rasm yoki video yuboring:")

# @dp.message(F.from_user.id.in_(ADMINS), F.media_group_id)
# async def handle_album(message: types.Message):
#     group_id = message.media_group_id
#     media_group_buffers.setdefault(group_id, []).append(message)
#     await asyncio.sleep(1.2)

#     messages = media_group_buffers.pop(group_id, [])
#     if not messages:
#         return

#     caption_message = next((m for m in messages if m.caption), messages[0])
#     text = caption_message.caption or ""
#     cleaned = clean_text_preserve_html(text)
#     tag = f"<a href='https://t.me/{CHANNEL_USERNAME.lstrip('@')}'>{CHANNEL_USERNAME}</a>"
#     cleaned = insert_at_symbol(cleaned, tag)

#     user_id = caption_message.from_user.id
#     user_data = user_states.get(user_id, {})
#     if user_data.get("mode") == "with" and user_data.get("link"):
#         markup = InlineKeyboardMarkup(inline_keyboard=[[
#             InlineKeyboardButton(text="Davomini o'qish...", url=user_data["link"])
#         ]])
#     else:
#         markup = None

#     media = []
#     for i, msg in enumerate(messages):
#         caption = cleaned if i == 0 else None
#         if msg.photo:
#             media.append(InputMediaPhoto(media=msg.photo[-1].file_id, caption=caption, parse_mode=ParseMode.HTML))
#         elif msg.video:
#             media.append(InputMediaVideo(media=msg.video.file_id, caption=caption, parse_mode=ParseMode.HTML))

#     try:
#         if markup and len(media) == 1:
#             if media[0].type == "photo":
#                 await bot.send_photo(CHANNEL_USERNAME, media[0].media, caption=media[0].caption, parse_mode=ParseMode.HTML, reply_markup=markup)
#             else:
#                 await bot.send_video(CHANNEL_USERNAME, media[0].media, caption=media[0].caption, parse_mode=ParseMode.HTML, reply_markup=markup)
#         else:
#             await bot.send_media_group(chat_id=CHANNEL_USERNAME, media=media)

#         await caption_message.reply("✅ Media guruhi kanalga yuborildi.")
#     except Exception as e:
#         await caption_message.reply(f"❌ Xatolik: {e}")

# @dp.message(F.from_user.id.in_(ADMINS))
# async def handle_admin_message(message: types.Message):
#     user_id = message.from_user.id
#     text = message.text or message.caption or ""
#     if not text and not (message.photo or message.video):
#         await message.reply("❗️ Matn, rasm yoki video jo'nating.")
#         return

#     cleaned = clean_text_preserve_html(text)
#     tag = f"<a href='https://t.me/{CHANNEL_USERNAME.lstrip('@')}'>{CHANNEL_USERNAME}</a>"
#     cleaned = insert_at_symbol(cleaned, tag)

#     user_data = user_states.get(user_id, {})
#     markup = None
#     if user_data.get("mode") == "with" and user_data.get("link"):
#         markup = InlineKeyboardMarkup(inline_keyboard=[[
#             InlineKeyboardButton(text="Davomini o'qish...", url=user_data["link"])
#         ]])

#     try:
#         if message.photo:
#             await bot.send_photo(CHANNEL_USERNAME, message.photo[-1].file_id, caption=cleaned, parse_mode=ParseMode.HTML, reply_markup=markup)
#         elif message.video:
#             await bot.send_video(CHANNEL_USERNAME, message.video.file_id, caption=cleaned, parse_mode=ParseMode.HTML, reply_markup=markup)
#         else:
#             await bot.send_message(CHANNEL_USERNAME, cleaned, parse_mode=ParseMode.HTML, reply_markup=markup)

#         await message.reply("✅ Xabar kanalga yuborildi.")
#         user_states.pop(user_id, None)  # Clear state
#     except Exception as e:
#         await message.reply(f"❌ Yuborishda xatolik: {e}")

# @dp.message()
# async def handle_non_admin(message: types.Message):
#     if message.from_user.id not in ADMINS:
#         logging.info(f"⛔️ Blocked message from non-admin: {message.from_user.id}")

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import json
import logging
import os
import re
from html.parser import HTMLParser
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.types import InputMediaPhoto, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMedia
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = "7364378096:AAHQ14X098RshIlptl8fm7ZEepYA3dIsAQY"
CHANNEL_USERNAME = "@bbclduz"
ADMINS_FILE = "admins.json"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class Form(StatesGroup):
    choose_mode = State()
    ask_link = State()
    ask_target_channel = State()
    save_content = State()

pending_messages = {}
media_groups = {}

# --- Helpers ---
def load_json(filename, default):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(default, f)
        return default
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return json.loads(content) if content else default
    except Exception as e:
        logging.error(f"Failed to load {filename}: {e}")
        return default

def save_json(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Failed to save {filename}: {e}")

ADMINS = set(load_json(ADMINS_FILE, [6667155546, 7148646716]))

def save_admins():
    save_json(ADMINS_FILE, list(ADMINS))

class SafeHTMLCleaner(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_starttag(self, tag, attrs):
        if tag in {"b", "i", "u", "s", "code", "pre", "a"}:
            attr_str = ' '.join(f'{k}="{v}"' for k, v in attrs)
            self.result.append(f"<{tag} {attr_str}>")

    def handle_endtag(self, tag):
        if tag in {"b", "i", "u", "s", "code", "pre", "a"}:
            self.result.append(f"</{tag}>")

    def handle_data(self, data):
        data = re.sub(r'\(?https?://[^\s()]+\)?', '', data)
        data = re.sub(r'\(?t\.me/[^\s()]+\)?', '', data)
        data = re.sub(r'\(?telegram\.me/[^\s()]+\)?', '', data)
        data = re.sub(r"@[\w_]+", "", data)
        self.result.append(data)

    def get_cleaned(self):
        return ''.join(self.result)

def clean_text_preserve_html(text: str) -> str:
    parser = SafeHTMLCleaner()
    parser.feed(text)
    return parser.get_cleaned().strip()

def insert_at_symbol(text: str, tag: str) -> str:
    markers = ["👉", "⚡️"]
    for mark in markers:
        if mark in text:
            return text.replace(mark, f"{mark} {tag}", 1)
    return text.strip() + f" {tag}"

@dp.message(F.text == "/start")
async def cmd_start(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="With Button", callback_data="with_button")],
            [InlineKeyboardButton(text="Without Button", callback_data="without_button")]
        ])
        await message.answer("Choose message type:", reply_markup=keyboard)
        await state.set_state(Form.choose_mode)
    else:
        await message.reply("❗️ Ushbu bot faqat adminlar uchun mo'ljallangan.")

@dp.callback_query(F.data.in_({"with_button", "without_button"}))
async def choose_button_mode(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(button_mode=callback.data)
    if callback.data == "with_button":
        await callback.message.answer("Iltimos, linkni yuboring:")
        await state.set_state(Form.ask_link)
    else:
        await callback.message.answer("Endi xabarni yuboring.")
        await state.set_state(Form.save_content)

@dp.message(Form.ask_link)
async def receive_link(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer("Kanal username-ni yuboring (masalan: @mychannel):")
    await state.set_state(Form.ask_target_channel)

@dp.message(Form.ask_target_channel)
async def receive_target_channel(message: types.Message, state: FSMContext):
    await state.update_data(target_channel=message.text.strip())
    await message.answer("Endi xabarni yuboring.")
    await state.set_state(Form.save_content)

@dp.message(Form.save_content)
async def handle_final_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = message.from_user.id
    media_group_id = message.media_group_id
    tag = f"<a href='https://t.me/{CHANNEL_USERNAME.lstrip('@')}'>{CHANNEL_USERNAME}</a>"
    reply_markup = None
    second_markup = None

    if media_group_id:
        media_groups.setdefault(media_group_id, []).append(message)
        await asyncio.sleep(1.5)  # Short delay to allow group to finish

        messages = media_groups.pop(media_group_id, [])
        if len(messages) < 2:
            return  # Let the single one fall through normally

        media = []
        caption = messages[0].caption or messages[0].text or ""
        cleaned = clean_text_preserve_html(caption)
        cleaned = insert_at_symbol(cleaned, tag)

        if data.get("button_mode") == "with_button":
            ref_id = f"{user_id}_{messages[0].message_id}"
            reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Davomini o'qish...", url=f"https://t.me/{data.get('target_channel').lstrip('@')}")]
            ])
            second_markup = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Davomini o'qish...", callback_data=f"readmore:{ref_id}")]
            ])
            pending_messages[ref_id] = {
                "link": data.get("link"),
                "target_channel": data.get("target_channel")
            }

        for i, msg in enumerate(messages):
            file = msg.photo[-1].file_id if msg.photo else msg.video.file_id
            media_type = "photo" if msg.photo else "video"
            caption_text = cleaned if i == 0 else None
            input_media = (
                InputMediaPhoto(media=file, caption=caption_text, parse_mode=ParseMode.HTML) if media_type == "photo"
                else InputMediaVideo(media=file, caption=caption_text, parse_mode=ParseMode.HTML)
            )
            media.append(input_media)

        await bot.send_media_group(CHANNEL_USERNAME, media)
        if second_markup:
            await bot.send_media_group(data.get("target_channel"), media, reply_markup=second_markup)
        await message.reply("✅ Xabar guruh holatida yuborildi.")
        await state.clear()
        return

    # Single media or text
    text = message.text or message.caption or ""
    cleaned = clean_text_preserve_html(text)
    cleaned = insert_at_symbol(cleaned, tag)

    if data.get("button_mode") == "with_button":
        ref_id = f"{user_id}_{message.message_id}"
        reply_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Davomini o'qish...", url=f"https://t.me/{data.get('target_channel').lstrip('@')}")]
        ])
        second_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Davomini o'qish...", callback_data=f"readmore:{ref_id}")]
        ])
        pending_messages[ref_id] = {
            "link": data.get("link"),
            "target_channel": data.get("target_channel")
        }

    try:
        if message.photo:
            await bot.send_photo(CHANNEL_USERNAME, message.photo[-1].file_id, caption=cleaned, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            if second_markup:
                await bot.send_photo(data["target_channel"], message.photo[-1].file_id, caption=cleaned, parse_mode=ParseMode.HTML, reply_markup=second_markup)
        elif message.video:
            await bot.send_video(CHANNEL_USERNAME, message.video.file_id, caption=cleaned, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            if second_markup:
                await bot.send_video(data["target_channel"], message.video.file_id, caption=cleaned, parse_mode=ParseMode.HTML, reply_markup=second_markup)
        else:
            await bot.send_message(CHANNEL_USERNAME, cleaned, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
            if second_markup:
                await bot.send_message(data["target_channel"], cleaned, parse_mode=ParseMode.HTML, reply_markup=second_markup)

        await message.reply("✅ Xabar yuborildi.")
    except Exception as e:
        await message.reply(f"❌ Yuborishda xatolik: {e}")

    await state.clear()

@dp.callback_query(F.data.startswith("readmore:"))
async def handle_readmore(callback: CallbackQuery):
    ref_id = callback.data.split(":", 1)[1]
    info = pending_messages.get(ref_id)
    if not info:
        await callback.message.answer("❌ Ma'lumot topilmadi.")
        return

    user_id = callback.from_user.id
    try:
        member = await bot.get_chat_member(chat_id=info["target_channel"], user_id=user_id)
        if member.status in ("member", "administrator", "creator"):
            await callback.message.answer(f"✅ <a href='{info['link']}'>Ma'lumotni o'qish</a>", parse_mode=ParseMode.HTML)
        else:
            raise Exception("Not a member")
    except:
        await callback.message.answer("❗️Avval kanalga obuna bo'ling.")

@dp.message()
async def handle_non_admin(message: types.Message):
    if message.from_user.id not in ADMINS:
        logging.info(f"⛔️ Blocked message from non-admin: {message.from_user.id}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

