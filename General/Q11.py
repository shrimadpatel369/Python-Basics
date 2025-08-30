for x in range (1,101):
    if x%3==0 and x%5==0:
        print("FIZZBUZZ")
    elif x%5==0:
        print("BUZZ")
    elif x%3==0:
        print("FIZZ")
    else:
        print()
