from plumbum import cli
import json
from map_layout import MapLayout

class RPGame(cli.Application):
    def main(self):
        with open('map_json.json') as file:
            data = json.load(file)
        map_layout = MapLayout(data)

        #file = json.loads('map_json.json', r)
if __name__ == "__main__":
    RPGame()