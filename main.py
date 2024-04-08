# ANIMATIONS:
# inside out    - 1
# outside in    - 2
# rapidly blink - 3
# upside down   - 4
# downside up   - 5
# random        - 6

from animations import *


def write(s, file_name):
    file_name.write(s)


def main():
    counter = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    filename = input("filename: ")
    file = open(filename, "a")
    for _ in range(0, 66):
        r = random.randint(1, 6)
        while counter[r] == 11:
            r = random.randint(1, 6)
        counter[r] += 1

        if r == 1:
            write(animate_1(), file)
        elif r == 2:
            write(animate_2(), file)
        elif r == 3:
            write(animate_3(), file)
        elif r == 4:
            write(animate_4(), file)
        elif r == 5:
            write(animate_5(), file)
        elif r == 6:
            write(animate_6(), file)

    for value in counter.values():
        print(" ", value)


if __name__ == "__main__":
    main()
