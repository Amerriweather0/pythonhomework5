def chaos(k, x, n):
    # Calculate and print the logistic values
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


def main():
    k = float(input("Enter the value of k: "))
    x = float(input("Enter the starting value of x: "))
    n = int(input("Enter the number of iterations: "))

    chaos(k, x, n)


main()