# 첫번째로 말하는 숫자 : 답의 자리수
# 두번째로 말하는 숫자 : 자릿수 간의 차이
# ex. 2 5 -> 16 27 38 49 50 61 72 83 94
# 3 3 -> 141 252 363 474 585 696 747 858 969
# 단) 0으로 시작하는 숫자는 없다.

digit = int(input())
dif = int(input())

results = []
def mk(cur, length):

    if digit<2 or digit>9 :
        return -1
    if dif<0 or dif>10:
        return -1

    if length<digit:
        if int(cur[-1])-dif >=0:
            mk(cur+str(int(cur[-1])-dif), length+1)
        if int(cur[-1])+dif<10:
            mk(cur+str(int(cur[-1])+dif), length+1)
    else:
        results.append(cur)
        #print(cur, end=" ")
        
for i in range(1,10):
    mk(str(i),1)

results = [int(x) for x in list(set(results))]

results = sorted(results)

#print(results)
for r in results:
    print(r, end=" ")