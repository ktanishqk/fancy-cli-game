from directions import Directions
from item import Item


class Location:
    def __init__(self, location: dict):
        self.name = location.get("name")
        self.name: str
        self.description = location.get("description")
        self.description: str
        self.items = location.get("item")
        if self.items != None:
            for i in range(len(self.items)):
                item = self.items[i]
                self.items[i] = Item(item)
        self.directions = location.get("directions")
        for i in range(len(self.directions)):
            direction = self.directions[i]
            self.directions[i] = Directions(direction)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_directions(self):
        return self.directions

    def get_items(self):
        return self.items

    def get_item_from_name(self, item_name: str):
        item_from_name = next(item for item in self.items if item_name == item.name)
        return item_from_name

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)
