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

# from curses.ascii import isalnum, isdigit
# from logging.config import valid_ident
# from operator import truediv
# from random import *
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
# # function
# ## 1
# def open_acc():
#     print("making Account")

# open_acc()

# def deposit(bal, money):
#     print("Complete. Balance is {0}".format(bal+money))
#     return bal+money

# def withdraw(bal,money):
#     if bal > money:
#         print("Withdrwa is complete. Balance is {0}".format(bal - money))
#         return bal - money
#     else:
#         print("Withdraw is failed. Balance is {0}".format(bal))
#         return bal

# def withdraw_night(bal, money):
#     comm = 100
#     return comm, bal - money - comm

# bal = 0
# bal = deposit(bal,5000)
# bal = deposit(bal,15000)

# bal = withdraw(bal, 50000)
# bal = withdraw(bal, 5000)

# comm, bal = withdraw_night(bal, 3000)
# print("commition is {0} and Balance is {1}".format(comm, bal))

# ## 2 가변인자
# def test(name, age, lang1, lang2, lang3):
#     print(name, age, end =" ")  # end는 줄바꿈 전에
#     print(lang1, lang2, lang3)

# test("abc",20,"java","c","go")

# def test2(name, age, *lang):
#     print(name, age, end =" ")  # end는 줄바꿈 전에
#     for lang in lang:
#         print(lang, end = " ")
#     print()
# test2("abc",20,"java","c","go","C++")

# ## 3 지역변수 / 전역변수
# gun = 10

# def check(sol):
#     global gun
#     gun = gun - sol
#     print("Remaining Gun : {0}".format(gun))

# check(5)

# def check_ret(gun,sol):
#     gun = gun - sol
#     print("Remaining Gun : {0}".format(gun))
#     #return gun

# check_ret(gun,3)
# print("Remaining Gun : {0}".format(gun))

#------------------------------------------#
# quiz

# std = 0

# def std_weight(height, gender):
#     global std
#     if gender == "mail":
#         std = float(height*0.01) * float(height*0.01) * 22
#     elif gender == "femail":
#         std = float(height*0.01) * float(height*0.01) * 21
#     else:
#         print("Wrong Gender")
#     print("{}cm {}'s standard weight is {}".format(height,gender, round(std,2)))

# std_weight(184,"mail")
# std_weight(168,"femail")

#------------------------------------------#
## Standard In/Out
# # 1
# import sys
# print("aa","bb", sep=",",end="?")   # sep = 구분자 (, 로 구분되는 부분을 치환), end = 문장의 끝 부분을 치환 (\r)
# print("hahaha")

# print("aa","bb", file=sys.stdout)
# print("aa","bb", file=sys.stderr)

# # 2 - just
# score = {"math":0, "eng":50, "coding":100}

# for sub, score in score.items():
#     #print(sub, score)
#     print(sub.ljust(10), str(score).rjust(4))

# # 3 - zfill
# for num in range(1,21):
#     print("No : " + str(num).zfill(3))

# # 4 - input - 항상 문자열임
# ans = input("Any Num : ")
# print(ans)

# # 5 - 다양한 출력 포맷
# # 빈자리 빈공간, 오른쪽 정렬, 총 10자리 공간
# print("{0: >10}".format(500))
# # 양수, 음수 구분
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬, 빈칸으로 _ 채움
# print("{0:_<+10}".format(500))
# # 세 자리 마다 콤마
# print("{0:,}".format(1234567890))
# # 세 자리 마다 콤마, 부호 표시
# print("{0:+,}".format(1234567890))
# # 세 자리 마다 콤마, 부호 표시, 자리수 확보, 빈자리 채움
# print("{0:^<+30,}".format(1234567890))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지 출력
# print("{0:.2f}".format(5/3))

#------------------------------------------#
# file in/out
# # 1
# score = open("score.txt","w",encoding="utf8")
# print("test 1", file=score)
# print("test 2", file=score)
# score.close()

# # 2
# score = open("score.txt","a", encoding="utf8")
# score.write("text3")
# score.write("\ntext4")
# score.close()

# # 3
# score = open("score.txt","r",encoding="utf8")
# print(score.read())
# score.close()

# # 4
# score = open("score.txt", "r", encoding="utf8")
# print(score.readline(), end="") ## 줄별로 읽기, 커서 다음줄 이동
# print(score.readline(), end="")
# print(score.readline(), end="")
# print(score.readline(), end="")
# score.close()

# # 5
# score = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score.readline()
#     if not line:
#         break
#     print(line, end="")
# score.close()

