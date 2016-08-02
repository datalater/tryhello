#Level1 제일 작은 수 제거하기

def rm_small(my_list):
    sort_list = list(my_list)
    sort_list.sort()
    for i in range(len(my_list)):
        if my_list[i]==sort_list[0]:
            del my_list[i]
            break
    return my_list
# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))

