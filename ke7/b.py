a = [1, 10, 3, 2,  5, 7, 9, 11]

count = 0
for i in a:
    print("hello")
    if i < 5:
        continue
    # count = count + i
    count += i
print(count)
