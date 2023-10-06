from typing import Optional


class Pokemon:
    def __init__(self, pokedex_number: int, name: str, generation: int, type_primary: str, type_secondary: Optional[str], image: str):
        self.pokedex_number = pokedex_number
        self.name = name
        self.generation = generation
        self.type_primary = type_primary
        self.type_secondary = type_secondary
        self.image = image

    def __str__(self) -> str:
        return f"{self.name} - {self.generation}"

    def __dict__(self) -> dict:
        return {
            "pokedex_number": self.pokedex_number,
            "name": self.name,
            "generation": self.generation,
            "type_primary": self.type_primary,
            "type_secondary": self.type_secondary,
            "image": self.image
        }
