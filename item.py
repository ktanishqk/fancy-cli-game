class Item:
    def __init__(self, item: dict):
    
        self.item_name = item.get("itemName")
        self.description = item.get("description")
        self.damage = int(item.get("damage"))
        self.range = int(item.get("range"))
        self.accuracy = int(item.get("accuracy"))

    def get_item_name(self):
        return self.item_name  

    def get_description(self):
        return self.description

    def get_damage(self):
        return self.damage

    def get_range(self):
        return self.range

    def get_accuracy(self):
        return self.accuracy
