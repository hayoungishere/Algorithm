dict = {"*-**":"ㄱ",
"**-*":"ㄴ",
"-***":"ㄷ",
"***-":"ㄹ",
"--":"ㅁ",
"*--":"ㅂ",
"--*":"ㅅ",
"-*-":"ㅇ",
"*--*":"ㅈ",
"-*-*":"ㅊ",
"-**-":"ㅋ",
"--**":"ㅌ",
"---":"ㅍ",
"*---":"ㅎ",
"*":"ㅏ",
"**":"ㅑ",
"-":"ㅓ",
"***":"ㅕ",
"*-":"ㅗ",
"-*":"ㅛ",
"****":"ㅜ",
"*-*":"ㅠ",
"-**":"ㅡ",
"**-":"ㅣ",
"--*-":"ㅐ",
"-*--":"ㅔ",
"*****-":"ㅖ",
"****-":"ㅒ",
}


def mos():
    inp = input()
    res = ""
    line = inp.split(" ")
    #print(line)
    for i in line:
        res +=dict[i]+" "
    return res.strip()

print(mos())