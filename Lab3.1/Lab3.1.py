t = str(input("������ �����, ���� �������� 8 �������: "))

while (len(t) < 8):

    t = str(input("������ �� ��� �����, ��� �� �� �� �������� 8 �������: "))

print("ϳ��� ���� ������ 8 �������: ", t[8:len(t)])

////////////////////////////////////////////////////////////////////////////////


def is_first_letter_upper(word):
    if word and word[0].isupper():
        return True
    else:
        return False

word = input("������ �����: ")

if is_first_letter_upper(word):
    print("����� ���������� � ������ �����.")
else:
    print("����� �� ���������� � ������ �����.")

////////////////////////////////////////////////////////////////////////////////

sentence = input("������ �������: ")
words = sentence.split()
words_sorted = sorted(words, key=len, reverse=True)
print("����� � ������� �������� �� �������:")
for word in words_sorted:
    print(word)
