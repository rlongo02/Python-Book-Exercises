colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']
colors.append('black')
colors.insert(3, 'cyan')
del colors[2]
popped_color = colors.pop(4)
colors.remove('red')
print(colors)
colors.reverse()
print(colors)
colors.reverse()
print(sorted(colors, reverse = True))
colors.sort()
print(colors)
print(len(colors))
