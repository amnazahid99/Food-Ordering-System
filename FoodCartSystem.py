class MenuItem:
  def __init__(self, name, description, price, available=True):
      self.name = name
      self.description = description
      self.price = price
      self.available = available

class FoodCart:
  def __init__(self):
      self.menu = {}
      self.orders = []

  def add_menu_item(self, category, item):
      if category not in self.menu:
          self.menu[category] = []
      self.menu[category].append(item)

  def display_menu(self):
      print("----- Menu -----")
      for category, items in self.menu.items():
          print(f"\n{category.capitalize()}:")
          for item in items:
              availability = "Available" if item.available else "Not Available"
              print(f"{item.name}: {item.description} - ${item.price} ({availability})")

  def place_order(self, item_name):
      found = False
      for items in self.menu.values():
          for item in items:
              if item.name.lower() == item_name.lower():
                  found = True
                  if item.available:
                      self.orders.append(item)
                      print(f"Added {item_name} to the cart.")
                  else:
                      print(f"Sorry, {item_name} is not available at the moment.")
      if not found:
          print(f"Sorry, {item_name} is not found in the menu.")

  def calculate_total(self):
      return sum(item.price for item in self.orders)


# Sample Menu
menu_items = [
  # Burgers
  MenuItem("Classic Burger", "Classic beef burger", 5.99),
  MenuItem("Cheeseburger", "Burger with cheese", 6.99),
  # Pizzas
  MenuItem("Margherita Pizza", "Classic Margherita pizza", 8.99),
  MenuItem("Pepperoni Pizza", "Pizza with pepperoni topping", 9.99),
  # Salads
  MenuItem("Caesar Salad", "Classic Caesar salad", 6.99),
  MenuItem("Greek Salad", "Fresh Greek salad", 7.99),
  # Desserts
  MenuItem("Chocolate Cake", "Rich chocolate cake", 4.99),
  MenuItem("Cheesecake", "Creamy cheesecake", 5.99),
  # Juices and Cold Drinks
  MenuItem("Orange Juice", "Freshly squeezed orange juice", 2.99),
  MenuItem("Cola", "Classic cola drink", 1.99),
  # Milkshakes
  MenuItem("Vanilla Milkshake", "Creamy vanilla milkshake", 3.99),
  MenuItem("Chocolate Milkshake", "Rich chocolate milkshake", 4.49),
  # Coffees
  MenuItem("Hot Coffee", "Freshly brewed hot coffee", 2.49),
  MenuItem("Iced Coffee", "Chilled iced coffee", 3.49),
  MenuItem("Cappuccino", "Classic cappuccino", 3.99),
  MenuItem("Latte", "Smooth latte", 4.49),
]

# Create a food cart and add menu items
food_cart = FoodCart()
for item in menu_items:
  # Extract category from the item name
  category = item.name.split()[0]
  food_cart.add_menu_item(category, item)

# Display welcome message and the menu
print("Welcome to Food Divine!")
food_cart.display_menu()

# Place orders
while True:
  order = input("Enter an item to order (q to quit): ")
  if order.lower() == "q":
      break
  else:
      food_cart.place_order(order)

# Display customer data and total bill
print("\n----- Customer Data -----")
for item in food_cart.orders:
  print(f"{item.name}: ${item.price}")
total = food_cart.calculate_total()
print(f"Total Bill: ${total:.2f}")
print("Thank you for coming to Food Divine!")
