# set of letters
s = {'H', 'e', 'l', 'l', 'l', 'o'}

# adding 's'
s.add('e')
print('Set after updating:', s)

# Discarding element from the set
s.discard('o')
print('\nSet after updating:', s)

# Removing element from the set
s.remove('l')
print('\nSet after updating:', s)

# Popping elements from the set
print('\nPopped element', s.pop())
print('Set after updating:', s)

s.clear()
print('\nSet after updating:', s)