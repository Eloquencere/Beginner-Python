def OddDigits(number):
    while number != 0:
        Digit = number % 10
        EvenDigit = Digit % 2 == 0
        if EvenDigit:
            return False
        number //= 10
    return True


low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
for number in (low, high + 1):
    if OddDigits(number):
        print(number, end=",")