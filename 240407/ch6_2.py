# for waiting_no in [1, 2, 3, 4, 5] :
#   print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5):
#   print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):
#   print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6, 2):
#   print("대기번호 : {0}".format(waiting_no))

# orders = ["아이언맨", "토르", "스파이더맨"]
# for customer in orders:
#   print("{0} 님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer))

# customer = "토르"
# index = 5

# while index >= 1:
#   print("{} 님, 커피가 준비됐습니다.".format(customer))
#   index -= 1
#   print("{}번 남았어요.".format(index))
#   if index == 0:
#     print("커피가 폐기 처분됩니다.")

# while True:
#   print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
#   index += 1

# customer = "토르"
# person = None

# while person != customer:
#   print("{0} 님, 커피가 준비됐습니다.".format(customer))
#   person = input("이름이 어떻게 되세요!")

# absent = [2, 5]

# for student in range(1, 11):
#   if student in absent:
#     continue
#   print("{0}번 학생, 책을 읽어보세요.".format(student))

# absent = [2, 5]
# no_book = [7]

# for student in range(1, 11):
#   if student in absent:
#     continue
#   elif student in no_book:
#     print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
#     break
#   print("{0}번 학생, 책을 읽어 보세요.".format(student))

# students = [1, 2, 3, 4, 5]
# print(students)

# students = [i + 100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "Spider Man"]
# print(students)

# students = [len(i) for i in students]
# print(students)

students = ["Iron Man", "Thor", "Spider Man"]
print(students)

students = [i.upper() for i in students]
print(students)