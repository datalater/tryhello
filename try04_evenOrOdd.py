#Level1 짝수와홀수

def evenOrOdd(num):
    s=""
    if num%2==0:
      s = "Even"
    else:
      s = "Odd"
    return s
#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