# # 6
# score = open("score.txt", "r", encoding="utf8")
# lines= score.readlines()
# for line in lines:
#     print(line, end="")
# score.close()

#------------------------------------------#
# Pickle - 데이터를 파일 형태로 저장

import pickle

# # 1
# profile_file = open("profile.pic","wb")
# profile = {"name":"lee","age":"33","hobby":["a","b","c"]}
# print(profile)
# pickle.dump(profile,profile_file)   # profile에 있는 정보를 file에 저장
# profile_file.close()

# # 2
# profile_file = open("profile.pic","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#------------------------------------------#
# with - close 안해도됨
# # 1
# with open("profile.pic","rb") as profile_file:
#     print(pickle.load(profile_file))

# # 2 - with를 이용해 입출력
# with open("st.txt","w",encoding="utf8") as st_file:
#     st_file.write("test123")

# with open("st.txt","r",encoding="utf8") as st_file:
#     print(st_file.read())

#------------------------------------------#
# # Quiz

# week = 1
# for week in range(1,51):
#     file_name = str(week) + "Week.txt"
#     with open(file_name, "w", encoding="utf8") as file:
#         file.write("- {0} Weekly -\n".format(week))
#         file.write("Department : \n")
#         file.write("name : \n")
#         file.write("summary : ")

# for week in range(1,51):
#     file_name = str(week) + "Week.txt"
#     with open(file_name, "r", encoding="utf8") as file:
#         print(file.read())

#------------------------------------------#
# @@@ class
# # 1
# class unit: # Normal Unit
#     def __init__(self,name,hp,dam): # 생성자
#         self.name = name
#         self.hp = hp
#         self.dam = dam
#         print("{0} Unit is Created !".format(self.name))
#         print("hp {0}, Attack Damage {1}".format(self.hp, self.dam))

# marine = unit("Marine",40,5)
# tank = unit("Tank",150,35)

# wraith1 = unit("Wraith", 80, 5)
# print("name : {0}, Attack Damage : {1}".format(wraith1.name, wraith1.dam))

# 변수를 외부에서 만들어 쓸수있음
# wraith2 = unit("Wraith", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} is clocking".format(wraith2.name))

# class AttackUnit:
#     def __init__(self,name,hp,dam): # 생성자
#         self.name = name
#         self.hp = hp
#         self.dam = dam

#     def attack(self, location):
#         print("{0} : Attack at {1} [Power {2}]".format(self.name,location,self.dam))

#     def damaged(self,damage):
#         print("{0} : {1} get damaged".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : current hp is {1}".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# fire1 = AttackUnit("Firebat", 50, 16)
# fire1.attack("5")

# fire1.damaged(25)
# fire1.damaged(25)

# # 2 - 상속
# class Unit:     # Normal Unit
#     def __init__(self,name,hp): # 생성자
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self,name,hp,dam): # 생성자
#         Unit.__init__(self,name,hp)
#         self.dam = dam

#     def attack(self, location):
#         print("{0} : Attack at {1} [Power {2}]".format(self.name,location,self.dam))

#     def damaged(self,damage):
#         print("{0} : {1} get damaged".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : current hp is {1}".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# fire1 = AttackUnit("Firebat", 50, 16)
# fire1.attack("5")

# fire1.damaged(25)
# fire1.damaged(25)

# # 3 - 다중 상속
# class Unit:     # Normal Unit
#     def __init__(self,name,hp): # 생성자
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self,name,hp,dam): # 생성자
#         Unit.__init__(self,name,hp)
#         self.dam = dam

#     def attack(self, location):
#         print("{0} : Attack at {1} [Power {2}]".format(self.name,location,self.dam))

#     def damaged(self,damage):
#         print("{0} : {1} get damaged".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : current hp is {1}".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# class Flyable:
#     def __init__(self, speed):
#         self.speed = speed
#     def fly(self,name,location):
#         print("{0} : Fly at {1}. [Speed : {2}]".format(name, location, self.speed))

# class FlyAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, speed):
#         AttackUnit.__init__(self,name,hp,damage)
#         Flyable.__init__(self,speed)

# val = FlyAttackUnit("Valkyrie",200,6,5)
# val.fly(val.name,"1")

# # 4 - 메소드 오버라이딩
# class Unit:     # Normal Unit
#     def __init__(self,name,hp, speed): # 생성자
#         self.name = name
#         self.hp = hp
#         self.speed = speed
        
