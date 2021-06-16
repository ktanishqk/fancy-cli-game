from map_layout import MapLayout
from location import Location
import TableIt
from plumbum import cmd


class GameEngine:
    def __init__(self, map_layout: MapLayout):
        self.map_layout = map_layout
        self.map_layout: MapLayout
        self.current_room = map_layout.get_locations()[0]
        self.current_room: Location
        self.inventory = []
        self.user_output_string: str

    def start_game(self):
        print(
            "Welcome to the Game! Your current room is " + self.current_room.get_name()
        )
        self.examine_the_room()
        self.handle_input()

    def handle_input(self):
        user_input_string = input("What would you like to do? Enter here! \n >> ")
        user_input_string = user_input_string.lower().replace(" ", "")
        if len(user_input_string) != 0:
            if user_input_string.startswith("go"):
                self.update_current_room(user_input_string.replace("go", ""))
            elif user_input_string.startswith("take"):
                self.take_item(user_input_string.replace("take", ""))
            elif "drop" in user_input_string:
                self.drop_item(user_input_string.replace("drop", ""))
            elif "quit" in user_input_string:
                self.game_finished()
            elif "examine" in user_input_string:
                self.examine_the_room()
            elif "info" in user_input_string:
                self.print_inventory()   
            else:
                print(
                    "Stop right there. That doesn't look like a valid command, wanna try again?"
                )
                if input("[y]/[n]") == "y":
                    return self.handle_input()
                else:
                    quit()

        self.examine_the_room()

    def update_current_room(self, user_input_string: str):
        if self.current_room.get_name() == self.map_layout.get_ending_room():
            game_finished()
        for direction in self.current_room.get_directions():
            if direction.get_name().replace(" ", "").lower() == user_input_string:
                self.current_room = self.map_layout.get_location_from_name(
                    direction.get_room()
                )
                self.examine_the_room()
            else:
                print("You can't go to " + user_input_string + " from here.")
        self.examine_the_room()
        self.handle_input()

    def game_finished(self):
        print("You are exiting the game now!")
        quit()
    def take_item(self, item_name: str):
        item = self.current_room.get_item_from_name(item_name)
        if item == None:
            print("Invalid Item")
        self.current_room.remove_item(item)
        self.inventory.append(item)
        self.examine_the_room()
        self.handle_input()

    def drop_item(self, item_name: str):
        item = self.current_room.get_item_from_name(item_name)
        if item == None:
            self.user_output_string = "Invalid Item"
        self.current_room.add_item(item)
        self.inventory.remove(item)
        self.examine_the_room()
        self.handle_input()

    def examine_the_room(self) -> TableIt:
        # Creating a list to make pretty tables in the terminal using TableIT
        output = [
            ["CURRENT LOCATION",""],
            ["DIRECTIONS TO GO",""],
            ["ROOMS TO GO TO",""],
            ["ITEMS IN THE ROOM",""],
        ]
        output[0][1] += self.current_room.get_name()
        for direction in self.current_room.get_directions():
            output[1][1] += "• " + direction.get_name() + " "
            output[2][1] += "• " + direction.get_room() + " "

        for item in self.current_room.get_items():
            if item is not None:
                output[3][1] += "• " + item.get_item_name() + " "
        print()        
        TableIt.printTable(output, color=(500, 100, 100, 600))
        self.handle_input()

    def print_inventory(self) -> str:
        print(f"{item.get_item_name}, " for item in self.inventory)
        self.handle_input()
