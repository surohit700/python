def swap(x, y, inplace=False):
    if inplace:
        x, y = y, x
        return x, y
    else:
        return y, x


a = 3
b = 4


a, b = swap(a, b, inplace=True) 

print(a, b)