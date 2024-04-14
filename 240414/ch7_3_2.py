# def profile(name, age, main_lang) :
#   print(name, age, main_lang)

# # profile(name="찰리", main_lang="파이썬", age=20)
# # profile(main_lang="자바", age=25, name="루시")

# profile("찰리", age=20, main_lang="파이썬")
# # profile(name="루시", 25, "파이썬") => 잘모된 예시

# def profile(name, age, *language) :
#   print("이름 : {0}\t 나이 : {1}\t".format(name, age), end= " ")
#   # print(lang1, lang2, lang3, lang4, lang5)
#   # print(language, type(language))
#   for lang in language :
#     print(lang, end=" ")
#   print()

# profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
# profile("루시", 25, "코틀린", "스위프트", "", "", "")

def add(item) :
  print(item, "붓기")

def americano() :
  add("뜨거운 물")
  add("에스프레소")

print("아메리카노 만드는 법")
americano()