from directions import Directions
class Location:
    def __init__(self, location: dict):            
        self.name = location.get('name')
        self.description = location.get('description')
        self.items = location.get('item')
        self.directions = location.get('directions')
        for i in range(len(self.directions)):
            direction = self.directions[i]
            print(direction)
            self.directions[i] = Directions(direction)
            

    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_directions(self):
        return self.directions
