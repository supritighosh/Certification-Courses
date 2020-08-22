#Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites
# if they are both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = zip(l1, l2)
print(l3)
opposites = list(filter(lambda s: len(s[0]) > 3 and len(s[1]) > 3, l3))
print(opposites)
