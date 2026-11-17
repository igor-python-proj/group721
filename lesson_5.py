# Магические методы
# Магические (dunder) методы - методы с "__" в имени, которые Python вызывает сам,
# а не мы напрямую: они задают поведение объекта в обычных операциях.

class Playlist:
    # __init__ тоже магический метод: Python вызывает его автоматически при создании объекта
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    # Python вызывает __str__ при print(obj) и str(obj); без него выведется <object at 0x...>
    def __str__(self):
        return f"Плейлист: {self.name}, песен: {len(self.songs)}"

    # __repr__ - отладочное представление для repr(obj) и консоли;
    # в отличие от __str__ оно рассчитано на разработчика, а не на пользователя
    def __repr__(self):
        return f"<Playlist object, name={self.name}, songs={self.songs[0:1]}>"

    # Python вызывает __eq__ при сравнении через ==; без него == сравнивает адреса объектов
    def __eq__(self, other):
        print(self.songs, other.songs)  # печать для наглядности: видно, какие списки сравниваются
        return self.name == other.name

    # Python вызывает __add__ при сложении через +; возвращается новый объект, исходные не меняются
    def __add__(self, other):
        new_playlist = Playlist(
            f"{self.name} {other.name}",
            self.songs + other.songs,
        )
        return new_playlist

    # Python вызывает __len__ при len(obj); метод должен вернуть целое число
    def __len__(self):
        return len(self.songs)


plist1 = Playlist("вайб", songs=["Песня 1", "Песня 2"])
plist2 = Playlist("вайб", songs=["Песня 3", "Песня 4"])
print(plist1)             # __str__
print(repr(plist1))       # __repr__
print(plist2 == plist1)   # __eq__
plist3 = plist1 + plist2 + plist1 # __add__ # обратная Польская нотация
print(plist3)             # __str__
print(len(plist3))        # __len__