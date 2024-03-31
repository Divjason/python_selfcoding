my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"푸", "피글렛", "티거"} # 자바 개발자 세트
python = set(["푸", "이요르"]) # 파이썬 개발자 세트

print(java, python)

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("피글렛")
print(python)

java.remove("피글렛")
print(java)