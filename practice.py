# print(abs(-5))
# print(pow(4,2))
# print(max(5,12))
# print(min(5,12))
# print(round(3.14))
# print(round(3.99))

# from math import *
# print(floor(4.99))
# print(ceil(4.99))
# print(sqrt(16))

from operator import truediv
from random import *
# print(random())
# print(random()*10)
# print(int(random()*10))
# print(int(random()*10+1))
# print(int(random()*45+1))
# print(int(random()*45+1))
# print(int(random()*45+1))
# print(int(random()*45+1))
# print(int(random()*45+1))
# print(int(random()*45+1))

# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))

# print(randint(1,45))    # 포함

# 퀴즈
# month = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(month) + "일로 선정되었습니다.")

# jumin = "123412-1133444"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

# python = "Python is Amazing"

# print(python.upper())
# print(python.lower())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))

# index = python.index('n')
# print(index)
# index = python.index('n', index + 1)
# print(index)
# print(python.find('n'))

# print("hi")
# print(python.count('n'))

# print("나는 %d살입니다" %20)
# print("나는 %s살입니다" %20)
# print("나는 %c살입니다" %"2")

# print("나는 %s색과 %s색을 좋아해" %("빨간","노랑"))

# print("나는 {}살" .format(20))
# print("나는 {}색과 {}색을 좋아해" .format("빨간","파랑"))
# print("나는 {1}색과 {0}색을 좋아해" .format("빨간","파랑"))


# print("나는 {age}살이고 {color}을 좋아해" .format(age=20, color="빨강"))
# print("나는 {age}살이고 {color}을 좋아해" .format(color="빨강", age=20))

# 이 방법은 뒤에 format 안붙여도됨
# age = 20
# color = "red"
# print(f"나는 {age}살이고 {color}을 좋아해")

#------------------------------------------#
# \" , \' : 문장 내에서 따음표
# print("asasdasd\r\nasdasd")

# \\ : 문장 내에서 \

#------------------------------------------#
# quiz
# strS = "http://naver.com"
# strS1 = strS.replace("http://", "")
# idx = strS1.find('.')
# str2 = strS1[:idx]
# print("생성된 비밀번호 : " + str2[:3] + str(len(str2)) + str(strS1.count('e')) + "!")

#------------------------------------------#
# 리스트 - 순서를 가지는 객체
# sub1 = 10
# sub2 = 20
# sub3 = 30

# sub = [10,20,30]

# print(sub)
# print(sub.index(10))

# sub.append(40)
# print(sub)
# sub.insert(2, 100)
# print(sub)

# sub.pop()
# print(sub)

# sub.append(30)
# print(sub)
# print(sub.count(30))

# # sort
# sub.sort()
# print(sub)

# sub.reverse()
# print(sub)

# sub.clear()
# print(sub)

# # variable type
# arr = [1,2,3]
# mix = ["aaa", 20, True]
# print(mix)

# # list extend
# arr.extend(mix)
# print(arr)

#------------------------------------------#
# # dictionary
# cab = {3:"aaa", 4:"bbb"}
# print(cab)
# print(cab[3])   # error 시 종료
# print(cab.get(3)) # error 시 종료안됨

# print(cab.get(10, "Not"))

# print(3 in cab)
# print(5 in cab)

# cab2 = {"a-1":"aaa", "a-2":"bbb"}
# print(cab2)

# # add
# cab2["a-1"] = "ddd"
# cab2["a-3"] = "ccc"
# print(cab2)

# # del
# del cab2["a-2"]
# print(cab2)

# # key only 
# print(cab2.keys())
# # value only
# print(cab2.values())
# # all
# print(cab2.items())

# cab.clear()
# cab2.clear()

#------------------------------------------#

# # 튜플 - 속도가 list보다 빠름 (변경되지 않음)
# m = ("a","b")
# print(m[0])

#------------------------------------------#
# # 집합 (set)
# # 중복이 안되고 순서가 없음
# my_set = {100,101,102}
# print(my_set)

# set2 = set([100,200,300])

# # 교집합
# print(my_set & set2)
# print(my_set.intersection(set2))

# # 합집합
# print(my_set | set2)
# print(my_set.union(set2))

# # 차집합
# print(my_set - set2)
# print(my_set.difference(set2))
# set2.add(400)
# set2.remove(200)
# print(set2)

#------------------------------------------#
# 자료구조의 변경
# menu = {"coffe", "milk", "juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#------------------------------------------#
# quiz

# #### 내가 짠거 ####
# arr = range(1,21)
# li = list(arr)

# # print(li)

# rank1 = sample(li,1)
# set_list = set(li)
# rank1 = set(rank1)

# set_list = set_list - rank1
# set_list = list(set_list)

# rank2 = sample(set_list,3)


# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : " + str(rank1))
# print("커피 당첨자 : " + str(rank2))
# print("-- 축하합니다 --")


# #### 정답 ####
# users = range(1,21)
# users = list(users)
# shuffle(users)

# winner = sample(users, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winner[0]))
# print("커피 당첨자 : {0}".format(winner[1:]))
# print("-- 축하합니다 --")

#------------------------------------------#
# if

## 1
# weather = input("What ? ")
# if weather == "rain" or weather == "snow":
#     print("umbrella")
# elif weather == "sunny":
#     print("good")
# else:
#     print("not good")


## 2
# temp = int(input("how is temp?"))

# if(temp >= 30):
#     print("so hot")
# elif temp >= 10 and temp < 30:
#     print("good")
# elif 0 <= temp < 10:
#     print("cold")
# else:
#     print("die")

#------------------------------------------#
# for
## 1
# for wait in range(1,10):
#     print("No. {0}".format(wait))

## 2
# star = ["iron", "hulk", "thor"]

# for customer in star:
#     print("{0}, ready".format(customer))

#------------------------------------------#
# while
## 1
# customer = "thor"
# index = 5

# while index >= 1:
#     print("{0}!!, {0} remaning".format(customer) .format(index))
#     index -= 1
#     if index == 0:
#         print("Complete")

## 2
# customer = "iron"
# person = "unknown"
# while person != customer:
#     print("{0}!!, It's ready".format(customer))
#     person = input("what is your name? ")

#------------------------------------------#
# continue , break
## 1
# absent = [2,5]
# no_book = [7]
# for stu in range(1,11):
#     if stu in absent:
#         continue
#     elif stu in no_book:
#         break
#     print("{0}, hi" .format(stu))

# ## 2
# # 1 2 3 4 -> 101 102 103 104
# stu = [1,2,3,4,5]
# print(stu)
# stu = [i+100 for i in stu]
# print(stu)

# ## 3
# # name to length
# stu = ["aa","bbb","cccc","dqweqwd"]
# stu = [len(i) for i in stu]
# print(stu)

# ## 4
# # lower -> upper
# stu = ["aa","bbb","cccc","dqweqwd"]
# stu = [i.upper() for i in stu]
# print(stu)

#------------------------------------------#
# # quiz
# total = 0
# for son in range(1,51):
#     in_time = randint(5,51)
#     correct = ''
#     if 5 <= in_time <= 15:
#         correct = 'O'
#         total += 1
#     else:
#         correct = ''
#     print("[{0}] {1} 번째 손님 (소요시간 : {2}" .format(correct, son, in_time))

# print("총 탑승 승객 : {0}분" .format(total))

#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#