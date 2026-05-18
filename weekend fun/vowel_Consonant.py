letter = input("Enter a letter: ")
if len(letter) == 1 and letter.isalpha():
    if letter.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
