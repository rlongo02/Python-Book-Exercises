from random import randint

value = randint(1,3)
if value == 1:
    alien_color = 'green'
elif value == 2:
    alien_color = 'yellow'
else:
    alien_color = 'red'

print(alien_color.title())    
if alien_color == 'green':
    print('You earned five points for shooting a green alien!')
else:
    print("You earned ten points for shooting a non-green alien!")
