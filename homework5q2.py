def kToF(k):
    # Convert Kelvin to Fahrenheit
    return (k - 273.15) * 9 / 5 + 32


def main():
    print("Kelvin\tFahrenheit")

    for k in range(0, 301, 20):
        fahrenheit = kToF(k)
        print(f"{k}\t{fahrenheit:.2f}")


main()