class Stadion:
    def __init__(self, name, year, country, city):
        self.name = name
        self.__year = ""
        self.__country = country
        self.__city = city
        self.capacity = input("Введите вместимость стадиона: ")

    def set_year(self):
        year = input("Введите дату открытия: ")
        self.__year = year

    def get_year(self):
        return self.__year

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city


stadion = Stadion("Metallist", "2000", "RF", "Korolyov")
print(stadion.name, stadion.capacity)

stadion.set_year()
print(stadion.get_year(), stadion.get_country(), stadion.get_city())
