# def myFunc(*args, **kwargs):
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#     print(kwargs["KEYONE"])
#     print(kwargs["KEYTWO"])

# myFunc('hey', True, 29, 'wow', KEYONE = "TEST", KEYTWO = 7)

import sys

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)