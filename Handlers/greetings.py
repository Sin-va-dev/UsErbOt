from telethon import events 

@events.register(events.NewMessage(outgoing=True , pattern=r'\.hello'))
async def greeting(event):
    chat = await event.get_chat()
    await event.reply("yara nee")