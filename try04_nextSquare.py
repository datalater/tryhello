#Level_1 정수제곱근판별하기

def nextSqure(n):
    i = 1
    while True:
        if n == i**2:
            result =(i+1)**2
            break
        elif n < (i+1)**2:
            result = "no"
            break
        else:
            i+=1
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
