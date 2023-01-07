# Don't Edit

import asyncio
import contextlib
import logging
import os
import re
import sys

from config import *
from database import *
from database.users import *
from helpers import *
from pyrogram import *
from pyrogram.errors import *
from pyrogram.types import *
from translation import *
from bot import *

logger = logging.getLogger(__name__)





@Client.on_callback_query(filters.regex(r"^ban"))
async def ban_cb_handler(c:Client,m: CallbackQuery):
    try:
        user_id = m.data.split("#")[1]
        user = await get_user(int(user_id))

        if user:
            if not user["banned"]:
                temp.BANNED_USERS.append(int(user_id))
                await update_user_info(user_id, {"banned": True})
                try:
                    owner = await c.get_users(int(OWNER_ID))
                    await c.send_message(user_id, f"You are now banned from the bot by Admin. Contact {owner.mention(style='md')} regarding this")
                except Exception as e:
                    logging.error(e)
                reply_markup = InlineKeyboardMarkup( [
                [
                    InlineKeyboardButton('Unban', callback_data=f'unban#{user_id}'),
                    InlineKeyboardButton('Close', callback_data='delete'),
                ]
            ])
                await m.edit_message_reply_markup(reply_markup)
                await m.answer(f"User [{user_id}] has been banned from the bot", show_alert=True)
            else:
                await m.answer("User is already banned", show_alert=True)
        else:
            await m.answer("User doesn't exist", show_alert=True)
    except Exception as e:
        logging.exception(e, exc_info=True)

@Client.on_callback_query(filters.regex("^unban"))
async def unban_cb_handler(c, m: CallbackQuery):
    user_id = m.data.split("#")[1]
    user = await get_user(int(user_id))
    if user:
        if user["banned"]:
            temp.BANNED_USERS.remove(int(user_id))
            await update_user_info(user_id, {"banned": False})
            with contextlib.suppress(Exception):
                await c.send_message(user_id, "You are now free to use the bot. You have been unbanned by the Admin")
            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Ban', callback_data=f'ban#{user_id}'), InlineKeyboardButton('Close', callback_data='delete')]])
            await m.edit_message_reply_markup(reply_markup)
            await m.answer("User is unbanned", show_alert=True)
        else:
            await m.answer("User is not banned yet", show_alert=True)
    else:
        await m.answer("User doesn't exist", show_alert=True)


@Client.on_callback_query(filters.regex("^setgs"))
async def user_setting_cb(c, query: CallbackQuery):
    _, setting, toggle, user_id = query.data.split('#')
    myvalues = {setting: toggle == "True"}
    await update_user_info(user_id, myvalues)
    user = await get_user(user_id)
    buttons = await get_me_button(user)
    reply_markup = InlineKeyboardMarkup(buttons)
    try:
        await query.message.edit_reply_markup(reply_markup)
        setting = re.sub("is|_", " ", setting).title()
        toggle = "Enabled" if toggle == "True" else "Disabled"
        await query.answer(f"{setting} {toggle} Successfully", show_alert=True)
    except Exception as e:
        logging.error("Error occurred while updating user information", exc_info=True)

@Client.on_callback_query()
async def on_callback_query(bot: Client, query: CallbackQuery):
    user_id = query.from_user.id
    h = Helpers()
    user = await get_user(user_id)
    if query.data == 'delete':
        await query.message.delete()
    elif query.data == 'help_command':
        await query.message.edit(HELP_MESSAGE.format(firstname=temp.FIRST_NAME, username=temp.BOT_USERNAME), reply_markup=HELP_REPLY_MARKUP, disable_web_page_preview=True)

    elif query.data == 'about_command':
        bot = await bot.get_me()
        await query.message.edit(ABOUT_TEXT.format(bot.mention(style='md')), reply_markup=ABOUT_REPLY_MARKUP, disable_web_page_preview=True)

    elif query.data == 'start_command':
        new_user = await get_user(query.from_user.id)
        tit = START_MESSAGE.format(query.from_user.mention, new_user["method"])

        await query.message.edit(tit, reply_markup=START_MESSAGE_REPLY_MARKUP, disable_web_page_preview=True)


    elif query.data == 'alias_conf':
        await query.message.edit(CUSTOM_ALIAS_MESSAGE, reply_markup=BACK_REPLY_MARKUP, disable_web_page_preview=True)

    elif query.data == 'admins_list':
        if user_id not in ADMINS:
            return await query.message.edit("Works only for admins", reply_markup=BACK_REPLY_MARKUP)

        await query.message.edit(ADMINS_MESSAGE.format(admin_list=await h.get_admins), reply_markup=BACK_REPLY_MARKUP)

    elif query.data == 'restart':
        await query.message.edit('**Restarting.....**')
        await asyncio.sleep(5)
        os.execl(sys.executable, sys.executable, *sys.argv)
    await query.answer()
