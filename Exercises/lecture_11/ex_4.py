"""
Briefly describe a possible collection of classes which can be used to represent a music collection
(for example, inside a music player), focusing on how they would be related by composition.
You should include classes for songs, artists, albums and playlists.
Hint: write down the four class names, draw a line between each pair of classes which you think should have a
relationship, and decide what kind of relationship would be the most appropriate.

For simplicity you can assume that any song or album has a single “artist” value (which could represent more than one
person), but you should include compilation albums (which contain songs by a selection of different artists).
The “artist” of a compilation album can be a special value like “Various Artists”.
You can also assume that each song is associated with a single album, but that multiple copies of the same song
(which are included in different albums) can exist.
Write a simple implementation of this model which clearly shows how the different classes are composed.
Write some example code to show how you would use your classes to create an album and add all its songs to a playlist.
Hint: if two objects are related to each other bidirectionally, you will have to decide how this link should be formed –
one of the objects will have to be created before the other, so you can’t link them to each other in both directions
simultaneously!
"""

"""
Outline:

Classes:
Song - belongs to an album (can belong to more than one album), performed by artist, part of a playlist
Artist - performs songs and albums.
Album - belongs to one or more (compilation) artists. If it's a compilation album - the album artist is 'Various', but each song has their own Artist.
Playlist - contains songs. regardless of albums \ artists.
"""


class Playlist:
    def __init__(self, name, songs=None):
        self.songlist = []
        self.name = name

        if songs is not None:
            if isinstance(songs, list):
                for song in songs:
                    self.add_song(song)
            else:
                self.add_song(songs)

    def add_song(self, song):
        assert isinstance(song, Song), 'song must be of Song type or a list of Song types, got {}'.format(type(song))
        self.songlist.append(song)


class Artist:
    def __init__(self, name):
        self.name = name


class Song:
    artist = None

    def __init__(self, name, artist=None):
        self.name = name
        if artist is not None:
            self.set_artist(artist)

    def set_artist(self, artist):
        self.artist = artist

    def get_artist(self):
        return self.artist


class Album(Playlist):

    def __init__(self, name, artist=None):
        super(Album, self).__init__(name=name)
        self.album_artist = artist if artist is not None else set()

    def set_album_artist(self):
        artist_set = self.album_artist
        if len(self.songlist):
            for song in self.songlist:
                artist_set |= {song.get_artist().name}
        if len(artist_set) == 1:
            self.album_artist = list(artist_set)[0]
        else:
            self.album_artist = 'Various'

# Initialize songs
song1 = Song('Yesterday', Artist('Beatles'))
song2 = Song('November Rain', Artist('GnR'))
song3 = Song('Jeremy', Artist('Pearl Jam'))
song4 = Song('Hey Jude', Artist('Beatles'))
song5 = Song('Paradise City', Artist('GnR'))

# Initialize albums
album1 = Album('Beatles Greatest Hits')
album1.add_song(song1)
album1.add_song(song4)
album1.set_album_artist()

album2 = Album('GnR Live')
album2.add_song(song2)
album2.add_song(song5)
album2.set_album_artist()

album3 = Album('Pearl Jam and Friends')
album3.add_song(song3)
album3.add_song(song4)
album3.add_song(song5)
album3.set_album_artist()

# Initialize playlist
playlist1 = Playlist('Songs I Like', songs=[song1, song2, song3, song4, song5])

# test
assert album1.album_artist == 'Beatles'
assert album2.album_artist == 'GnR'
assert album3.album_artist == 'Various'

# a more detailed solution is here:
# http://python-textbok.readthedocs.io/en/latest/Object_Oriented_Programming.html#answer-to-exercise-1







