class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"Плейлист: {self.name}, песен: {len(self.songs)}"

    def __repr__(self):
        return f"<Playlist object, name={self.name}, songs={self.songs[0:1]}>"

    def __eq__(self, other):
        print(self.songs, other.songs)
        return self.name == other.name

    def __add__(self, other):
        new_playlist = Playlist(
            f"{self.name} {other.name}",
            self.songs + other.songs,
        )
        return new_playlist

    def __len__(self):
        return len(self.songs)

plist1 = Playlist("вайб", songs=["Песня 1", "Песня 2"])
plist2 = Playlist("вайб", songs=["Песня 3", "Песня 4"])
print(plist1)
print(repr(plist1))
print(plist2 == plist1)
plist3 = plist1 + plist2
print(plist3)
print(len(plist3))
