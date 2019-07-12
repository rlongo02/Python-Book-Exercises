alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow', 'health': 100}
alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'medium', 'health': 200}
alien_2 = {'color': 'red', 'points': 15, 'speed': 'fast', 'health': 300}

alien_army = [alien_0, alien_1, alien_2]

a = 1
for alien in alien_army:
    print("Alien #" + str(a))
    print("This alien is " + alien['color'] + ". It is worth " + str(alien['points']) + " points.")
    print("It moves at a " + alien['speed'] + " speed and has " + str(alien['health']) + " health.\n")
    a+=1
