price = 1000
goods = 3
total = 0

for i in range(1, goods + 1):
  print("2+1 상품입니다.")
  if i % 3 == 0:
    continue
  total += price

print("총 가격은 " + str(total) + "원 입니다.")