from random import randint

value = randint(1,3)
if value == 1:
    alien_color = 'green'
elif value == 2:
    alien_color = 'yellow'
else:
    alien_color = 'red'
  
if alien_color == 'green':
    print('You earned five points for shooting a green alien!')
elif alien_color == 'yellow':
    print("You earned ten points for shooting a yellow alien!")
else:
    print('You earned fifteen points for shooting a red alien!')
