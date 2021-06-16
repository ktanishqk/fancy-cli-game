from location import Location


class MapLayout:
    def __init__(self, data: dict):
        self.starting_room = data.get("starting_room")
        self.ending_room = data.get("ending_room")
        self.locations = data.get("locations")
        for i in range(len(self.locations)):
            location = self.locations[i]
            self.locations[i] = Location(location)

    def get_starting_room(self):
        return self.starting_room

    def get_ending_room(self):
        return self.ending_room

    def get_locations(self):
        return self.locations
    def get_location_from_name(self, location_name):
        for location in self.locations:
            if location.get_name() == location_name:
                location_to_return = location
                return location_to_return
            else: 
                "Location not found!" 


