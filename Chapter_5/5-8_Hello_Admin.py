usernames = ['john', 'betty', 'admin', 'mark', 'phyllis']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to access advanced options?")
    else:
        print("Hello " + username.title() + ", thank you for logging in.")
