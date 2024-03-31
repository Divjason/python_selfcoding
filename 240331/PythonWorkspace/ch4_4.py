print("ab" + "ab")
print("ab", "ab")

# 서식지정자
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살 입니다." % 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# format()함수
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# f-문자열
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

apple = "사과"
banana = "바나나"

print("빨가면 {} 맛있으면 {}".format(apple, banana))
print("빨가면", apple, "맛있으면", banana)
print("빨가면 {1} 맛있으면 {0}".format(banana, apple))
print(f"빨가면 apple 맛있으면 banana")