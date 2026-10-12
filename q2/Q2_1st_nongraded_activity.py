class PSHS_Galaxy:
    def __init__(self, living, location, galaxy):
        self.living = living
        self.location = location
        self.galaxy = galaxy

    def get_location(self):
        return f"Is living in {self.location} of {self.galaxy} galaxy."

    def get_galaxy(self):
        return f"Is living in {self.galaxy} galaxy."

    def get_living(self):
        return f"Is living in {self.living}."


class Nationality(PSHS_Galaxy):
    def __init__(self, living, location, galaxy, nationality):
        super().__init__(living, location, galaxy)
        self.nationality = nationality

    def get_nationality(self):
        return f"Is a {self.nationality} living in {self.location} of {self.galaxy} galaxy."


class Filipino(Nationality):
    def __init__(self, living, location, galaxy, nationality, language):
        super().__init__(living, location, galaxy, nationality)
        self.language = language

    def get_language(self):
        return f"Speaks {self.language} language."

    def get_full_info(self):
        return self.get_nationality() + " " + self.get_language()


class Indonesian(Nationality):
    def __init__(self, living, location, galaxy, nationality, language):
        super().__init__(living, location, galaxy, nationality)
        self.language = language

    def get_language(self):
        return f"Speaks {self.language} language."

    def get_full_info(self):
        return self.get_nationality() + " " + self.get_language()


class Spaniards(Nationality):
    def __init__(self, living, location, galaxy, nationality, language):
        super().__init__(living, location, galaxy, nationality)
        self.language = language

    def get_language(self):
        return f"Speaks {self.language} language."

    def get_full_info(self):
        return self.get_nationality() + " " + self.get_language()


class Alien(PSHS_Galaxy):
    def __init__(self, living, location, galaxy, species):
        super().__init__(living, location, galaxy)
        self.species = species

    def get_species(self):
        return f"Is a {self.species} living in {self.location} of {self.galaxy} galaxy."


class Marvels(Alien):
    def __init__(self, living, location, galaxy, species, superpower):
        super().__init__(living, location, galaxy, species)
        self.superpower = superpower

    def get_superpower(self):
        return f"Has a superpower of {self.superpower}."

    def get_full_info(self):
        return self.get_species() + " " + self.get_superpower()


class Avengers(Alien):
    def __init__(self, living, location, galaxy, species, superpower):
        super().__init__(living, location, galaxy, species)
        self.superpower = superpower

    def get_superpower(self):
        return f"Has a superpower of {self.superpower}."

    def get_full_info(self):
        return self.get_species() + " " + self.get_superpower()


popoo = Filipino("Yes", "Philippines", "Milky Way", "Filipino", "Filipino")
oahq = Indonesian("Yes", "Indonesia", "Milky Way", "Indonesian", "Indonesian")
The_locust = Alien("Yes", "Mars", "Milky Way", "Alien")

print(popoo.get_full_info())
print(oahq.get_full_info())
print(The_locust.get_species())


        


