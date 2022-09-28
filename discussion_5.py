import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max = 0
		maxim = self.items[0].name
		for i in range(len(self.items)):
			if (self.items[i].stock > max):
				max = self.items[i].stock
				maxim = self.items[i].name
		return maxim

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max = 0
		maxim = self.items[0].name
		for i in range(len(self.items)):
			if (self.items[i].price > max):
				max = self.items[i].price
				maxim = self.items[i].name
		return maxim	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.warehouse1 = Warehouse([])

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a(self.item1.name), 0, "Test Count, 0 'a's")
		self.assertEqual(count_a(self.item3.name), 1, "Test Count, 1 'a'")
		self.assertEqual(count_a(self.item4.name), 2, "Test Count, 2 'a'")
		self.assertEqual(count_a(self.item5.name + " " + self.item3.name), 3, "Test Count, full sentence")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse1.add_item(self.item1)
		self.assertEqual(self.warehouse1.items[0].name, "Beer" ,"Test add item")

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.warehouse1.add_item(self.item1)
		self.assertEqual(self.warehouse1.get_max_stock(), "Beer", "one item")
		self.warehouse1.add_item(self.item2)
		self.assertEqual(self.warehouse1.get_max_stock(), "Cider", "two items")
		self.warehouse1.add_item(self.item5)
		self.assertEqual(self.warehouse1.get_max_stock(), "CocaCola", "two items")
		self.warehouse1.add_item(self.item3)
		self.assertEqual(self.warehouse1.get_max_stock(), "Water", "two items")

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.warehouse1.add_item(self.item3)
		self.assertEqual(self.warehouse1.get_max_price(), "Water", "two items")
		self.warehouse1.add_item(self.item1)
		self.assertEqual(self.warehouse1.get_max_price(), "Beer", "one item")
		self.warehouse1.add_item(self.item2)
		self.assertEqual(self.warehouse1.get_max_price(), "Beer", "two items")
		self.warehouse1.add_item(self.item4)
		self.assertEqual(self.warehouse1.get_max_price(), "Beer", "two items")

def main():
	unittest.main()

if __name__ == "__main__":
	main()