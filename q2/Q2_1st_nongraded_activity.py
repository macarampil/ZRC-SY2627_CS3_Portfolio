class PSHS_Galaxy:
    def __init__(self, living, location, galaxy):
        self.living = living
        self.location = location
        self.galaxy = galaxy

class Nationality(PSHS_Galaxy):
    def __init__(self, living, location, galaxy, nationality):
        super().__init__(living, location, galaxy)
        self.nationality = nationality

    def get_nationality(self):
        return f"Is a {self.nationality} living in {self.location} of {self.galaxy} galaxy."

    def get_location(self):
        return f"Is living in {self.location} of {self.galaxy} galaxy."

    def get_galaxy(self):
        return f"Is living in {self.galaxy} galaxy."

    def get_living(self):
        return f"Is living in {self.living}."


class Filipino(Nationality):
    def __init__(self, living, location, galaxy, nationality, language):
        super().__init__(living, location, galaxy, nationality)
        self.language = "Filipino"

    def get_language(self):
        return f"Speaks {self.language} language."


class Indonesian(Nationality):
    def __init__(self, living, location, galaxy, nationality, language):
        super().__init__(living, location, galaxy, nationality)
        self.language = "Indonesian"

    def get_language(self):
        return f"Speaks {self.language} language."

class Spaniards(Nationality):
    def __init__(self, living, location, galaxy, nationality, language):
        super().__init__(living, location, galaxy, nationality)
        self.language = "Spanish"

    def get_language(self):
        return f"Speaks {self.language} language."

class Alien(PSHS_Galaxy):
    def __init__(self, living, location, galaxy, species):
        super().__init__(living, location, galaxy)
        self.species = "Alien"

    def get_species(self):
        return f"Is a {self.species} living in {self.location} of {self.galaxy} galaxy."


class Marvels(Alien):
    def __init__(self, living, location, galaxy, species, superpower):
        super().__init__(living, location, galaxy, species)
        self.superpower = "Strong"

    def get_superpower(self):
        return f"Has a superpower of {self.superpower}."

class Avengers(Alien):
    def __init__(self, living, location, galaxy, species, superpower):
        super().__init__(living, location, galaxy, species)
        self.superpower = "Fast"

    def get_superpower(self):
        return f"Has a superpower of {self.superpower}."

meow = Avengers("Alien", "Mars", "Milky Way", "Alien", "Fast")
popoo = Nationality("Human", "Earth", "Milky Way", "Filipino")

print(popoo.get_nationality())
print(popoo.get_location())
print(popoo.get_galaxy())
print(meow.get_species())
print(meow.get_superpower())


        


