'''
문제 : 2016년
2016년 1월 1일은 금요일이다. 
2016년 a월 b일은 무슨 요일일까?
단, 2016년은 윤년이다.
'''

def solution(a, b):
    answer = ''
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    days=[31,29,31,30,31,30,31,31,30,31,30,31] #JAN,FEB,MAR, ...
    
    day_sum=0
    for i in range(a-1):
        day_sum+=days[i]
    day_sum+=b
    answer = day[day_sum%7-1]
    return answer