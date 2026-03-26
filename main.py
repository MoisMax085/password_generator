import random
import string
import os
import pyperclip

def ask_():
    lengt = int(input("\nВведите желаемую длину пароля: "))
    os.system("cls" if os.name == "nt" else "clear")
    special_symbols = int(input("Нужно ли использовать специальные символы ?" + "\033[31m{}\033[0m".format("\n1. ") + "Да" + "\033[31m{}\033[0m".format("\n2. ") + "Нет\n"))
    os.system("cls" if os.name == "nt" else "clear")
    return lengt, special_symbols


def get_alphabet(special_symbols):
    if special_symbols == 1:
        alphabet = ''.join(chr(i) for i in range(33, 127))
    else:
        alphabet = string.ascii_letters + string.digits
    return alphabet

def set_password(lengt, alpabet):
    passw = ''.join(random.choice(alpabet) for i in range(0, lengt+1))
    pyperclip.copy(passw)
    print(f"\nВаш пароль: \n{passw}")
    print("\033[31m{}\033[0m".format("\n\nВаш пароль скопирован в буфер обмена."))
def main():
    [lengt, special_symbols] = ask_()
    alphabet = get_alphabet(special_symbols)
    set_password(lengt, alphabet)
    input()

if __name__ == "__main__":
    main()
