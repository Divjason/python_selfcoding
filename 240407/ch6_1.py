# weather = "비"

# if weather == "비":
#     print("우산을 챙기세요!")

# weather = "미세먼지"

# if weather == "비":
#   print("우산을 챙기세요.")
# elif weather == "미세먼지":
#   print("마스크를 챙기세요.")

# weather = "맑음"

# if weather == "비":
#   print("우산을 챙기세요")
# elif weather == "미세먼지":
#   print("마스크를 챙기세요.")
# else:
#   print("준비물이 필요 없어요.")

# weather = input("오늘 날씨는 어때요?")
# print(weather)

# weather = input("오늘 날씨는 어때요?")

# if weather == "비":
#   print("우산을 챙기세요.")
# elif weather == "미세먼지":
#   print("마스크를 챙기세요.")
# else:
#   print("준비물이 필요 없어요.")

# weather = input("오늘 날씨는 어때요?")

# if weather == "비" or weather == "눈":
#   print("우산을 챙기세요.")
# elif weather == "미세먼지":
#   print("마스크를 챙기세요.")
# else:
#   print("준비물이 필요 없어요.")

# temp = int(input("오늘 기온은 어때요?"))

# if 30 <= temp :
#   print("너무 더워요. 외출을 자제하세요.")
# elif 10 <= temp and temp < 30 :
#   print("활동하기 좋은 날씨에요.")
# elif 0 <= temp and temp < 10 :
#   print("외투를 챙기세요.")
# else :
#   print("너무 추워요. 나가지 마세요.")

# temp = int(input("오늘 기온은 어때요?"))

# if 30 <= temp:
#   print("너무 더워요. 외출을 자제하세요.")
# elif 10 <= temp < 30:
#   print("활동하기 좋은 날씨에요.")
# elif 0 <= temp < 10:
#   print("외투를 챙기세요.")
# else:
#   print("너무 추워요. 나가지 마세요.")

temp = int(input("오늘 기온은 어때요?"))

if temp >= 30 :
  print("너무 더워요. 외출을 자제하세요.")
elif temp >= 10 :
  print("활동하기 좋은 날씨에요.")
elif temp >= 0 :
  print("외투를 챙기세요.")
else :
  print("너무 추워요. 나가지 마세요.")