from random import randint


def gen_random(num_count: int, begin: int, end: int):
    for i in range(num_count):
        print(randint(begin, end))


def main():
    gen_random()


if __name__ == "__main__":
    main()
