# 4가지 숫자로 만들 수 있는 가장 큰 시간을 출력해라
# 시계에 표시된 시간은 24시간 기준이다.
# 4가지 숫자를 조합해서 시간을 출력할 수 없는 경우에는 -1을 출력해라
res = ""
time = input()
time = [int(x) for x in time.split()]
time.sort(reverse = True)

def clock(time):
    res =""
    
    #첫번째 자리 시간 후보 : 2,1,0
    if min(time) >= 3:
        return "-1"
    myFilter = [x<3 for x in time]
    arr = [i for (i,v) in zip(time, myFilter) if v]
    v = max(arr)
    res+=str(v)
    time.remove(v)

    #print(res,time)

    # 첫번째가 2일때 두번째 자리 시간 후보 : 3,2,1,0
    if res =="2":
        if min(time)>=4:
            return "-1"
        myFilter =[x<4 for x in time]
        arr = [i for (i,v) in zip(time,myFilter) if v]
        v=max(arr)
        res+=str(v)
        time.remove(v)
    
    
    # 첫번째가 1 또는 0 일때 두번째 자리 시간 후보 : 9,8,7,6,5,4,3,2,1,0
    else:
        v=max(time)
        res+=str(v)
        time.remove(v)
    
    
    
    # 세번째 자리 시간 후보 : 5,4,3,2,1,0
    if min(time)>=6:
        return "-1"
    myFilter = [x<6 for x in time]
    arr = [i for (i,v) in zip(time,myFilter) if v]
    v = max(arr)
    res+=":"+str(v)
    time.remove(v)
  #  print(res,time)
    
    # 네번째 자리 시간 후보 : 9,8,7,6,5,4,3,2,1,0
    res+=str(time[0])

#    print(res,time)

    return res
    
    
print(clock(time))
