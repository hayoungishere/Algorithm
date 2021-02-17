ori = input()
erase = input()

#print(ori.replace(erase,""))

while erase in ori:
    ori = ori.replace(erase,"")


print(ori)