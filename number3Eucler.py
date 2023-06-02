num = 600851475143
div =2

while (num != 1):
    reminder = num%div

    if reminder == 0:
        num=num/div
        print(div)
    else:
        div = div + 1