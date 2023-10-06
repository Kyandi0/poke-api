from flask import Flask, request
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
def get_specific_pokemon(id_or_name) -> dict | tuple[dict, int]:
    try:
        if id_or_name.isnumeric():
            return pokemon_fetch_service.get_pokemon_by_pokedex_number(int(id_or_name)).__dict__()
        else:
            return pokemon_fetch_service.get_pokemon_by_name(id_or_name).__dict__()
    except KeyError:
        return {"msg": f"Pokemon with path /pokemon/{id_or_name} not found"}, 404


if __name__ == '__main__':
    app.run(debug=True, port=2137)

