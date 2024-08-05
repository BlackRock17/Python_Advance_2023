from project_h.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    INCREASES_SPEED = 2

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + self.INCREASES_SPEED, self.MAX_SPEED)
