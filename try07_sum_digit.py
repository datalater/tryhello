#Level1 자릿수더하기


def sum_digit(number):
    str_digit = str(number)
    result = 0
    for i in range(len(str_digit)):
        result += int(str_digit[i])

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
