# 조건문(condition): if~elif~else
# - 특정조건을 만족하는 경우 수행할 작업에 사용
# - 모든 조건은 boolean 으로 표현 됨
# - 조건문의 경우 if, elif, else 블록 내 들여쓰기
# - 모든 블록문의 시작점의 마지막 : (콜론, colon) 추가

#JAVA & C                                      Python
# if (조건물1) {                               if 조건물1:
#   code                                            code
#} else if(조건문2) {                          elif 조건문2:
# code                                              code
#} else if(조건문3) {                          elif 조건문3:
# code                                              code
#} else{                                       else:
# code                                              code
#}

#Python은 조건문에서 ":"로 시작해서 블록에 들여쓰기가 끝날때 끝 블록문은 들여쓰기가 필수

# if 조건문1:
#   code
# if 조건문2:
#   code
# if 조건문3:
#   code

#if문을 활용한 조합식 ( 4 가지 )
# 1.if
# 2.if~else
# 3.if~elif~elif
# 4.if~elif~else

#논리 연산자(AND, OR, NOT)

# 1. AND
# 조건1   조건2  결과
#   F  and  F      F
#   T  and  F      F
#   F  and  T      F
#   T  and  T      T
# 2. OR
# 조건1   조건2  결과
#   F  and  F      F
#   T  and  F      T
#   F  and  T      T
#   T  and  T      T
# 1.NOT
#   F -> F
#   T -> F

# A, B, C, D, F로 계산하는 프로그램
# 4.1~4.5 : A
# 3.6~4.0 : B
# 3.1~3.5 : C
# 2.6~3.0 : D
# 2.4 이하 : F
score = 4.2  # 총학점 0.0~4.5
if score >= 4.1:
    print("A")
elif score >=3.6:
    print("B")
elif score >=3.1:
    print("C")
elif score >=2.6:
    print("D")
else:
    print("F")

print("*"*100)

if 4.5 >= score >= 4.1:
    print("A")
elif 4.0 >= score >=3.6:
    print("B")
elif 3.5 >= score >=3.1:
    print("C")
elif 3.0 >= score >=2.6:
    print("D")
else:
    print("F")
print("="*100)
# (초등학생, 중학생, 고등학생, 대학생, 학생x) 판별

# input() : 키보드로 값을 입력
born = input("태어난 년도: ")    # String type 으로 입력됨
print(born)

from datetime import datetime
now = datetime.today().year
print(now)
age = now - int(born)+1   # 2023 - 2004 + 1
print(age)

if 26>= age >= 20:
    print("대학생")
elif 19>= age >= 17:
    print("고등학생")
elif 16>= age >= 14:
    print("중학생")
elif 13>= age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")