t = str(input("Введіть рядок, який перевищує 8 символів: "))

while (len(t) < 8):

    t = str(input("Введіть ще раз рядок, так як він не перевищує 8 символів: "))

print("Після зрізу перших 8 символів: ", t[8:len(t)])

////////////////////////////////////////////////////////////////////////////////


def is_first_letter_upper(word):
    if word and word[0].isupper():
        return True
    else:
        return False

word = input("Введіть слово: ")

if is_first_letter_upper(word):
    print("Слово починається з великої літери.")
else:
    print("Слово не починається з великої літери.")

////////////////////////////////////////////////////////////////////////////////

sentence = input("Введіть речення: ")
words = sentence.split()
words_sorted = sorted(words, key=len, reverse=True)
print("Слова в порядку спадання їх довжини:")
for word in words_sorted:
    print(word)
