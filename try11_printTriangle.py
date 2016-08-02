#Level_1 삼각형출력하기

def printTriangle(num):
    num = num+1
    s = "*\n"
    for i in range(2,num):
        s = s + (i*"*"+"\n")
    return s
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )

'''다른 사람 풀이
def printTriangle(num):
    s = ""
    #함수를 완성하세요
    for temp1 in range(num):
        for temp2 in range(temp1+1):
            s += "*"
        s += "\n"
    return s
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )
'''
