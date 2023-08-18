class NegError(Exception):
    pass


def readposint():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegError
        print(int(num))
    except ValueError:
        print("String not allowed")
    except NegError:
        print("Negative not allowed")


readposint()
