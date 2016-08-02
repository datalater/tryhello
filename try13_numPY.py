#Level_1 문자열 내 p와 y의 개수

def numPY(s):
    sort = s.lower()
    if sort.count("p") != sort.count("y"):
        return False
    else:
        return True

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )

'''다른 사람 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
'''
    
