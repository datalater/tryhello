#Level_1 문자열 내 마음대로 정렬하기

def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )

'''다른 사람 풀이 (1)
#dictionary 활용
def strange_sort(strings, n):
    strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요
    dic = {}
    ret = []
    for string in strings:
        dic[string[n]] = string
    for key in sorted(dic):
        #print(key, dic[key])
        ret.append(dic[key])
    return ret

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
'''

'''다른 사람 풀이 (2)
#lambda 활용법 (설명: http://stackoverflow.com/questions/13669252/what-is-key-lambda)
def strange_sort(strings, n):
    
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))
'''
