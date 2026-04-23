#simple and fast bruteforce program :3
import random
import time
not_found = True
tries = 0

password = input("Enter a password made of numbers: ")
start = time.time()

# I know this program will get the same guess number combinations and guessing them again and again, but I still found this to be the most effective and optimized way at cracking short passwords compared to other programs
while not_found:
    pword_guess = "".join(str(random.randint(0, 9)) for _ in range(len(password)))
    tries += 1
    print("Bruteforcing...")
    if password == pword_guess:
        end = time.time()
        print("Password cracked!")
        print("Password was:", password)
        print("Tries it took:",tries)
        print(f"Time it took: {round(end - start, 2)} seconds")
        not_found = False