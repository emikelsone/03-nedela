numbers = [1, 2, 3, 4, 5, 6]
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

even_numbers = []
for num in numbers:
    if num % 2 == 0: # parbauda, vai skaitlis ir pāra skaitlis. Ja num % 2 ir vienāds ar 0, tas nozīmē, ka num ir pāra skaitlis.
        even_numbers.append(num)
print("Even numbers:", even_numbers)

print("\n ---Slice ---")
print("First three numbers:", numbers[0:3])
print("Last three numbers:", numbers[-3:])
print("Numbers from index 2 to 4:", numbers[2:5])
