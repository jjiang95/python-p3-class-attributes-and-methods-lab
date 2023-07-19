class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_count()
        Song.add_artist(self.artist)
        Song.add_genre(self.genre)
        Song.add_genre_count(self.genre)
        Song.add_artist_count(self.artist)
    
    @classmethod
    def add_count(cls, increment=1):
        cls.count += increment
    
    @classmethod
    def add_artist(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            return

    @classmethod
    def add_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1 
    
    @classmethod
    def add_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
