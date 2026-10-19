
import csv

# Sample current stock prices
stock_prices = {
    "AAPL": 230.00,
    "GOOGL": 180.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
    "TSLA": 250.00
}

portfolio = {}

print("===================================")
print("     INVESTMENT PORTFOLIO TRACKER")
print("===================================")

number = int(input("How many stocks do you want to add? "))

for i in range(number):
    print(f"\nStock {i + 1}")

    ticker = input("Enter stock symbol (AAPL/GOOGL/MSFT/AMZN/TSLA): ").upper()

    if ticker not in stock_prices:
        print("Invalid stock symbol. Try again.")
        continue

    buy_price = float(input("Enter buying price per share: "))
    quantity = int(input("Enter number of shares: "))

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": stock_prices[ticker]
    }

total_investment = 0
total_value = 0

print("\n========== PORTFOLIO SUMMARY ==========")

for ticker, details in portfolio.items():
    invested = details["buy_price"] * details["quantity"]
    current_value = details["current_price"] * details["quantity"]
    gain_loss = current_value - invested
    percentage = (gain_loss / invested) * 100

    total_investment += invested
    total_value += current_value

    print(f"\nStock: {ticker}")
    print(f"Invested: ${invested:.2f}")
    print(f"Current Value: ${current_value:.2f}")
    print(f"Gain/Loss: ${gain_loss:.2f}")
    print(f"Percentage: {percentage:.2f}%")

total_gain_loss = total_value - total_investment

if total_investment > 0:
    total_percentage = (total_gain_loss / total_investment) * 100
else:
    total_percentage = 0

print("\n========== TOTAL PORTFOLIO ==========")
print(f"Total Investment: ${total_investment:.2f}")
print(f"Total Market Value: ${total_value:.2f}")
print(f"Total Gain/Loss: ${total_gain_loss:.2f}")
print(f"Overall Percentage: {total_percentage:.2f}%")

# Save summary to CSV file
with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock", "Buy Price", "Quantity",
        "Current Price", "Invested",
        "Current Value", "Gain/Loss", "Percentage"
    ])

    for ticker, details in portfolio.items():
        invested = details["buy_price"] * details["quantity"]
        current_value = details["current_price"] * details["quantity"]
        gain_loss = current_value - invested
        percentage = (gain_loss / invested) * 100

        writer.writerow([
            ticker,
            details["buy_price"],
            details["quantity"],
            details["current_price"],
            invested,
            current_value,
            gain_loss,
            percentage
        ])

print("\nPortfolio summary saved to portfolio_summary.csv")
