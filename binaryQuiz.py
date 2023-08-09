import random
import time

# Binary to decimal quiz
def quiz1():
    def generate_binary():
        binaryList = []
        for i in range(8):
            binaryList.append(random.randint(0, 1))
        return binaryList

    def calculate_decimal(binaryList):
        binaryTotal = 0
        if binaryList[0] == 1:
            binaryTotal += 128
        if binaryList[1] == 1:
            binaryTotal += 64
        if binaryList[2] == 1:
            binaryTotal += 32
        if binaryList[3] == 1:
            binaryTotal += 16
        if binaryList[4] == 1:
            binaryTotal += 8
        if binaryList[5] == 1:
            binaryTotal += 4
        if binaryList[6] == 1:
            binaryTotal += 2
        if binaryList[7] == 1:
            binaryTotal += 1
        return binaryTotal

    def binary_string(binaryList):
        binaryString = ""
        for binary in binaryList:
            binaryString += f" {binary}"
        return binaryString

    run = 1
    while run == 1:
        # Binary generation
        binaryList = generate_binary() # Generate a random binary
        binaryTotal = calculate_decimal(binaryList) # Calculate the decimal value of the binary
        binaryString = binary_string(binaryList) # Convert the binary to a string

        # User Input
        while True:
            print("Binary Chart:\n|128|64|32|16|8|4|2|1|\n")
            print("What is the decimal value of the following binary? (enter 'x' to exit)")
            print(binaryString)
            # print("Debug:", binaryTotal)

            # Prompt user input and check if it is an integer
            user_input = input("> ")
            if user_input.lower() == "x":
                quit()
            elif user_input.isdigit():
                break
            else:
                print("Invalid input. Please enter a valid integer or enter 'x' to exit.")
        
        # Check Answer
            if int(user_input) == binaryTotal:
                print("Correct! The total is", binaryTotal)
            else:
                print("Incorrect. The total is", binaryTotal)
            time.sleep(2)

# Decimal to binary quiz
def quiz2():
    run = 1
    while run == 1:
        def generate_decimal():
            decimal = random.randint(0, 255)
            return decimal
        
        def decimal_binary(decimal):
            binary = bin(decimal)
            binaryString = str(binary) # Convert the binary to a string
            binaryString = binaryString[2:] # Remove the "0b" from the binary string
            while len(binaryString) < 8: # Add 0s to the beginning of the binary string if it is less than 8 bits
                binaryString = "0" + binaryString
            return binaryString
        
        decimal = generate_decimal()# Generate a random decimal from 0-255
        binaryString = decimal_binary(decimal) # Convert the decimal to a binary string

        # User Input
        while True:
            print("Binary Chart:\n|128|64|32|16|8|4|2|1|\n")
            print("What is the following decimal in binary? (enter 'x' to exit)")
            print(decimal)
            print("Debug:", binaryString)

            user_input = input("> ")
            if user_input.lower() == 'x':
                quit()
            elif all(bit == '0' or bit == '1' for bit in user_input):
                # Check if the binary is 8 bits
                if len(user_input) < 8:
                    # Add 0s to the beginning of the binary string if it is less than 8 bits
                    while len(user_input) < 8:
                        user_input = "0" + user_input
                break
            else:
                print("Invalid input. Enter 0s or 1s or 'x' to quit.")

        # Check Answer
        if user_input == binaryString:
            print("Correct! The total is", binaryString)
        else:
            print("Incorrect. The total is", binaryString)
        time.sleep(2)

if __name__ == "__main__":
    # Select mode
    while True:
        print("Select mode:")
        print("1. Binary to decimal quiz")
        print("2. Decimal to binary quiz")
        print("3. Exit")
        mode = input("> ")
        if mode == "1":
            quiz1()
        elif mode == "2":
            quiz2()
        elif mode == "3":
            quit()
