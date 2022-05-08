import sys


def read_file(file_name):
    with open(f"{file_name}", "r") as f:
        a = [int(line.strip()) for line in f]
    return a


def get_steps(a):
    sorted(a)

    if len(a) % 2 == 0:

        m = (a[(len(a) // 2) - 1] + a[(len(a) // 2) + 1]) // 2
    else:
        m = a[len(a) // 2]

    steps = sum(abs(i - m) for i in a)
    return print(steps)


if __name__ == "__main__":
    num = read_file(sys.argv[1])
    # print(num)
    get_steps(num)
