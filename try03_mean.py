#Level 1 평균구하기

def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    count = len(list)
    sum = 0
    for e in range(count):
        sum += (list[e])
    return sum/count

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
