from typing import Union
from flask import Flask
from poke_api.pokemon_fetch import PokemonFetchService

app = Flask(__name__)
pokemon_fetch_service = PokemonFetchService()


@app.route('/pokemon', methods=['GET'])
def get_all_pokemon() -> list:
    return [
        pokemon.__dict__()
        for pokemon in pokemon_fetch_service.get_all_pokemon()
    ]


@app.route('/pokemon/<id_or_name>', methods=['GET'])
def get_specific_pokemon(id_or_name) -> Union[dict, tuple[dict, int]]:
    try:
        if id_or_name.isnumeric():
            return pokemon_fetch_service.get_pokemon_by_pokedex_number(int(id_or_name)).__dict__()
        else:
            return pokemon_fetch_service.get_pokemon_by_name(id_or_name).__dict__()
    except KeyError:
        return {"msg": f"Pokemon with path /pokemon/{id_or_name} not found"}, 404


@app.route('/generations', methods=['GET'])
def get_all_generations() -> list:
    return [
        generation.__dict__()
        for generation in pokemon_fetch_service.get_all_generations()
    ]


@app.route('/generations/<gen_number>', methods=['GET'])
def get_specific_generation(gen_number: int) -> Union[dict, tuple[dict, int]]:
    try:
        gen_number = int(gen_number)
        return pokemon_fetch_service.get_generation_by_gen_number(gen_number).__dict__()
    except IndexError:
        return {"msg": f"Generation with path /generations/{gen_number} not found"}, 404
    except ValueError:
        return {"msg": f"Invalid generation number: {gen_number}"}, 400


if __name__ == '__main__':
    app.run(debug=True, port=2137)

