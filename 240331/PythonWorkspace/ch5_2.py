cabinet = {3: "푸", 100: "피글렛"}
print(cabinet)

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet.get(5))
print("hi")
print(cabinet[5])
print("hi")

print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print("곰" in "곰돌이")
print("돌이" in "곰돌이")
print("푸" in "곰돌이")

print(cabinet)
cabinet["A-3"] = "티거"
cabinet["C-20"] = "이요르"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
# print(cabinet.clear())
cabinet.clear()
print(cabinet)