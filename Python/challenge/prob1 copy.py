
'''
Code Challenge
'''


def solution(n, record):
    answer = []
    server =[['' for j in range(1)] for i in range(n)]
    print(server)

    for item in record:
        print(item.split())
        s, ni = item.split()
        if ni not in server[int(s)-1] :
            server[int(s)-1].append(ni)
        if len(server[int(s)-1]) > 5:
            server[int(s)-1] = server[int(s)-1][1:]
        
    print(server)
    for s in server:
        for c in s:
            if c != '':
                answer.append(c)
    return answer


if __name__ == "__main__":
    print(solution(1,["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"]))
    print(solution(4, ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]))