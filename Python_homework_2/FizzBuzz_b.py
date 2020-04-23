print("Welcome to the FizzBuzz game!")

end = input("Please enter a number between 1 and 100: ")
end = int(end)  # convert string into number

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZBUZZ")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)