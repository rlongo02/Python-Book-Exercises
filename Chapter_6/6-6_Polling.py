friends = ['erin', 'jen', 'kevin', 'larry', 'sarah', 'edward', 'john', 'phil']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
for friend in friends:        
    if friend in favorite_languages.keys():
        print(friend.title() + ", thank you for taking the poll.")
    elif friend not in favorite_languages.keys():
        print(friend.title() + ", please take our poll!")
