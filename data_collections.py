numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.pop()

total=0
for num in numbers:
    total += num
print("Total:", total)

count=0
for num in numbers:
    count += 1
print("Count:", count)

average = total / count
print("Average:", average)