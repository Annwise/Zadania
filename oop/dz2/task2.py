class Film:
    def __init__(self, name, genre, director, actor):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = input("Введите год выпуска фильма: ")
        self.actor = actor

    def play(self):
        return "Смотрим фильм"


class Comedy(Film):
    def buy(self):
        return "Оплачена подписка"


film = Film("Interstellar", "Fantastik", "Nolan", "McConaughey")
print(film.play(), film.name)
film1 = Comedy("Home Alone", "Family", "Columbus", "Culkin")
print(film1.buy())
