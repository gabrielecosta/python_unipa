"""
Scrivere la funzione ricorsiva is_palindrome(string)
che ritorna True se string è palindroma, cioè se letta in ordine inverso
è la stessa stringa, come ad esempio la stringa:
"i topi non avevano nipoti"
"""

def is_palindrome(string):
    value = ""
    for letter in string:
        if letter.isalpha():
            value += letter.lower()
    print(f"Stringa formattata: {value}")
    is_palidrome = True
    for i in range(len(value)):
        if value[i]!=value[(len(value)-1)-i]:
            is_palidrome = False
    return is_palidrome

def main():
    value = input("Inserisci stringa: ")
    print(f"La parola inserita è palindroma? {is_palindrome(value)}")

if __name__ == "__main__":
    main()