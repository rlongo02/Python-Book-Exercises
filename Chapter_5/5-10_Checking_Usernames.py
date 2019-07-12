current_users = ['jim', 'kevin', 'tiffany', 'christine', 'erin']
new_users = ['jeffrey', 'kane', 'Jim', 'keVIn', 'lauren']

for user in new_users:
    if user.lower() in current_users:
        print("Username "+user+" in use. Please choose a new one.")
    else:
        print("Username "+user+" available. Welcome!")
