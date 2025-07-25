import random
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def main():
    numbers = [1.5, 2.3, 3.7]
    word_list = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(word_list)
    print(word_list)
    append_random_words(word_list, 4)
    print(word_list)

def append_random_words(wordlist, quantity=1):
    for _ in range(quantity):
        wordlist.append(random.choice(words))

def append_random_numbers(numlist, quantity=1):
    for _ in range(quantity):
        num = random.uniform(0, 100)
        num = round(num, 1)
        numlist.append(num)


if __name__ == "__main__":
    main()
