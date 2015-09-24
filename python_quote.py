import random


def random_python_quote():

    quotes = ("It's just a flesh wound.",
              "He's not the Messiah. He's a very naughty boy!",
              "THIS IS AN EX-PARROT!!")
    rand_index = random.randint(0, len(quotes)-1)
    print('hello')
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
