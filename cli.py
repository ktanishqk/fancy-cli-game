from plumbum import cli
import json
from map_layout import MapLayout
from game_engine import GameEngine
import pyfiglet


class RPGame(cli.Application):
    """ The base class handling the initialization of the game and formation of a Game Engine object. """
    def print_name(self):
        # Uses pyfiglet to print the name of the game 
        print(pyfiglet.figlet_format("ADVENTURE RPG", font="slant", justify = "right"))

    def main(self):
        self.print_name()
        # Deserializing the json here
        with open("map_json.json") as file:
            data = json.load(file)
        # Handles all deserialization and handles object decomposition for the same   
        map_layout = MapLayout(data)
        game_engine = GameEngine(map_layout)
        game_engine.start_game()


if __name__ == "__main__":
    RPGame()
