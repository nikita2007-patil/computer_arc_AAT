binary = input("Enter the binary number: ")

if not binary or any(bit not in "01" for bit in binary):
    print("Invalid binary number!")
    exit()

operation = input("Enter rotation type (ROR/RCR): ").upper()

if operation == "ROR":
    positions = int(input("Enter number of positions: "))

    print("Original number:", binary)

    for i in range(positions):
        binary = binary[-1] + binary[:-1]
        print("After rotation", i + 1, ":", binary)

    print("Final result:", binary)

elif operation == "RCR":
    positions = int(input("Enter number of positions: "))
    carry = 0

    print("Original number:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        last_bit = int(binary[-1])
        binary = str(carry) + binary[:-1]
        carry = last_bit

        print("After rotation", i + 1, ":", binary)
        print("Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)

else:
    print("Invalid rotation type!")
