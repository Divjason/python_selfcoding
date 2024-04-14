# glasses = 10

# def rent(people) :
#   glasses = glasses - people
#   print("[함수내부] 남은 3D 안경 개수 : {0}".format(glasses))

# print("전체 3D 안경 개수: {0}".format(glasses))
# rent(2)
# # print("남은 3D 안경 개수: {0}".format(glasses))

# glasses = 10

# def rent(people) :
#   global glasses
#   glasses = glasses - people
#   print("[함수내부] 남은 3D 안경 개수 : {0}".format(glasses))

# print("전체 3D 안경 개수 : {0}".format(glasses))
# rent(2)
# print("전체 3D 안경 개수 : {0}".format(glasses))

glasses = 10
def rent_return(glasses, people) :
  glasses = glasses - people
  print("[함수내부] 남은 3D 안경 개수:{0}".format(glasses))
  return glasses
print("전체 3D 안경 개수 : {0}".format(glasses))
glasses = rent_return(glasses, 2)
print("전체 3D 안경 개수 : {0}".format(glasses))