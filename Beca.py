import random

list = [random.randrange(1,6),random.randrange(1,6),random.randrange(1,6)]
print(list)

if list[0] == list[1] and list[1] == list[2] and list[0] == list[2]:
    print(list[0] * 3)

elif list[0] == list[2]:
    print(list[0] * 2)

elif list[0] == list[1]:
    print(list[0] * 2)

elif list[1] == list[2]:
    print(list[1] * 2)

elif list[0] != list[1] != list[2]:
    print(max(list))
