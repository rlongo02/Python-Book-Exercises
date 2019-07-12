sandwich_orders = ['philly cheesesteak', 'pastrami', 'italian deluxe', 'pastrami', 'chicken philly', 'pastrami', 'chicken buffalo']
finished_sandwiches = []
print("Unfortunately, the deli has run out of pastrami, so Pastrami sandwich orders cannot be finished.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while len(sandwich_orders) > 0:
    popped = sandwich_orders.pop()
    print("\nI finished your " + popped.title() + ".")
    finished_sandwiches.append(popped)

print("\nThe following sandwiches were made today:")
for finished in finished_sandwiches:
    print(finished.title())
