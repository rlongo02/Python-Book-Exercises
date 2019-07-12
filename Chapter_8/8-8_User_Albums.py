def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'album title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease recommend an album to me: ")
    print("(enter 'q' at any time to quit)")
    
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    
    album_title = input("Album title: ")
    if album_title == 'q':
        break
    
    album = make_album(artist_name, album_title)
    print("\nThanks, I'll check it out!")
    print(album)
