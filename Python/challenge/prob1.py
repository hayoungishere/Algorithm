
'''
서버 n개가 있는 온라인 RPG 게임을 이용하는 한 유저가 각 서버에 새 캐릭터를 생성하려한다. 캐릭터 생성 규칙은 다음과 같다.

1. 각 서버에는 1 부터 n까지 번호가 하나씩 붙어있다.
2. 서버별로 캐릭터는 최대 5개까지 생성 가능하다.
3. 캐릭터가 이미 5개인 서버에 새 캐릭터를 생성하면, 해당 서버에서 가장 오래된 캐릭터 하나를 삭제하고 빈자리에 캐릭터가 생성된다.
4. 해당 서버에 이미 같은 닉네임이 있는 경우 캐릭터가 생성되지 않는다.
    4-1. 서로 다른 서버에는 닉네임이 같은 캐릭터를 만들 수 있다.

단, 다른 유저가 생성한 캐릭터들의 닉네임은 고려하지 않는다고 가정한다.

서버개수n, 유저가 새 캐릭터를 생성한 기록이 담긴 배열 record가 매개변수로 주어진다. 이때, 각 서버별로 어떤 캐릭터들이 생성됐는지 닉네임을 문자열 배열 형태로 return 하도록 solution 함수를 완성해라.

[제한사항]
* n은 1이상 9이하인 자연수이다.
* record는 캐릭터의 생성 기록이 시간 순서대로 담긴 문자열 배열이다.
* record의 길이(=캐릭터 생성 기록 개수)는 1이상 1,000 이하이다.
* record의 각 원소는 캐릭터 생성 기록을 나타낸다.
    * 캐릭터 생성 기록은 "N nickanme"형태이다.
    * N은 서버 번호를 나타내며 n(서버 개수) 이하인 한 자리 자연주이다.
    * nickname은 해당 서버에 생성한 캐릭터의 닉네임을 나타낸다.
    * N과 nickname은 공백(스페이스) 하나로 구분되어 있다.
    * 닉네임의 길이는 1이상 6 이하이며 알파벳 소문자로만 이루어져있다.
* return 하는 문자열 배열은 서버별 닉네임을 다음 기준에 따라 정렬해 return 해주세요.
    * 번호가 더 작은 서버에 있는 닉네임은 더 앞에 온다.
    * 서버 번호가 같을 경우 해당 서버에서 더 오래된 닉네임이 더 앞에 온다.
    * 캐릭터가 하나도 생성되지 않은 서버는 무시해도 된다.
    

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