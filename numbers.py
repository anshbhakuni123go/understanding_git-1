def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


number = int(input("Enter a number: "))
odd_even(number)
