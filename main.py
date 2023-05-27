from email import message
from telethon import TelegramClient , events
from html_telegraph_poster.upload_images import upload_image
import Handlers.client , Handlers.greetings 
import Handlers.client , Handlers.greetings , Handlers.alive
import time 
import string



client = Handlers.client.client


with client as SVD:
    SVD.add_event_handler(Handlers.greetings.greeting)


@client.on(events.NewMessage(outgoing=True , pattern=r'\.alive'))
async def aliveHandler(event):
    chat = await event.get_chat()
    # await client.send_message(chat, "yes iruken da nalavanee")
    await client.delete_messages(chat , event.message)
    photo = await client.download_profile_photo('me')
    me = await client.get_me()

    time.sleep(3)
    await client.send_file(chat , file=photo , 
    caption=
    "nan than ds velakenna.\n\n"
    "owner [SVD_squad](https://t.me/SVD_squad)\n".format(me.username , '@SVD_squad')
    )


# -------------------- CLOSE ---------------------------------------------#


@client.on(events.NewMessage(outgoing=True , pattern=r'\.me'))
async def aboutme(event):
    chat = await event.get_chat()
    time.sleep(3)
    await client.edit_message(event.message , "my name is SVDSQUAD.")  


# -------------------- CLOSE --------------------------------------------- #

@client.on(events.NewMessage(outgoing=True , pattern=r'\.dir'))
async def telegraphUploadHandler(event):
    chat = await event.get_chat()
    time.sleep(6)
    await client.edit_message(event.message , "processiing....")
    replied = await event.get_reply_message()
    try:
        image = await replied.download_media()
        x = upload_image(image)
        await client.edit_message(event.message , "processiing....")
    except:
       time.sleep(5)
       return await  client.send_message(chat , "ina da looku ! olunga parru")
    image = await replied.download_media()
    
    await client.edit_message(event.message , x , link_preview=True)   





# main function
if __name__ == '__main__':
	msg = "Its looks like auto typing"
	
	# calling the function for printing the
	# characters with delay
	
from telethon import client

@client.onMessage(from_users="me")
async def echo(event):
    text = "You said __{}__!".format(event.text)
    await event.reply(text)



client.start()
client.run_until_disconnected()