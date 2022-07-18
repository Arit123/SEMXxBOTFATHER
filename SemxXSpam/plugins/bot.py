
import os
import sys
import heroku3
from SemxXSpam import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY
from SemxXSpam import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from datetime import datetime

    
@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sjanu(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%slove(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def fuck(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        event = await e.reply("𝙋𝙤𝙣𝙜!", parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🎉 ⚔️🇽𝐄𝐑𝐕𝐈𝐒 ✘🇸𝐏𝐀𝐌𝐁𝐎𝐓⚔️ 🤖!\n✘`{ms}` ms\n 𝕁𝕆 Ⱨ𝕌𝕂𝕌𝕄 𝕄𝔼ℝ𝔼 𝔸𝔸𝕂𝔸😈🔥")
        
        

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your ⚔️🇽𝐄𝐑𝐕𝐈𝐒 ✘🇸𝐏𝐀𝐌𝐁𝐎𝐓⚔️...**\nPlease Wait For Few Seconds."
        await e.reply(text)
        try:
            await MK1.disconnect()
        except Exception:
            pass
        try:
            await MK2.disconnect()
        except Exception:
            pass
        try:
            await MK3.disconnect()
        except Exception:
            pass
        try:
            await MK4.disconnect()
        except Exception:
            pass
        try:
            await MK5.disconnect()
        except Exception:
            pass
        try:
            await MK6.disconnect()
        except Exception:
            pass
        try:
            await MK7.disconnect()
        except Exception:
            pass
        try:
            await MK8.disconnect()
        except Exception:
            pass
        try:
            await MK9.disconnect()
        except Exception:
            pass
        try:
            await MK10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"__Adding User As Sudo...__")
        mks = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To a User !!")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added** `{target}` **As Sudo User** ✨ \nRestarting... Please Wait Few Seconds.")
        heroku_var[mks] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
