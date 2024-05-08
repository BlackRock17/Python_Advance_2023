from project.player import Player


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        player_names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                player_names.append(player.name)

        return f"Successfully added: {', '.join(player_names)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player(player_name)

        if player is None:
            return

        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        idx, supply = self.__find_supply(sustenance_type)

        if supply is None:
            return f"There are no {sustenance_type.lower()} supplies left!"

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        player.stamina = min(player.stamina + supply.energy, Player.MAX_STAMINA)
        self.supplies.pop(idx)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = self.__find_player(first_player_name)
        player_two = self.__find_player(second_player_name)
        res = []
        if player_one.stamina == 0:
            res.append(f"Player {player_one.name} does not have enough stamina.")
        if player_two.stamina == 0:
            res.append(f"Player {player_two.name} does not have enough stamina.")

        if res:
            return "\n".join(res)

        if player_one.stamina > player_two.stamina:
            player_one, player_two = player_two, player_one

        player_one_damage = player_one.stamina / 2
        player_two.stamina = max(player_two.stamina - player_one_damage, 0)
        if player_two.stamina == 0:
            return f"Winner: {player_one.name}"

        player_two_damage = player_two.stamina / 2
        player_one.stamina = max(player_one.stamina - player_two_damage, 0)
        if player_one.stamina == 0:
            return f"Winner: {player_two.name}"

        winner = player_one if player_one.stamina > player_two.stamina else player_two
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        res = []

        for player in self.players:
            res.append(str(player))

        for supply in self.supplies:
            res.append(supply.details())

        return "\n".join(res)

    def __find_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return p

    def __find_supply(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, - 1, - 1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return idx, supply

        return -1, None




