# Don't Edit


import logging
from config import *
import asyncio
from database.users import *
from pyrogram import *
from pyrogram.types import *
from bot import *
from pyrogram.errors.exceptions.bad_request_400 import *


logger = logging.getLogger(__name__)

channel = UPDATE_CHANNEL

ft = f"Due To Overload Only Channel Sub Are Use This Bot Join @Shortnerfly."


# Private Chat
@Client.on_message(filters.private)
async def private_link_handler(c: Client, message: Message):

    try:
        Fsub = await force_sub(c, message, channel, ft)
        if Fsub == True:
            return
        user = await get_user(message.from_user.id)
        if message.text and message.text.startswith('/'):
            return
        if message.text:
            caption = message.text.html
        elif message.caption:
            caption = message.caption.html
        if len(await extract_link(caption)) <= 0 and not message.reply_markup:
            return
        user_method = user["method"]
        vld = await user_api_check(user)
        if vld is not True:
            return await message.reply_text(vld)
        try:
            txt = await message.reply('`Converting.......`', quote=True)

            await main_convertor_handler(message, user_method, user=user)
            await update_stats(message, user_method)
            bin_caption = f"""{caption}

#NewPost
From User :- {message.from_user.mention} [`{message.from_user.id}`]"""

            try:
                if LOG_CHANNEL and message.media:
                    await message.copy(LOG_CHANNEL, bin_caption)
                elif message.text and LOG_CHANNEL:
                    await c.send_message(LOG_CHANNEL, bin_caption, disable_web_page_preview=True)
            except PeerIdInvalid as e:
                logging.error("Make sure that the bot is admin in your log channel")
        except Exception as e:
            await message.reply(f"Error while trying to convert links {e}", quote=True)
            logger.exception(e)
        finally:
            await txt.delete()
            
    except Exception as e:
        logging.exception(e, exc_info=True)
