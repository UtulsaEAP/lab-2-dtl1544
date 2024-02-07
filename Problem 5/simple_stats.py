
def simple_stats():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    product = num1 * num2 * num3 * num4
    average = (num1 + num2 + num3 + num4) / 4

    rounded_product_int = int(round(product))
    rounded_average_int = int(round(average))

    print(f'{rounded_product_int} {rounded_average_int}')
    print(f'{product:.3f} {average:.3f}')
if __name__ == "__main__":
    simple_stats()