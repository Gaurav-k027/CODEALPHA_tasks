
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300,
    "AMZN": 130
}

def main():
    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    portfolio = {}
    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    total_value = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value
        print(f"{stock} - {qty} shares = ${value}")

    print("\nTotal Investment Value: $", total_value)

    choice = input("Do you want to save this result to a file? (y/n): ").lower()
    if choice == "y":
        with open("portfolio.txt", "w") as f:
            f.write("Your Portfolio:\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock} - {qty} shares = ${value}\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
        print("Portfolio saved to portfolio.txt")

if __name__ == "__main__":
    main()
