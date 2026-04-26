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