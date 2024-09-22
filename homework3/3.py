import re


def load_words(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file] 

#a)
def find_words_ending_with_ime(words):
    return [word for word in words if word.endswith('ime')]

# b)
def find_words_with_ave(words):
    return [word for word in words if len(word) >= 4 and word[1:4] == 'ave']

# c) 
def count_words_with_common_letters(words):
    common_letters = set('rstlne')
    return [word for word in words if any(letter in word for letter in common_letters)]

# d) 
def percentage_words_with_rstln(words):
    words_with_rstln = [word for word in words if any(letter in word for letter in 'rstln')]
    return (len(words_with_rstln) / len(words)) * 100

# e) 
def find_words_with_no_vowels(words):
    vowels = 'aeiou'
    return [word for word in words if not any(vowel in word for vowel in vowels)]

# f) 
def find_words_with_all_vowels(words):
    vowels = set('aeiou')
    return [word for word in words if vowels.issubset(set(word))]

file_name = 'wordlist.txt'
words = load_words(file_name)


words_ending_with_ime = find_words_ending_with_ime(words)
print("Words ending with 'ime':", words_ending_with_ime)


words_with_ave = find_words_with_ave(words)
print("Words with 'ave' in positions 2, 3, and 4:", words_with_ave)


words_with_common_letters = count_words_with_common_letters(words)
print(f"Number of words containing 'r', 's', 't', 'l', 'n', 'e': {len(words_with_common_letters)}")

percentage_with_rstln = percentage_words_with_rstln(words)
print(f"Percentage of words containing at least one of 'r', 's', 't', 'l', 'n': {percentage_with_rstln:.2f}%")


words_with_no_vowels = find_words_with_no_vowels(words)
print("Words with no vowels:", words_with_no_vowels)


words_with_all_vowels = find_words_with_all_vowels(words)
print("Words containing every vowel:", words_with_all_vowels)
