#!/usr/bin/python3
fchars = [chr(i) for i in range(97, 123) if chr(i) not in "qe"]
put = "".join(fchars)
print("{}".format(put), end='')
