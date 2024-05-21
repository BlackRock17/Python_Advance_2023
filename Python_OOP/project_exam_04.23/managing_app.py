from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPE = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in [u.driving_license_number for u in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPE.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [v.license_plate_number for v in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VALID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)

        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length > length:
                r.is_locked = True

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number,self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicle = [v for v in self.vehicles if v.is_damaged]
        vehicle_for_repair = {}
        for v in damaged_vehicle:
            vehicle_for_repair[v] = [v.brand, v.model]

        sorted_vehicle = dict(sorted(vehicle_for_repair.items(), key=lambda x: (x[1][0], x[1][1])))
        count_of_repaired_vehicles = 0
        if count > 0:
            counter = count
            for v in sorted_vehicle.keys():
                v.change_status()
                v.recharge()
                counter -= 1
                count_of_repaired_vehicles += 1
                if counter == 0:
                    break

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***\n"
        users = {}
        for user in self.users:
            users[user] = user.rating

        for u, v in dict(sorted(users.items(), key=lambda x: -x[1])).items():
            result += str(u) + "\n"

        return result.strip()








