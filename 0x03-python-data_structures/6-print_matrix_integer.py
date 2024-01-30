#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))


if __name__ == "__main__":
    matrix = [
        list(map(int, input().split())),
        list(map(int, input().split())),
        list(map(int, input().split())),
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
