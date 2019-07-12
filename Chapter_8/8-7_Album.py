def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'album title': title}
    if tracks:
        album['tracks'] = tracks
    return album

album = make_album('jonas brothers', 'happiness begins')
print(album)

album = make_album('coldplay', 'a head full of dreams')
print(album)

album = make_album('imagine dragons', 'night visions')
print(album)

album = make_album('green day', 'revolution radio', 12)
print(album)
