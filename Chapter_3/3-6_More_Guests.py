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

