from pyrogram import filters, Client
from pyrogram.types import CallbackQuery
from pyrocon import Askclient

app = Client("AskPyro", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

read = Askclient(app)

@app.on_callback_query()  
async def callback(_, msg: CallbackQuery):
    answer = await read.ask(msg, "ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ʙʀᴏ ?", alert=True)
    await answer.reply(f"ʏᴏᴜʀ ᴀɴsᴡᴇʀ ɪs {ans.text}")
    
app.run()
