subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subwayCh = ["푸", "피글렛", "티거"]
print(subwayCh)

print(subwayCh.index("피글렛"))

subwayCh.append("이요르")
print(subwayCh)

subwayCh.insert(1, "루")
print(subwayCh)

print(subwayCh.pop())
print(subwayCh)

print(subwayCh.pop())
print(subwayCh)

print(subwayCh.pop())
print(subwayCh)

subwayCh.clear()
print(subwayCh)

subway = ["푸", "피글렛", "티거"]
subway.append("푸")

print(subway)
print(subway.count("푸"))

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# num_list.sort(reverse=True)
# print(num_list)

num_list.reverse()
print(num_list)

my_list = [1, 3, 2]
my_list.sort()
print(my_list)

your_list = [1, 3, 2]
new_list = sorted(your_list)
print(your_list)
print(new_list)

mix_list  = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list)

mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]

num_list.extend(mix_list)
print(mix_list)
print(num_list)