sandwich_orders = ['philly cheesesteak', 'italian deluxe', 'chicken philly', 'chicken buffalo']
finished_sandwiches = []

while len(sandwich_orders) > 0:
    popped = sandwich_orders.pop()
    print("\nI finished your " + popped.title() + ".")
    finished_sandwiches.append(popped)

print("\nThe following sandwiches were made today:")
for finished in finished_sandwiches:
    print(finished.title())
