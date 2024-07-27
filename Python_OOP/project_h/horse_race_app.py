from project_h.horse_race import HorseRace
from project_h.horse_specification.appaloosa import Appaloosa
from project_h.horse_specification.thoroughbred import Thoroughbred
from project_h.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_BREEDS = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        for h in self.horses:
            if h.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_BREEDS:
            self.horses.append(HorseRaceApp.VALID_HORSE_BREEDS[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        for j in self.jockeys:
            if j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        for r in self.horse_races:
            if r.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        try:
            jockey = list(filter(lambda j: j.name == jockey_name, self.jockeys))[0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        try:
            horse_race = list(filter(lambda r: r.race_type == race_type, self.horse_races))[0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = list(filter(lambda j: j.name == jockey_name, self.jockeys))[0]
        except IndexError:
            Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        try:
            horse_race = list(filter(lambda r: r.race_type == race_type, self.horse_races))[0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner = ""


        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner = jockey


        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."
