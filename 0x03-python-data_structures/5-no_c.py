#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c not in ['c', 'C']:
            new_string += char
    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
