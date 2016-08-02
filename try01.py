#Level 1 x만큼 간격이 있는 n개의 숫자

def number_generator(x, n):
    # 함수를 완성하세요
    a = [x]
    for i in range(2, n+1):
        a.append(i*x)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))
