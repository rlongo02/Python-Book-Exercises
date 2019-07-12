guestList = ['alexander hamilton', 'thomas jefferson', 'james madison']
invite = ', you are cordially invited to dinner.'
print(guestList[0].title() + invite)
print(guestList[1].title() + invite)
print(guestList[2].title() + invite)
print('')

print('Unfortunately, ' + guestList[0].title() + ' cannot make it to dinner.')
del guestList[0]

print('Also, I happened to find a larger dinner table online, so I can invite three new guests.')
print('')

guestList.insert(0, 'aaron burr')
guestList.insert(2, 'george washington')
guestList.append('john adams')
print(guestList[0].title() + invite)
print(guestList[1].title() + invite)
print(guestList[2].title() + invite)
print(guestList[3].title() + invite)
print(guestList[4].title() + invite)
print('')

print("Oh, darn! My new table won't arrive in time for dinner, so I can only invite two people.")
print('')

uninvited_1 = guestList.pop(0)
print("I'm sorry, " + uninvited_1.title() + ", but I can no have you for dinner.")
uninvited_2 = guestList.pop(2)
print("I'm sorry, " + uninvited_2.title() + ", but I can no have you for dinner.")
uninvited_3 = guestList.pop(-1)
print("I'm sorry, " + uninvited_3.title() + ", but I can no have you for dinner.")
print('')

invite = ", don't worry! You're still invited to dinner."
print(guestList[0].title() + invite)
print(guestList[1].title() + invite)
del guestList[0]
del guestList[0]
print(guestList)
