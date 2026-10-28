import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python multiplication.py <number1> <number2>")
        return

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be valid numbers.")
        return

    product = a * b
    print(f"{a} * {b} = {product}")

if __name__ == "__main__":
    main()
