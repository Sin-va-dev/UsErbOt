from telethon import events
from telethon.tl.types import ReplyInlineMarkup
import Handlers.client

client = Handlers.client.client

@events.register(events.NewMessage(outgoing=True , pattern=r'\.q'))
async def qutohandler(event):
    chat = await event.get_chat()
    repplied_msg = await event.get_reply_message()
    await repplied_msg.forward_to('@QuotLybot')
    print(event.message.id) 
    print(x)
    async with client.conversation('@QuotLyBot') as conv:
       x = await conv.get.message()
       