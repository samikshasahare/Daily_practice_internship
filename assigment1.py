# Shopping Cart Management System

class Product:
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category

    def display_product(self):
        print(f"{self.product_id}. {self.product_name} - ₹{self.price} ({self.category})")


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_item_total(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append(CartItem(product, quantity))
        print(product.product_name, "added to cart")

    def remove_product(self, product_name):
        for item in self.items:
            if item.product.product_name == product_name:
                self.items.remove(item)
                print(product_name, "removed from cart")
        print("Product not found")

    def update_quantity(self, product_name, quantity):
        for item in self.items:
            if item.product.product_name == product_name:
                item.quantity = quantity
                print("Quantity updated")
        print("Product not found")

    def view_cart(self):
        print("\nCart Items:")
        for item in self.items:
            print(item.product.product_name,
                  "Quantity:", item.quantity,
                  "Total: ₹", item.calculate_item_total())

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_item_total()
        return total

    def discount(self):
        total = self.calculate_total()

        if total > 10000:
            return total * 0.15
        elif total > 5000:
            return total * 0.10
        else:
            return 0

    def generate_invoice(self):
        print("\n --- INVOICE --- ")
        for item in self.items:
            print(item.product.product_name,"x", item.quantity,"= ₹", item.calculate_item_total())

        subtotal = self.calculate_total()
        discount = self.discount()
        final_amount = subtotal - discount

        print("---------------------")
        print("Subtotal: ₹", subtotal)
        print("Discount: ₹", discount)
        print("Final Amount: ₹", final_amount)


# Method calling
laptop = Product(1, "Laptop", 50000, "Electronics")
mouse = Product(2, "Mouse", 500, "Electronics")
keyboard = Product(3, "Keyboard", 300, "Electronics")

print("Available Products:")
laptop.display_product()
mouse.display_product()
keyboard.display_product()

cart = ShoppingCart()
cart.add_product(laptop, 2)
cart.add_product(mouse, 2)
cart.add_product(keyboard, 2)

cart.view_cart()
cart.generate_invoice()