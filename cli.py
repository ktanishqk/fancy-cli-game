from plumbum import cli
import json
from map_layout import MapLayout
from game_engine import GameEngine
import pyfiglet


class RPGame(cli.Application):
    def print_name(self):
        print(pyfiglet.figlet_format("ADVENTURE RPG", font="slant"))

    def main(self):
        self.print_name()
        with open("map_json.json") as file:
            data = json.load(file)
        map_layout = MapLayout(data)
        game_engine = GameEngine(map_layout)
        game_engine.start_game()


if __name__ == "__main__":
    RPGame()
