def analyze_text(text):
    words = text.split()
    word_count = len(words)
    letter_count = 0
    number_count = 0
    upper_count = 0
    lower_count = 0
    for i in text:
        if i.isalpha():
            letter_count += 1
            if i.isupper():
                upper_count += 1
            if i.islower():
                lower_count += 1
        elif i.isdigit():
            number_count += 1
    most_frequent_letter = {}
    for word in text:
        if word in most_frequent_letter:
            most_frequent_letter[word] = most_frequent_letter[word] + 1
        else:
            most_frequent_letter[word] = 1
    most_1 = 0
    most = ""
    for word in most_frequent_letter:
        if most_frequent_letter[word] > most_1:
            most_1 = most_frequent_letter[word]
            most = word
    max_word = {}
    for word in words:
        if word in max_word:
            max_word[word] = max_word[word] + 1
        else:
            max_word[word] = 1
    most_word = ""
    most_count = 0
    for word in max_word:
        if max_word[word] > most_count:
            most_count = max_word[word]
            most_word = word
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    palindrome_count = 0
    for word in words:
        if word == word[::-1]:
            palindrome_count += 1
    return (
        word_count,
        letter_count,
        number_count,
        most,
        most_word,
        longest_word,
        shortest_word,
        palindrome_count,
        upper_count,
        lower_count
    )


text = input("Enter your text: ")

(
    word_count,
    letter_count,
    number_count,
    most_frequent_letter,
    most_frequent_word,
    longest_word,
    shortest_word,
    palindrome_count,
    upper_count,
    lower_count
) = analyze_text(text)

print("Word count:", word_count)
print("Letter count:", letter_count)
print("Number count:", number_count)
print("Most frequent letter:", most_frequent_letter)
print("Most frequent word:", most_frequent_word)
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
print("Palindrome word count:", palindrome_count)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)