#pylint:disable=W0602
#pylint:disable=W0122
#pylint:disable=W0603
#pylint:disable=W0702
#pylint:disable=E1101
from rubpy import Client, handlers, Message, models
import asyncio
import os
from assistor import result as air
from morser import decode , encode
import random

def st(msg, key):
    if msg.raw_text.startswith(key):
        return msg.raw_text[len(key)+1:]

me = "u03S1P0443f1c947872906d2263a54cd"
swears = [
"کیر", "کص", "جق", "تناسل", "واژن", "بیدمشک", "حامله", "پورن", "کون", "ممه", "جنده",
"sex", "dick", "penis", "pussy", "vugina", "vulva", "porn", "ass", "boob", "fuck"
]

seen = []
warns = {}
def save(text, file):
    with open(file,'w') as f:
        f.write(text)
def load(file):
    with open(file,'r') as f:
        return f.read()
try:
    ps = load('lp.ps')
    warns = dict(load('warns.txt'))
    swears = list(set(swears + list(load('swears.txt'))))
except:
    ps = "1289"
bin2 = lambda inp: bin(inp)[2:]
def textbin(text):
    return ' '.join(list(map(bin2,map(ord,list(text)))))
async def domorse(text):
    if text is None: return None
    if text == "help":
    	return """ Commands:
-[msg]    message to ai chatbot
cp [oldpass] [newpass]    change root password
[pass] [command]    run a command from shell
[pass] py [command]    run a python command
enm [msg] encode message to code morse
dem [morse] decode morse code
enc [msg] encode message to binary
dec [bin] decode binary message
note that by asking to execute code, owner will verify and then run the command.
"""
    if text.startswith('enm'):
        text = text[4:]
        encoded = await encode(text.lower())
        return encoded
    elif text.startswith('dem'):
        text = text[4:]
        decoded = await decode(text)
        return decoded
    else:
        return None
def do(msg,psi=None):
    # print(msg, ps)
    if msg is None: return None
    if msg.startswith("enc"):
        text = msg[4:]
        return textbin(text)
    elif msg.startswith("dec"):
        text = msg[4:]
        dec = lambda inp: chr(int(inp,2))
        return ''.join(map(dec, text.split(" ")))
    if psi is None:
        global ps
    else:
        ps = psi
    if msg.startswith(ps):
        nxt = msg[5:]
        if nxt[:2] == "py":
            if input("execute "+nxt+" ?") == "yes":
                exec(nxt[3:])
            else:
                return "access denied"
        elif nxt != "end":
            if input("execute "+nxt+" ?") == "yes" or nxt == "":
                os.system(nxt)
            else:
                return "access denied"
        else:
            exit()
        return f"bot executed \"{nxt}\"."
    elif msg.startswith("cp"):
        if msg[3:7] == ps and input(f"change pass from {ps} to {msg[8:13]} ?") == "y":
            ps = msg[8:13]
            save(ps,'lp.ps')
            return "password changed successfully"
        else:
            return "password change failed, old password was wrong."
    elif msg.startswith("-"):
        return msg[1:]+":\n\n"+air(msg[1:])
run = True
async def main():
    global ps, me, swears, warns, seen, run
    async with Client(session="morsebot") as client:
        run = True
        print("client: ")
        print(str(await client.get_me())[72:93])
        @client.on(handlers.MessageUpdates(models.is_private()))
        async def updates(message: Message):
                # print("b")
                for i in swears:
                    if i in message.raw_text and message.author_guid != me:
                        if not message.author_guid in warns.keys():
                            await message.reply("اخطار اگر دوباره از این نوع کلمات استفاده کنید ربات برای شما غیرفعال خواهد شد.")
                            warns[message.author_guid] = False
                            save(str(warns),'warns.txt')
                        elif not warns[message.author_guid]:
                            warns[message.author_guid] = True
                            save(str(warns),'warns.txt')
                        return None
                if message.author_guid in warns.keys():
                    if warns[message.author_guid]:
                        return
                    else:
                        result = await domorse(message.raw_text)
                        if result is None:
                            result = do(message.raw_text,ps)
                        if result is None:
                            pass
                        elif type(result) is str:
                            result = "شما دارای اخطار هستید اگر دوباره اخطار بگیرید ربات برای شما غیرفعال خواهد شد\n\n" + result
                            await message.reply(result)
                        return
                print(message.raw_text)
                result = await domorse(message.raw_text)
                if result is None:
                    result = do(message.raw_text,ps)
                if result is None:
                    pass
                elif type(result) is str:
                    await message.reply(result)
        @client.on(handlers.MessageUpdates(models.is_group()))
        async def updates2(message: Message):
            global run
            try:
                if "یک عضو" in message.raw_text:
                    return
            except:
                return
            if message.object_guid != "g0Cic160ebb0c1e8eff64188b1ca71b8":
                async def author(txt):
                    return str(await client.get_user_info(txt))
                if message.raw_text == "guid":
                    await message.reply(
                    "here: `"+message.object_guid+"`\nyou: `"+message.author_guid+"`")
                elif (txt := st(message, "random")):
                    test = True
                    for i in txt:
                        if not i in "0123456789.۰۱۲۳۴۵۶۷۸۹. -":
                            await message.reply("Invalid input")
                            test = False
                    if test:
                        txt = txt.replace("۰","0")
                        txt = txt.replace("۱","1")
                        txt = txt.replace("۲","2")
                        txt = txt.replace("۳","3")
                        txt = txt.replace("۴","4")
                        txt = txt.replace("۵","5")
                        txt = txt.replace("۶","6")
                        txt = txt.replace("۷","7")
                        txt = txt.replace("۸","8")
                        txt = txt.replace("۹","9")
                        txt = txt.replace(".",".")
                        txt = txt.split(" ")
                        if len(txt) == 1:
                            await message.reply(str(random.randint(0, int(txt[0]))))
                        elif len(txt) == 2:
                            await message.reply(str(random.randint(int(txt[0]),int(txt[1]))))
                elif (txt := st(message,"ban")) and message.author_guid == me:
                    warns[txt] = True
                    save(str(warns),'warns.txt')
                    he = await author(txt)
                    await client.send_message(me,"banned")
                    await message.reply("Banned @"+
                    he[he.find("username")+10:he.find("last_online")-3]
                    )
                elif (txt := st(message,"unban")) and message.author_guid == me:
                    warns[txt] = False
                    save(str(warns),'warns.txt')
                    he = await author(txt)
                    await client.send_message(me, "unbanned")
                    await message.reply("Unbanned @"+
                    he[he.find("username")+10:he.find("last_online")-3]
                    )
                elif (txt := st(message,"add")) and message.author_guid == me:
                    swears.append(txt)
                    save(str(txt),'swears.txt')
                    await message.reply("The word '"+txt+"' added as swear word")
                elif (txt := st(message,"rem")) and message.author_guid == me:
                    swears.remove(txt)
                    save(str(txt),'swears.txt')
                    await message.reply("The word '"+txt+"' removed from swear word list")
                elif run and message.raw_text.startswith("off") and message.author_guid == me:
                    run = False
                    await message.reply("Turned off")
                elif (not run) and message.raw_text.startswith("on") and message.author_guid == me:
                    run = True
                    await message.reply("Turned on")
                else:
                    if run:
                        await updates(message)
                        if not message.author_guid in seen:
                            he = await author(message.author_guid)
                            await client.send_message(me,
                                "@"+he[he.find("username")+10:he.find("last_online")-3]
                                +"\n\n"+message.author_guid
                            )
                            seen.append(message.author_guid)
        await client.run_until_disconnected()
asyncio.run(main())

