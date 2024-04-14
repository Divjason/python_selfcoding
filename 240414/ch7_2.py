def open_account() :
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money) :
    print("{0}원을 입금했습니다. 잔액은 {1}원 입니다.".format(money, balance + money))
    return balance + money

def withdraw_night(balance, money) :
    commission = 100
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)

# 업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# 튜플 예제
(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)