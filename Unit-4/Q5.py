def number():
    try:
        ip = input("Enter 2 numbers(separated by a comma): ")
        nums = ip.split(",")
        num1 = int(nums[0])
        num2 = int(nums[1])
        div = num1 / num2
    except ValueError:
        print("Format not allowed")
    except ZeroDivisionError:
        print("Second number can't be zero")
    finally:
        print(" 'Finally' was executed")


number()
