class Item:
    def __init__(self, item: dict):
        if len(item) != 0:
            self.item_name = item.get("name")
            self.description = item.get("description")
            self.damage = int(item.get("damage"))
            self.range = int(item.get("range"))
            self.accuracy = int(item.get("accuracy"))
