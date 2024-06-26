from project_F1_PA.formula_teams.mercedes_team import MercedesTeam
from project_F1_PA.formula_teams.red_bull_team import RedBullTeam
from project_F1_PA.formula_teams.formula_team import FormulaTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name, budget):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        winer = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"
        revenue_red_bull = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        revenue_mercedes = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {revenue_red_bull}. " \
               f"Mercedes: {revenue_mercedes}. " \
               f"{winer} is ahead at the {race_name} race."


