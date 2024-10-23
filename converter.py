


def binary_to_decimal():
    
    binary_number = 15
    user_number = int(input("input a number 1-15: "))
    binary = [0, 0, 0, 0]


    if user_number >= 8:
        binary[0] = 1
        user_number -= 8

    if user_number >= 4:
        binary[1] = 1
        user_number -= 4

    if user_number >= 2:
        binary[2] = 1
        user_number -= 2

    if user_number >= 1:
        binary[3] = 1
        user_number -= 1

    print(binary)


binary_to_decimal()
