#method 1 by doing 3 and 5 first

# for number in range (1, 101):
#     if number % 3==0 and number % 5==0:
#         print("FizzBuzz")
#     elif number % 3==0:
#         print("Fizz")
#     elif number % 5==0:
#         print("Buzz")
#     else:
#         print(number)

#method 2 by doing 3 firat and then 5 
for number in range (1, 101):
    if number % 3==0:
        print("Fizz")
    elif number % 5==0:
        print("Buzz")
    elif number % 3==0 and number % 5==0:
        print("FizzBuzz")
    else:
        print(number)

