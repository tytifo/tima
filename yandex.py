a = input()
min1 = int(input())
max1 = int(input())
min2 = int(input())
max2 = int(input())
with open(a) as file:
    int_number = file.read()
    b = int_number.split()
    for i in b:
        v = i.split(':')
        print(v)
        print(v[-1])
        if int(v[-1]) <= min1 and min1 >= int(v[-2]):
            if int(v[-1]) <= max1 and max1 >= int(v[-2]):
                if int(v[-1]) <= max2 and max2 >= int(v[-2]):
                    if int(v[-1]) <= min2 and min2 >= int(v[-2]):
                        print(v[0])
