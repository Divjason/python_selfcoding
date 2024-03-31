# random 모듈 추가
from random import *

# lst = [1, 2, 3, 4, 5]
# print(lst)

# shuffle(lst)
# print(lst)

# print(sample(lst, 1))

users = range(1, 21) #리스트 생성, 1부터 21직전(20)까지 연속한 숫자 모음
users = list(users) #users를 리스트 자료구조로 변환
shuffle(users) #리스트 섞기

winners = sample(users, 4) #users 리스트레서 중복없이 4명 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) #0번째 인덱스(1명)
print("커피 당첨자 : {0}".format(winners[1:])) #1번째부터 마지막까지 슬라이싱(3명)
print("-- 축하합니다! --")
