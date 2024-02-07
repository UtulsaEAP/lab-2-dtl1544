
def real_estate():
    
    current_price = int(input("Enter the current price: "))
    last_month_price = int(input("Enter the last month's price: "))

    price_change = current_price - last_month_price
    monthly_mortgage = (current_price * 0.051) / 12

    print(f"This house is ${current_price}. The change is ${price_change} since last month.")
    print(f"The estimated monthly mortgage is ${monthly_mortgage:.2f}.")

if __name__ == "__main__":
    real_estate()