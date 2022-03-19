ans = 0
neg_flag = False
x = int(input("Enter an integer: "))

if x < 0:
    neg_flag = True

while ans ** 2 < x:
    ans += 1

if ans ** 2 == x:
    print(f"The square root of {x} is {ans}")
else:
    print(f"{x} is not a perfect square")
    if neg_flag:
        print(f"Just checking... did you mean {-x}?")
