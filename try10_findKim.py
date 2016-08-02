#Level_1 서울에서김서방찾기

def findKim(seoul):
    kimIdx = 0
    # 함수를 완성하세요
    for kimIdx in range(len(seoul)):
        if seoul[kimIdx] == "Kim":
            return "김서방은 {}에 있다".format(kimIdx)


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))

'''다른사람의 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))
'''
