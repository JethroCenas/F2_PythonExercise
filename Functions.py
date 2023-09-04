def DecimalToBinary(decimal):
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")

    if decimal == 0:
        return "0"

    binary = ""

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary

def decToOctal(decimal):
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")

    if decimal == 0:
        return "0"

    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8

    return octal

def binaryToNI(binary, ntype):
    if ntype == "dec":
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal
    elif ntype == "octal":
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        octal = ""
        while decimal > 0:
            remainder = decimal % 8
            octal = str(remainder) + octal
            decimal = decimal // 8
        return octal
    elif ntype == "hex":
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            hexadecimal = format(remainder, 'X') + hexadecimal
            decimal = decimal // 16
        return hexadecimal
    else:
        raise ValueError("Invalid type. Supported types are 'dec', 'octal', and 'hex'.")


def decToHex(decimal):
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")

    if decimal == 0:
        return "0"

    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


def main():
    decimal_value = 16

    print(f'\nDecimal to Binary from 16 to {DecimalToBinary(decimal_value)}')
    print(f'Decimal to Hex from 16 to {decToHex(decimal_value)}')
    print(f'Decimal to Octal from 16 to {decToOctal(decimal_value)}')
    binary_value = "10000"
    print(f'Binary to Decimal from 11010 to {binaryToNI(binary_value, "dec")}')
    print(f'Binary to Octal from 11010 to {binaryToNI(binary_value, "octal")}')
    print(f'Binary to Hex from 11010 to {binaryToNI(binary_value, "hex")}')

if __name__ == '__main__':
    main()