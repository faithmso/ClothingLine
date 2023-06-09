from helper_functions import process_csv_supplies
from collections import deque
from collections import namedtuple
from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap
from collections import Counter
from collections import UserDict
from collections import UserList
from collections import UserString

# deque
# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
supplies_deque = deque()
for supply in csv_data:
    if supply[2] == 'important':
        # With a deque, we can append to the front directly
        supplies_deque.appendleft(supply)
    else:
      supplies_deque.append(supply)
ordered_important_supplies = deque()
for num in range(25):
  ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()

for num in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())

# namedtuple


clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
ClothingItem = namedtuple('ClothingItem', ['type', 'color','size','price'])
new_coat = ClothingItem('coat', 'black', 'small', 14.99)
coat_cost = new_coat.price

updated_clothes_data = []
for cloth in clothes:
  updated_clothes_data. append(ClothingItem(cloth[0], cloth[1], cloth[2], cloth[3]))

print(updated_clothes_data)

#defaultdict
site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
validated_locations = defaultdict(lambda : 'TODO: Add to website')
validated_locations.update(site_locations)

for product in updated_products:
  site_locations[product] = validated_locations[product]

print(site_locations)

#OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!

# Checkpoint #1
orders = OrderedDict(order_data)

# Checkpoint #2
to_move = []
to_remove = []
for key, val in orders.items():
  if val == 'returned':
    to_move.append(key)
  elif val == 'canceled':
    to_remove.append(key)

# Checkpoint #3
for item in to_remove:
  orders.pop(item)

# Checkpoint #4
for item in to_move:
  orders.move_to_end(item)

# Checkpoint #5
print(orders)

#ChainMap
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
profit_map = ChainMap(*year_profit_data)

def get_profits(input_map):
  holiday_profit = 0
  standard_profit = 0
  for key in input_map.keys():
    if 'holiday' in key:
      holiday_profit += input_map[key] 
    else:
      standard_profit += input_map[key]
  return standard_profit, holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

for data in new_months_data:
  profit_map = profit_map.new_child(data)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(year_diff_standard_profit)
print(year_diff_holiday_profit)

#Counter
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
def find_amount_sold(opening, closing, item):
 opening_count = Counter(opening)
 closing_count = Counter(closing)
 opening_count.subtract(closing_count)
 return opening_count[item]
 

tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')
print(tshirts_sold)

#wrapper
class Customer:
 
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number


class CustomerWrap(Customer):
 
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
 
  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)


customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()

#UserDict

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
class OrderProcessingDict(UserDict):

  def clean_orders(self):
    to_del = []
    for key, val in self.data.items():
      if val['order_status'] == 'complete':
        to_del.append(key)

    for item in to_del:
      del self.data[item]

process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)

#UserList

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):
  def append(self, item):
    self.data.append(item)
    self.data.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)

#UserString
str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
class SubtractString(UserString):
  
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)

#project


overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# Write your code below!
split_prices = deque()
for item in overstock_items:
  if item[1] > 20.0:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)
print(split_prices)

ClothesBundle = namedtuple('ClothesBundle',('bundle_items', 'bundle_price'))

bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(),split_prices.pop(),split_prices.pop(),split_prices.popleft(),split_prices.popleft()]

  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

print(bundles)
promoted_bundles = []
for bundle in bundles:
  if bundle[1] > 100:
    promoted_bundles.append(bundle)

print(promoted_bundles)