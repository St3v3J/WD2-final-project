# this program input from the user, and calclulates the cube. If the input is zero it exits.
def cube(num):
    return num * num * num

def get_input():
    result =  int(input("enter any number, press zero to exit:"))
    return result

number = get_input()
while number != 0:
    value = cube(number)
    print(value)
    number = get_input()