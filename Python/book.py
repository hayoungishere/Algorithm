bookNumber = input()
bookName = input() # first and last character
num = input() # 1<= num <=100

for i in range(int(num)):
    info = input().split()
    #print(info)
    
    if info[0] != bookNumber:
        print("False")
        continue
    if info[1][0]+"*"+info[1][-1] != bookName:
        print("False")
    else:
        print("True")