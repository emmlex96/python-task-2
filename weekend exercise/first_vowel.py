def first_vowel_position(vow):
    vowels = "aeiouAEIOU"
    for i in range(len(vow)):
        if vow[i] in vowels:
            return i
    return -1  
