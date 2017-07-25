def divide_by_zero(a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(c)
    finally:
        print("I'm done")
