
from telethon import events  
import Handlers.client
import os

client = Handlers.client

@events.register(events.NewMessage(outgoing=True , pattern=r'\.alive'))
async def aliveHandler(event):
    chat = await event.get_chat()
    # await client.send_message(chat, "yes iruken da nalavanee")
    await client.delete_messages(chat , event.message)
    photo = await client.download_profile_photo('me')
    me = await client.get_me()

    await client.send_file(chat , file=photo , 
    caption=
    "nan than ds velakenna.\n\n"
    "owner [SVD_squad](https://t.me/SVD_squad)\n".format(me.username , '@SVD_squad')
    )
    os.remove(photo)