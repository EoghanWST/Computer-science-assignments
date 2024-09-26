counts = {} # create a dictionary
counts2 = dict({}) # create a dictionary
print(counts)
print(counts2)
# to add a key value pair
counts['games'] = 24
print(counts)
counts['players']= 200
print(counts)
#To fins the number of lines in a dictionary

if 'players' in counts:#boolen counts
    print('players found')
if 'managers' not in counts:#return true or false
    print('managers not found')
#to print a value
print(counts['games']) # returns games value - returns error if no key
print(counts)
print(counts.get('games')) # returns games value - returns none if no key
print(counts)
print(counts.pop('games')) # returns games value - remove item from list
print(counts)
for key in counts.keys():
    print(key)
for keys in counts:
    print(keys)#WILL PRINT THE KEYS IN DICTIONARY
for values in counts.values():
    print(values) # will print the values in dictionary
for keys,value in counts.items():
    print(f'{key} -- {value}')

 