magicians = ['harry', 'ron', 'albus', 'draco']

def show_magicians():
    for magician in magicians:
        print(magician.title())

def make_great():
    for magician in magicians:
        magician = magicians.pop(0)
        great_magician = "great " + magician
        magicians.append(great_magician)

make_great()
show_magicians()

