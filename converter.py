


def binary_to_decimal(user_number, binary_number):
    
    binary_number = 15
    user_number = input(int("input a number 1-15"))
    binary = [0, 0, 0, 0]


    if binary_number - 8 <= user_number:
        binary[0] = 1

        if binary_number - 4 <= user_number:
            binary[1] = 1

            if binary_number - 2 <= user_number:
                binary[2] = 1

                if binary_number - 1 <= user_number:
                    binary[3] = 1

    print(bianry)


binary_to_decimal(user_number, binary_number)
