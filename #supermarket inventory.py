#supermarket inventory
inventory = {
    "apple" : {"price": 1.0, "quantity": 100},
    "banana": {"price": 0.5, "quantity": 50 },
    "orange": {"price": 1.5, "quantity": 30 },
    "potato": {"price": 2.0, "quantity": 100 },
    "tomato": {"price": 2.0, "quantity": 100 },
    "onion": {"price": 1.0, "quantity": 200},
    "mango": {"price": 1.5, "quantity": 150 },
}

#inventory
def display_inventory():
  print("/tSupermarket inventory:")
  print("-" * 30)
  for item, details in inventory.items():
    print(f"{item.capitalize}: ${details['price']} each, {details['quantity']}remaining in stock")
    print("-" *30)

#customers shopping
def customer_shopping():
  print("/nWelcome to the virtual supermarket")
  cart = {}
  while True:
    display_inventory()
    item = input("Enter the name of the item you want to buy or(type 'done' to finish):").lower()
    if item == "done":
       break
    if item not in inventory:
      print("Sorry, that item is not available.")
      continue
    quantity = int(input(f"How many {item}s would you like to buy? "))
    if quantity > inventory[item]["quantity"]:
      print("Sorry, we don't have enough stock available for your request.")
    else:
      inventory[item]["quantity"] -=quantity
      cart[item] = {"price": inventory[item]["price"], "quantity": quantity}
      print(f"Added {quantity}{item}(s)to your cart.")

  return cart

#generate a receipt
def generate_receipt(cart):
  print("/nReceipt:")
  print("-" * 30)
  total = 0
  for item, details in cart.items():
    cost = details["price"] * details["quantity"]
    total += cost
    print(f"{item.capitalize()}: {details['quantity']} * ${details['price']} = ${cost:.2f}")
  print("-" * 30)
  print(f"Total: ${total:.2f}")
  print("-" * 30)

#manage multiple customers
def main():
  while True:
    cart = customer_shopping()
    if cart:
      generate_receipt(cart)
    another = input("Is there another customer? (yes/no): ").lower()
    if another != "yes":
      print("Thankyou for shopping with us!")
    break



main()