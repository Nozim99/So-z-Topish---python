import random

words = [
    "nozimbek",
    "mezes",
    "maxpiraliyev",
    "frontend",
    "backend",
    "python",
    "javascript",
    "django",
    "fastapi",
    "react",
    "next",
]


def getWord():
    random_word = random.choice(words)
    return random_word


def display(current_word, random_words):
    # word_arr = list(current_word)
    new_word = ""
    random_lower_words = random_words.lower()

    for symbol in current_word:
        if symbol in random_lower_words:
            new_word += symbol
        else:
            new_word += "-"

    return new_word.upper()


def play():
    random_word = random.choice(words)
    user_words = ""

    print(f"Yashirin so'z > {"-" * len(random_word)}")

    while True:
        user_word = input("Harf kiriting >> ")
        user_words = "".join(set(user_words + user_word.upper()))
        response_word = display(random_word, user_words)
        print(f"Siz kiritgan harflar: {user_words}\n{response_word}")
        if "-" not in response_word:
            return response_word

print("So'z kiritib yashirin so'zni toping")
print(play())
