import re


def binary(n, bits):
    return format(n & ((1 << bits) - 1), f'0{bits}b')


expression = input("Enter arithmetic expression: ").strip()

# Convert Unicode minus and plus signs to standard symbols
expression = expression.replace('−', '-').replace('＋', '+')

pattern = r'\s*\(*\s*\(?\s*([+-]?\d+)\s*\)?\s*([+-])\s*\(?\s*([+-]?\d+)\s*\)?\s*\)*\s*'

match = re.fullmatch(pattern, expression)

if not match:
    print("Invalid expression!")
    raise SystemExit

a = int(match.group(1))
op = match.group(2)
b = int(match.group(3))

if not (-128 <= a <= 127 and -128 <= b <= 127):
    print("Operands must be within -128 to 127.")
    raise SystemExit

result = a + b if op == '+' else a - b

print("\nOperand 1:", a)
print("Binary (8-bit):", binary(a, 8))

print("Operand 2:", b)
print("Binary (8-bit):", binary(b, 8))

print("\nResult (decimal):", result)
print("Result (16-bit binary):", binary(result, 16))
print("Result (8-bit binary):", binary(result, 8))

overflow = result < -128 or result > 127
print("8-bit Arithmetic Overflow:", "Yes" if overflow else "No")
