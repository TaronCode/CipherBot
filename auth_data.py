token = 'your token'

def Cipher(step, text):
    rus_lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret_text = ""

    for i in text:
        if i in eng_upper_alphabet or i in eng_lower_alphabet:
            if i.islower():
                ret_text += eng_lower_alphabet[(eng_lower_alphabet.index(i) + step) % 26]
            elif i.isupper():
                ret_text += eng_upper_alphabet[(eng_upper_alphabet.index(i) + step) % 26]


        elif i in rus_upper_alphabet or i in rus_lower_alphabet:
            if i.islower():
                ret_text += rus_lower_alphabet[(rus_lower_alphabet.index(i) + step) % 32]
            elif i.isupper():
                ret_text += rus_upper_alphabet[(rus_upper_alphabet.index(i) + step) % 32]
        else:
            ret_text += i

    return ret_text

def disCipher(step, text):
    rus_lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret_text = ""

    for i in text:
        if i in eng_upper_alphabet or i in eng_lower_alphabet:
            if i.islower():
                ret_text += eng_lower_alphabet[(eng_lower_alphabet.index(i) - step) % 26]
            elif i.isupper():
                ret_text += eng_upper_alphabet[(eng_upper_alphabet.index(i) - step) % 26]
        elif i in rus_upper_alphabet or i in rus_lower_alphabet:
            if i.islower():
                ret_text += rus_lower_alphabet[(rus_lower_alphabet.index(i) - step) % 32]
            elif i.isupper():
                ret_text += rus_upper_alphabet[(rus_upper_alphabet.index(i) - step) % 32]
        else:
            ret_text += i

    return ret_text