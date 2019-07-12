guestList = ['alexander hamilton', 'thomas jefferson', 'james madison']
invite = ', you are cordially invited to dinner.'
print(guestList[0].title() + invite)
print(guestList[1].title() + invite)
print(guestList[2].title() + invite)
print('')
print('Unfortunately, ' + guestList[0].title() + ' cannot make it to dinner.')
del guestList[0]
print('')
print(guestList[0].title() + invite)
print(guestList[1].title() + invite)
