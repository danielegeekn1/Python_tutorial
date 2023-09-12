friends = ['Federica', 'Muslim', 'Gennaro', 'Radim']
lucky_numbers = [3, 9, 10, 34, 12, 6]
print(friends[1:3])
print(friends[-1])
print(friends[0])

friends[-1] = 'Francesco'
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append('Radim')
friends.insert(1, 'Simone')
print(friends)
friends.remove('Simone')
print(friends)
print(friends.index('Federica'))
friends.append('Federica')
print(friends.count('Federica'))
