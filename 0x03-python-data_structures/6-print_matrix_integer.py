#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n in row:
            print("{:d}".format(n), end='')
        print()


if __name__ == "__main__":
    matrix = [
        list(map(int, input().split())),
        list(map(int, input().split())),
        list(map(int, input().split())),
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
