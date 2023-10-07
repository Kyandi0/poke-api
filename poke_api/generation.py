from typing import List
from poke_api.pokemon import Pokemon


class PokemonGeneration:
    def __init__(self, gen_number: int, pokemon: List[Pokemon]):
        self.gen_number = gen_number
        self.pokemon = pokemon

    def __dict__(self) -> dict:
        return {
            "gen_number": self.gen_number,
            "pokemon": [
                pokemon.__dict__()
                for pokemon in self.pokemon
            ]
        }
