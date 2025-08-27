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

# Create three album dictionaries
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Nirvana', 'Nevermind')
album3 = make_album('Pink Floyd', 'The Dark Side of the Moon', num_songs=10)

# Print the album dictionaries
print(album1)
print(album2)
print(album3)
