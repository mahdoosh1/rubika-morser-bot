# Any editing of this file without mention of owner and
# pretending to be the creator of the file is illegal .
#
# Rubika: @mahdoosh1, bot: @morserbot

from morser import decode , encode
from asyncio import run
from rubpy import Client , Message , models , handlers


client = Client(session="morsebot") 

async def main():

    async with client:
        @client.on(handlers.MessageUpdates())
        async def updates(message : Message):
            
            text = message.raw_text
            if text.startswith('enc'):
                mes_id = message.message_id
                text = text[4:]
                encoded = await encode(text.lower())
                await message.reply(encoded,reply_to_message_id=mes_id)
            elif text.startswith('dec'):
                mes_id = message.message_id
                text = text[4:]
                decoded = await decode(text)
                await message.reply(decoded,reply_to_message_id=mes_id)

        await client.run_until_disconnected()
run(main()) # Made by mahdoosh1
