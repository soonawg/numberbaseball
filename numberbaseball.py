#숫자야구
#인덱싱?
#스트라이크 : 자리와 숫자 동일
#볼 : 숫자만 동일
#아웃 : 아무것도 동일하지 않음
#랜덤 숫자 4개 뽑기
#랜덤 숫자 배정하기
#랜덤 배정받은 숫자 4개 중복체크
#입력 후 비교

import random

print("숫자 야구 게임에 오신 것을 환영합니다.")

correct_number = ["0", "0", "0", "0"] #정답 수 조합 (컴퓨터)를 리스트로 만들기
correct_number[0] = str(random.randrange(0, 10, 1)) #각 수자를 랜덤으로 지정 (랜덤 모듈 사용 / 0~9)
correct_number[1] = str(random.randrange(0, 10, 1))
correct_number[2] = str(random.randrange(0, 10, 1))
correct_number[3] = str(random.randrange(0, 10, 1))

#랜덤 숫자가 같다면 계속 반복 (예 : 1자리수 2자리수가 같으면 다시 지정)
while(correct_number[0] == correct_number[1]):
    correct_number[1] = str(random.randrange(0, 10, 1))

while(correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
    correct_number[2] = str(random.randrange(0, 10, 1))

while(correct_number[0] == correct_number[3] or correct_number[1] == correct_number[3] or correct_number[2] == correct_number[3]):
    correct_number[3] = str(random.randrange(0, 10, 1))

try_number = 0
strike_number = 0
ball_number = 0

print("숫자야구를 시작합니다.")
print("-------------------------------")

print(correct_number)

while (strike_number < 4):

    number = str(input("숫자 4자리를 입력해주세요 : "))

    strike_number = 0
    ball_number = 0

    for i in range(0, 4): # i 값의 범위 0 ~ 3
        for j in range(0, 4):
            if (number[i] == str(correct_number[j]) and i == j):
                strike_number += 1
            elif(number[i] == str(correct_number[j]) and i != j):
                ball_number += 1
    print(f"결과: {strike_number}스트라이크 {ball_number}볼")
    try_number += 1

print("----------------------------")
print("축하합니다! 정답입니다")
print(f"{try_number}번 만에 맞추었습니다.")
print(correct_number)
