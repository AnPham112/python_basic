foods = ['pizza', 'hamburger', 'noodles', 'rice', 'hotdog', 'popcorn'];

for food in foods:
  print(food)

for index, food in enumerate(foods):
  print(f"{index} - {food}")

print(foods[:1])
print(foods[0:])
print(foods[::2])

print(foods*2)

print(foods.append('banana'))
print(foods)
print(foods.extend(['chicken', 'sandwich']))
print(foods)
print(foods.insert(1, 'huge pizza'))
print(foods)
print(foods.pop(1))
print(foods)
print(foods.remove('banana'))
print(foods)