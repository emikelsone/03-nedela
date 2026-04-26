def capitalize(text):
    return text.capitalize()

def count_words(text):
    words= text.split()
    return len(words)

if __name__ == "__main__":
    print(capitalize("hello"))
    print(count_words("hello world python"))