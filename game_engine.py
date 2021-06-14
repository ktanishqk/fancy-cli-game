from map_layout import MapLayout
from location import Location
import TableIt

class GameEngine:
    def __init__(self, map_layout: MapLayout):
        self.map_layout = map_layout
        self.map_layout: MapLayout
        self.current_room = map_layout.get_locations()[0]
        self.current_room: Location
        self.inventory = []
        self.user_output_string: str
        self.examine_the_room()

    # def start_game(self):
        # print(self.map_layout.get_locations())

    def handle_input(self, user_input_string: str):
        user_input_string = user_input_string.lower().replace("\\s", "")
        if len(user_input_string) != 0:
            if user_input_string.startswith("go"):
                update_current_room(user_input_string.replace("go", ""))
            if user_input_string.startswith("take"):
                update_current_room(user_input_string.replace("take", ""))
            # elif "drop" in user_input_string:

    def update_current_room(self, user_input_string: str):
        if self.current_room.get_name == self.map_layout.get_ending_room:
            game_finished()

    def game_finished(self):
        self.user_output_string = "You have completed the game"

    def drop_item(self, item_name: str):
        item = self.current_room.get_item_from_name(item_name)
        if item == None:
            self.user_output_string = "Invalid Item"
        self.current_room.add_item(item)
        self.inventory.remove(item)

    def examine_the_room(self):

        self.user_output_string = (
            "Your current location is "
            + self.current_room.get_name()
            + "\n"
            + "From here you can go: \n"
            + "directions, room - "
        )
        for direction in self.current_room.get_directions():
            self.user_output_string += f"{direction.get_name()}" + f", {direction.get_room()}"
        self.user_output_string += "\n Items Visible: "  
        print(self.user_output_string)
