a = list(input())
dic = {char:0 for char in a} # 기준
b = list(input()) # 정렬할 문자열

output = ""
for c in b:
    if c in dic.keys():
        dic[c]+=1
    else:
        output+=c

front = ""
for c in a:
    front+=c*dic[c]
print(front+output)