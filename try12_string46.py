#Level_1 문자열 다루기 기본

def alpha_string46(s):
    if len(s)==4 or len(s)==6:
        while True:
            try:
                int(s)
                s = True
                break
            except ValueError:
                s = False
                break
    else:
        s = False
    return s
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )

'''다른 사람 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in [4, 6]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )

'''
