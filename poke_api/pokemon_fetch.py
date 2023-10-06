from typing import List
import requests
from bs4 import BeautifulSoup
from poke_api.pokemon import Pokemon


class PokemonFetchService:

    def get_pokemon_by_pokedex_number(self, pokedex_number: int) -> Pokemon:
        pokemon_list = self.get_all_pokemon()
        for pokemon in pokemon_list:
            if pokemon.pokedex_number == pokedex_number:
                return pokemon
        raise KeyError(f"Pokemon with id {pokedex_number} not found")

    def get_pokemon_by_name(self, name: str) -> Pokemon:
        pokemon_list = self.get_all_pokemon()
        for pokemon in pokemon_list:
            if pokemon.name == name:
                return pokemon
        raise KeyError(f"Pokemon with name {name} not found")

    def get_all_pokemon(self) -> List[Pokemon]:
        soup = self.__get_pokemon_soup()

        pokemon_names = []
        pokemon_list = []
        generation_tables = soup.select("table.roundy")
        generation = 0

        for table in generation_tables:
            generation += 1

            for row in table.select("tr")[1:]:
                pokemon_name = row.select("td")[2].select_one("a").text
                if pokemon_name in pokemon_names:
                    continue
                else:
                    pokemon_names.append(pokemon_name)

                has_secondary_type = len(row.select("td")) > 4
                pokemon_nr_text = row.select("td")[0].text.replace("#", "")

                if pokemon_nr_text == "":
                    continue

                pokemon_nr = int(pokemon_nr_text)
                pokemon_img = "https:" + row.select("td")[1].select_one("a img").attrs["src"]
                pokemon_type_primary = row.select("td")[3].select_one("a span").text

                if has_secondary_type:
                    pokemon_type_secondary = row.select("td")[4].select_one("a span").text
                else:
                    pokemon_type_secondary = None

                pokemon = Pokemon(pokemon_nr, pokemon_name, generation, pokemon_type_primary, pokemon_type_secondary,
                                  pokemon_img)
                pokemon_list.append(pokemon)

        return pokemon_list

    @staticmethod
    def __get_pokemon_soup():
        bulbapedia_endpoint = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number"
        bulbapedia_response = requests.get(bulbapedia_endpoint)
        bulbapedia_html = bulbapedia_response.text
        soup = BeautifulSoup(bulbapedia_html, 'html.parser')
        return soup
