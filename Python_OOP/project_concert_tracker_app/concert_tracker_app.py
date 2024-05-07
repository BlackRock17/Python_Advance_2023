from project_concert_tracker_app.band import Band
from project_concert_tracker_app.band_members.drummer import Drummer
from project_concert_tracker_app.band_members.guitarist import Guitarist
from project_concert_tracker_app.band_members.singer import Singer
from project_concert_tracker_app.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN = ("Guitarist", "Drummer", "Singer")

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def __check_exist_name(self, name):
        for m in self.musicians:
            if m.name == name:
                raise Exception(f"{name} is already a musician!")

    def __find_musician_obj(self, name):
        for m in self.musicians:
            if m.name == name:
                return m

    def __find_band_obj(self, name):
        for b in self.bands:
            if b.name == name:
                return b

    def __find_concert_obj(self, place):
        for c in self.concerts:
            if c.place == place:
                return c

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")

        self.__check_exist_name(name)

        if musician_type == "Guitarist":
            new_musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            new_musician = Drummer(name, age)
        else:
            new_musician = Singer(name, age)

        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        for b in self.bands:
            if b.name == name:
                raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for c in self.concerts:
            if c.place == place:
                raise Exception(f"{c.place} is already registered for {c.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        if musician_name not in [m.name for m in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")
        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.__find_musician_obj(musician_name)
        current_band = self.__find_band_obj(band_name)

        current_band.members.append(musician)
        return f"{musician.name} was added to {current_band.name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        musician_for_remove = None

        band_ = self.__find_band_obj(band_name)

        for m in band_.members:
            if m.name == musician_name:
                musician_for_remove = m

        if not musician_for_remove:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        else:
            band_.members.remove(musician_for_remove)
            return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band_ = self.__find_band_obj(band_name)
        concert_ = self.__find_concert_obj(concert_place)
        guitarist = False
        drummer = False
        singer = False

        for inc in band_.members:
            if isinstance(inc, Guitarist):
                guitarist = True
            elif isinstance(inc, Drummer):
                drummer = True
            elif isinstance(inc, Singer):
                singer = True

        if not guitarist or not drummer or not singer:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert_type = concert_.genre

        guitarist_needed_skill = False
        drummer_needed_skill = False
        singer_needed_skill = False

        if concert_type == "Rock":
            for m in band_.members:
                if isinstance(m, Drummer) and "play the drums with drumsticks" in m.skills:
                    drummer_needed_skill = True
                elif isinstance(m, Singer) and "sing high pitch notes" in m.skills:
                    singer_needed_skill = True
                elif isinstance(m, Guitarist) and "play rock" in m.skills:
                    guitarist_needed_skill = True

        elif concert_type == "Metal":
            for m in band_.members:
                if isinstance(m, Drummer) and "play the drums with drumsticks" in m.skills:
                    drummer_needed_skill = True
                elif isinstance(m, Singer) and "sing low pitch notes" in m.skills:
                    singer_needed_skill = True
                elif isinstance(m, Guitarist) and "play metal" in m.skills:
                    guitarist_needed_skill = True

        elif concert_type == "Jazz":
            for m in band_.members:
                if isinstance(m, Drummer) and "play the drums with drum brushes" in m.skills:
                    drummer_needed_skill = True
                elif isinstance(m, Singer) and "sing low pitch notes" in m.skills \
                        and "sing high pitch notes" in m.skills:
                    singer_needed_skill = True
                elif isinstance(m, Guitarist) and "play jazz" in m.skills:
                    guitarist_needed_skill = True

        if not guitarist_needed_skill or not drummer_needed_skill or not singer_needed_skill:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert_.audience * concert_.ticket_price) - concert_.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert_type} concert in {concert_place}."














