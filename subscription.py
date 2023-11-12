subscriptions = []

def add_subscription():
    sub_name = input("Enter name of subscription: ")
    sub_price = float(input("Enter price: "))  
    subscription = {'name': sub_name, 'price': sub_price}
    subscriptions.append(subscription)

def display_subscriptions():
    print("\nCurrent Subscriptions:")
    for sub in subscriptions:
        print(f"Name: {sub['name']}, Price: ${sub['price']}")