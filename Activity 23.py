dogs_breed = ['Aspin', 'Bulldog', 'Husky', 'Chihuahua', 'Greyhound']

print(dogs_breed)

print(dogs_breed[3])
print(dogs_breed[2 : 5])

dogs_breed.append('German Shepherd')
print(dogs_breed)

dogs_breed.pop()
print(dogs_breed)

dogs_breed.insert(3, 'American Bull')
print(dogs_breed)

dogs_breed.remove('Husky')
print(dogs_breed)

dogs_breed.sort()
print(dogs_breed)

dogs_breed.reverse()
print(dogs_breed)

print(f'You only have {len(dogs_breed)} dogs')