#     def move(self,location):
#         print("Unit is Moving")
#         print("{0} : Move at {1} location. [Speed : {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self,name,hp,speed, dam): # 생성자
#         Unit.__init__(self,name,hp, speed)
#         self.dam = dam

#     def attack(self, location):
#         print("{0} : Attack at {1} [Power {2}]".format(self.name,location,self.dam))

#     def damaged(self,damage):
#         print("{0} : {1} get damaged".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : current hp is {1}".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# class Flyable:
#     def __init__(self, speed):
#         self.speed = speed
#     def fly(self,name,location):
#         print("{0} : Fly at {1} location. [Speed : {2}]".format(name, location, self.speed))

# class FlyAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, speed):
#         AttackUnit.__init__(self,name,hp,0,damage)
#         Flyable.__init__(self,speed)

#     def move(self, location):
#         print("Fly Unit Moving")
#         self.fly(self.name,location)

# vul = AttackUnit("Vulture", 80, 10, 20)
# battle = FlyAttackUnit("Battle Cruiser", 500, 25, 3)

# vul.move("5")
# #battle.fly(battle.name, "9")
# battle.move("9")

# # 5 - PASS
# def game_start():
#     print("Start Game")
# def game_over():
#     pass        # 완성된것 처럼 보임

# game_start()
# game_over()

# # 6 - Super - practice_class.py 참조
# class Unit:     # Normal Unit
#     def __init__(self,name,hp, speed): # 생성자
#         self.name = name
#         self.hp = hp
#         self.speed = speed
        
#     def move(self,location):
#         print("Unit is Moving")
#         print("{0} : Move at {1} location. [Speed : {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self,name,hp,speed, dam): # 생성자
#         Unit.__init__(self,name,hp, speed)
#         self.dam = dam

#     def attack(self, location):
#         print("{0} : Attack at {1} [Power {2}]".format(self.name,location,self.dam))

#     def damaged(self,damage):
#         print("{0} : {1} get damaged".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : current hp is {1}".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# class Flyable:
#     def __init__(self, speed):
#         self.speed = speed
#     def fly(self,name,location):
#         print("{0} : Fly at {1} location. [Speed : {2}]".format(name, location, self.speed))

# class FlyAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, speed):
#         AttackUnit.__init__(self,name,hp,0,damage)
#         Flyable.__init__(self,speed)

#     def move(self, location):
#         print("Fly Unit Moving")
#         self.fly(self.name,location)

# class buildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)
#         self.location = location


# # 8 - Project
# class Unit:     # Normal Unit
#     def __init__(self,name,hp, speed): # 생성자
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} Unit Create complete".format(self.name))
        
#     def move(self,location):
#         print("Unit is Moving")
#         print("{0} : Move at {1} location. [Speed : {2}]".format(self.name, location, self.speed))

#     def damaged(self,damage):
#         print("{0} : {1} get damaged".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : current hp is {1}".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} is dead".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self,name,hp,speed, dam): # 생성자
#         Unit.__init__(self,name,hp, speed)
#         self.dam = dam
#     def attack(self, location):
#         print("{0} : Attack at {1} [Power {2}]".format(self.name,location,self.dam))

# class Flyable:
#     def __init__(self, speed):
#         self.speed = speed
#     def fly(self,name,location):
#         print("{0} : Fly at {1} location. [Speed : {2}]".format(name, location, self.speed))

# class FlyAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, speed):
#         AttackUnit.__init__(self,name,hp,0,damage)
#         Flyable.__init__(self,speed)
#     def move(self, location):
#         print("Fly Unit Moving")
#         self.fly(self.name,location)

# class marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,"Marine", 40, 1, 5)
#     def steampack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : Use Steampack (hp is decreased)".format(self.name))
#         else:
#             print("{0} : lack of hp".format(self.name))

# class tank(AttackUnit):
#     seize_developed = False
#     def __init__(self):
#         AttackUnit.__init__(self,"Tank",150,1,35)
#         self.seize_mode = False
#     def setSeize(self):
#         if tank.seize_developed == False:
#             return
#         if self.seize_mode == False:
#             self.seize_mode = True
#             self.dam *= 2
#             print("{0} : Switch to seize mode")
#         else:
#             self.seize_mode = False
#             self.dam /= 2
#             print("{0} : Turns seize Mode off")

# class wraith(FlyAttackUnit):
#     def __init__(self):
#         FlyAttackUnit.__init__(self,"Wraith",80,20,5)
#         self.clock_state = False
#     def clocking(self):
#         if self.clock_state:
#             print("{} : Clocking mode release".format(self.name))
#             self.clock_state = False
#         else:
#             print("{} : Clocking mode on".format(self.name))
#             self.clock_state = True

