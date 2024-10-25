# coding: utf-8

"""
    Pokedex API

    API for håndtering af Pokémon data ved brug af en Pandas DataFrame.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.add_data200_response import AddData200Response

class TestAddData200Response(unittest.TestCase):
    """AddData200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddData200Response:
        """Test AddData200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddData200Response`
        """
        model = AddData200Response()
        if include_optional:
            return AddData200Response(
                message = 'New entry added successfully'
            )
        else:
            return AddData200Response(
        )
        """

    def testAddData200Response(self):
        """Test AddData200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
