from project_concert_tracker_app.band_members.musician import Musician

SKILLS_FOR_LEARN = ("play the drums with drumsticks", "play the drums with drum brushes", "read sheet music")


class Drummer(Musician):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.SKILLS_FOR_LEARN = SKILLS_FOR_LEARN

    #def learn_new_skill(self, new_skill):
        #pass