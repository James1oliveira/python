def make_album(artist_name, album_title, num_songs=None):
    """
    Build a dictionary describing a music album.
    If num_songs is provided, include it in the dictionary.
    """
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

while True:
    print("\nEnter album information (or 'q' to quit):")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Album title: ")
    if title.lower() == 'q':
        break

    # Optional: ask for number of songs, user can skip by pressing Enter
    num_songs_input = input("Number of songs (press Enter to skip): ")
    if num_songs_input.lower() == 'q':
        break
    elif num_songs_input.isdigit():
        num_songs = int(num_songs_input)
    else:
        num_songs = None

    album = make_album(artist, title, num_songs)
    print("\nAlbum info created:")
    print(album)
