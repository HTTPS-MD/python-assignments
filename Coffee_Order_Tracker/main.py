import database

if __name__ == "__main__":
    coffee_order = input("Hello, what's your order po? ")
    customer_name = input("What's your name for the cup po? ")

    database.save_order(customer_name, coffee_order)
    print("\nThank You! Your order will be served nalang po later. Thank You!")
