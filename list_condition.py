transactions = [100,200,300,400,500]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07

def get_price_tax_service(bill):
  return bill*(1 + TAX_RATE + SERVICE_CHARGE)

even_numbers = [transaction for transaction in transactions if transaction%2 == 0]

final_prices = [get_price_tax_service(transaction) for transaction in transactions]

total_transaction = 0
for transaction in transactions:
  total_transaction += get_price_tax_service(transaction)

print(even_numbers)
print(final_prices)
print(total_transaction)

# convert string to list
my_string = "Welcome to my party"
list_of_chars = list(my_string)
print(list_of_chars)

# sum list
print(sum([1,3,5,7]))
print(min([1,3,5,7]))
print(max([1,3,5,7]))

developers = ['Hao', 'Tung', 'Quang']
pets = ['dog', 'cat', 'fish']

for dev, pet in zip(developers, pets):
  print(f'{dev} has {pet}')


sorted_by_first_word = sorted(['me','em', 'hi', 'hello', 'you', 'anh'])
print(sorted_by_first_word)

sorted_by_second_word = sorted(['me','em', 'hi', 'hello', 'you', 'anh'], key=lambda el: el[1])
print(sorted_by_second_word)

sorted_by_key_name = sorted([{'name': 'Tung', 'age': 18}, {'name': 'Hao', 'age': 18}, {'name': 'An', 'age': 24}], key=lambda el: el['name'])
sorted_by_key_age = sorted([{'name': 'Tung', 'age': 18}, {'name': 'Hao', 'age': 20}, {'name': 'An', 'age': 24}], key=lambda el: el['age'])
print(sorted_by_key_name)
print(sorted_by_key_age)

matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]

print(matrix[1][2])
print(matrix[2][0])

list_test = []
for row in range(len(matrix)):
  for col in range(len(matrix)):
    list_test.append(matrix[row][col])
    print(matrix[row][col])

print(list_test)

list_converted = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converted)

print([x for x in zip(*matrix)])