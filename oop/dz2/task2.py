class Film:
    def __init__(self, name, genre, year, director, actor):
        self.name = name
        self.genre = genre
        self.year = year
        self.director = director
        self.actor = actor

    def play(self):
        return "Смотрим фильм"

film = Film("Interstellar", "Fantastik", "2014", "Nolan", "McConaughey")
print(film.play(), film.name)
