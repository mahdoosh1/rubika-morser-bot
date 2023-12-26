import asyncio

e_to_m = {
"a":"·—",
"b":"—···",
"c":"—·—·",
"d":"—··",
"e":"·",
"f":"··—·",
"g":"——·",
"h":"····",
"i":"··",
"j":"·———",
"k":"—·—",
"l":"·—··",
"m":"——",
"n":"—·",
"o":"———",
"p":"·——·",
"q":"——·—",
"r":"·—·",
"s":"···",
"t":"—",
"u":"··—",
"w":"·——",
"x":"—··—",
"y":"—·——",
"z":"——··"
}
m_to_e = {
".-":"a",
"-...":"b",
"-.-.":"c",
"-..":"d",
".":"e",
"..-.":"f",
"--.":"g",
"....":"h",
"..":"i",
".---":"j",
"-.-":"k",
".-..":"l",
"--":"m",
"-.":"n",
"---":"o",
".--.":"p",
"--.-":"q",
".-.":"r",
"...":"s",
"-":"t",
"..-":"u",
".--":"w",
"-..-":"x",
"-.--":"y",
"--..":"z"
}


async def decode(morse):
    global m_to_e
    out = ""
    morse = morse.replace("—","-")
    morse = morse.replace("·",".")
    words = morse.split("/")
    for word in words:
        letters = word.replace('\xa0',' ').split("  ")
        for letter in letters:
            letter2 = letter.replace(' ','')
            try:
                out = out + m_to_e[letter2]
            except:
                out = out + "?"
        out = out + " "
    return out

async def encode(text):
    global e_to_m
    out = ""
    words = text.split(" ")
    for word in words:
        for letter in word:
            try:
                out = out + e_to_m[letter] + "   "
            except:
                out = out + "?  "
        out = out[:len(out)-3] + "/"
    return out[:len(out)-1]

if __name__ == "__main__":
    run = True
    while run:
        inp = input()
        if inp.startswith('enc'):
            print(asyncio.run(encode(inp[4:])))
        elif inp.startswith('dec'):
            print(asyncio.run(decode(inp[4:])))
        elif inp != "exit":
            print('Invalid command')
        else:
            run = False
