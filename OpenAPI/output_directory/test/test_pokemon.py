# coding: utf-8

"""
    Pokedex API

    API for håndtering af Pokémon data ved brug af en Pandas DataFrame.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    """Pokemon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Pokemon:
        """Test Pokemon
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Pokemon`
        """
        model = Pokemon()
        if include_optional:
            return Pokemon(
                image = 'images/1.png',
                index = 1,
                name = 'Bulbasaur',
                type_1 = 'Grass',
                type_2 = 'Poison',
                total = 318,
                hp = 45,
                attack = 49,
                defense = 49,
                sp__atk = 65,
                sp__def = 65,
                speed = 45
            )
        else:
            return Pokemon(
        )
        """

    def testPokemon(self):
        """Test Pokemon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
