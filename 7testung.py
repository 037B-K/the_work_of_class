import random


class NPC:
    def __init__(self, name, job, race, espece):
        self.force = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.agilite = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.constitution = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.intelligence = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.sagesse = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.charisme = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.armor = random.randint(1, 12)
        self.pt_de_vie = random.randint(1, 20)
        self.nom = name
        self.job = job
        self.race = race
        self.espece = espece

    def show_stats(self):
        print("Force: ", self.force, "\nAgilite: ", self.agilite, "\nConstitution: ", self.constitution,
              "\nIntelligence: ",
              self.intelligence, "\nSagesse: ", self.sagesse, "\nCharisme: ", self.charisme, "\nClasse d'armure: ",
              self.armor,
              "\nPoints de vie: ", self.pt_de_vie, "\nNom: ", self.nom, "\nProfession: ", self.job, "\nRace: ",
              self.race,
              "\nEspece: ", self.espece)


class Kobold(NPC):
    def __init__(self, name, job, race, espece):
        super().__init__(name, job, race, espece)


    def attack(self, person):
        print(person, " is my enemy")


