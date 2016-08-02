#Level_1 수박수박수박수박수박수?

def water_melon(n):
    l = n//2 #몫
    k = n%2 #나머지
    return "수박"*l+"수"*k


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

