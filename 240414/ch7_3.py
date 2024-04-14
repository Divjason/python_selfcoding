# def profile(name, age, main_lang) :
#     print("이름 : {0}, \t 나이 : {1}, \t 주 사용 단어 : {2}".format(name, age, main_lang))

# profile("찰리", 20, "파이썬")
# profile("루시", 25, "자바")

def profile(name, age=20, main_lang="파이썬") :
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))

# profile("찰리")
# profile("루시")

profile("찰리", 22)
profile("찰리", 24, "자바")