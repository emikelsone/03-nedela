def capitalize(text):
    return text.capitalize()

def count_words(text):
    words= text.split()
    return len(words)

if __name__ == "__main__":
    print(capitalize("hello"))
    print(count_words("hello world python"))

    def truncate(text, max_length):
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text
    
    def clamp(number, min_value, max_value):
        if number < min_value:
            return min_value
        elif number > max_value:
            return max_value
        return number
    
    if __name__ == "__main__":
        print(capitalize("hello"))
        print(count_words("hello world python"))
        print(truncate("hello world python", 10))
        print(clamp(5, 1, 10))

    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
            
        return True

def factorial(n):
    if n < 0:
        raise ValueError("Skaitlis nevar būt negatīvs")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result
    
def total(numbers):
        total_sum = 0
        for num in numbers:
            total_sum += num
        return total_sum
    
def average(numbers):
        if len(numbers) == 0:
            raise ValueError("Saraksts nevar būt tukšs")
        total_sum = total(numbers)
        return total_sum / len(numbers)  

if __name__ == "__main__":
    print(capitalize("hello"))
    print(count_words("hello world python"))
    
    print(truncate("Šis ir ļoti garš teikums", 10))

    print(clamp(15, 0, 10))
    print(clamp(-5, 0, 10))
    print(clamp(7, 0, 10))

    print(is_prime(7))
    print(is_prime(10))

    print(factorial(5))

    print(total([1, 2, 3, 4, 5]))
    print(average([1, 2, 3, 4, 5]))