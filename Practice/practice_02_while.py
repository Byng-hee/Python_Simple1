# 문제1)  로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료!
# pw = 1234

# count = 0  #  틀린횟수
# while True:
#     input_pw = int(input("암호: "))
#     if count >= 3:
#         print("종료: 암호를 3회이상 틀리셨습니다.")
#         break
#     if pw == input_pw:
#         print("반갑습니다.")
#         break
#     else:
#         print("올바른 암호를 입력해주세요. ")
#         count += 1

# 문제2) 1~100까지 더해서 총합을 계산하세요.
# # - for문
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(f"1부터 100까지의합(for): {sum}이다.")
#
# # - while문
# i = 1
# sum1 = 0
# while i < 101:
#     sum1 += i
#     i += 1
#
# print(f"1부터 100까지의합(wihle): {sum1}이다.")


