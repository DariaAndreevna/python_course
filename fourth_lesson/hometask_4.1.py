input = [0,9,4,5,0,8,0,2,0,0,0]
x = input.count(0)

for i in range(x):
    input.remove(0)
    input.append(0)

print(input)