# def game_start():
#     print("Game Start")
# def game_over():
#     print("GG")

# game_start()

# m1 = marine()
# m2 = marine()
# m3 = marine()
# t1 = tank()
# t2 = tank()
# w1 = wraith()

# unit_list = []
# unit_list.append(m1)
# unit_list.append(m2)
# unit_list.append(m3)
# unit_list.append(t1)
# unit_list.append(t2)
# unit_list.append(w1)

# for unit in unit_list:
#     unit.move("1")

# tank.seize_developed = True

# for unit in unit_list:
#     if isinstance(unit, marine):
#         unit.steampack()
#     elif isinstance(unit, tank):
#         unit.setSeize()
#     elif isinstance(unit, wraith):
#         unit.clocking()

# for unit in unit_list:
#     unit.attack("1")

# for unit in unit_list:
#     unit.damaged(randint(5,21))

# game_over()

#------------------------------------------#
# # Quiz - Class
# class house:
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     def show(self):
#         #print(self.location + " " + self.house_type + " " + self.deal_type + " " + self.price + " " + self.completion_year)
#         print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)

# house1 = house("Seoul","APT","Lease","500 million","2024")
# house2 = house("Incheon","APT","Buy","300 million","Indefinitely")
# house3 = house("Busan","OP","Lease","200 million","2023")

# house_list = []
# house_list.append(house1)
# house_list.append(house2)
# house_list.append(house3)

# print("Total {0} For Sale".format(len(house_list)))

# for ho in house_list:
#     ho.show()

#------------------------------------------#
# Exception
#------------------------------------------#
# # 1
# try:
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자 : ")))
#     nums.append(int(input("두 번째 숫자 : ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError as err:
#     print(err)
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)

# # 2 - 의도적 error 발생
# try:
#     print("한 자리 숫자 나누기")
#     num1 = int(input("first : "))
#     num2 = int(input("second : "))

#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("err")

# # 3 - 사용자 정의 에러 처리
# class bigNumErr(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기")
#     num1 = int(input("first : "))
#     num2 = int(input("second : "))

#     if num1 >= 10 or num2 >= 10:
#         raise bigNumErr("Class Exception")
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("err")
# except bigNumErr as err:
#     print(err)

# # 4 - Finally (무조건 실행)
# class bigNumErr(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기")
#     num1 = int(input("first : "))
#     num2 = int(input("second : "))

#     if num1 >= 10 or num2 >= 10:
#         raise bigNumErr("Class Exception")
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("err")
# except bigNumErr as err:
#     print(err)
# finally:
#     print("test")

#------------------------------------------#
# # Quiz - Exception
# class SoldoutErr(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# max_order = 10
# waiting = 1

# while(True):
#     try:
#         print("남은 치킨 : {0}".format(max_order))
#         order = int(input("how many? : "))
#         if order < 1:
#             raise ValueError
#         elif order > max_order:
#             print("남은 치킨이 부족합니다")
#         else:
#             print("대기번호 {0} : {1} 마리 주문 완료".format(waiting,order))
#             waiting += 1
#             max_order -= order

#         if max_order == 0:
#             #raise Sold5outErr
#             raise SoldoutErr("장사 종료")
            
#     except ValueError as err:
#         print(err)
#     except SoldoutErr as err:
#         print(err)
#         break
#     except Exception as err:
#         print(err)


#------------------------------------------#
# Module - 부품처럼 잘 만들어진 파일
#------------------------------------------#
# # 1
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_army(5)

# # 2
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_army(5)

# # 3
# from theater_module import *
# price(3)
# price_morning(4)
# price_army(5)

# # 4
# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# # 5
# from theater_module import price_army as price
# price(3)

# # 6 - package
# # import는 모듈이나 패키지만 가능
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # 7
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# # 8 - __all__
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to2 = thailand.ThailandPackage()
# trip_to2.detail()

# # 9 - 위치 확인 - lib 폴더 아래에 두면 어느 프로젝트던 사용 가능
# from travel import *
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# # 10 - pip install (pypi search)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 11 - 내장 함수
# lan = input("무슨 언어를 좋아해?")
# print("{0}은 아주 좋은 언어야".format(lan))

#dir - 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "aaa"
# print(dir(name))

# google search - list of python builtins (내장함수 정보)

# 12 - 외장 함수 (직접 import) (list of python modules)
# # - glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다")

# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(100)
print(today + td)

#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#