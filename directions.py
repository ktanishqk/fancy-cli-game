class Directions:
    def __init__(self, direction: dict):
        self.name = direction["directionName"]
        self.room = direction["room"]

    def get_name(self):
        return self.name

    def get_room(self):
        if self.room == "TRAP":
            return "SECRET PLACE"    
        return self.room
