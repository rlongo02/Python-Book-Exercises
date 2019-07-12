magicians = ['harry', 'ron', 'albus', 'draco']
copy_magicians = magicians[:]

def show_magicians(group):
    for magician in group:
        print(magician.title())

def make_great(group):
    for magician in group:
        magician = group.pop(0)
        great_magician = "great " + magician
        group.append(great_magician)

make_great(copy_magicians)

print("Great List:")
show_magicians(copy_magicians)

print('')

print('Unchanged List:')
show_magicians(magicians)
