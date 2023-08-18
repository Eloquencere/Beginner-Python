class ImgyError(Exception):
    pass


def MySqrt(num):
    return pow(num, 0.5)


try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ImgyError
    print(MySqrt(num))
except ValueError:
    print("Must be a number")
except ImgyError:
    print("Imaginary Root")
