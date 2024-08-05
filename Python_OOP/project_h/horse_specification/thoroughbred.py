from project_h.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    INCREASES_SPEED = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + self.MAX_SPEED, self.MAX_SPEED)

