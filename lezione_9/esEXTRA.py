word = input("Scrivi una parola: ")

with open('withlove.txt', 'w') as f:
    for i in range(100):
        print(f"{word} \t {word} \t {word}", file=f)