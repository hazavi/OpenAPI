from fastapi import FastAPI, HTTPException
from typing import List
from openapi_client.api import DefaultApi
from openapi_client.models import Pokemon
from openapi_client import ApiClient  # Make sure to import the ApiClient

app = FastAPI()

# Replace 'https://example.com/api' with the actual base URL of your Pokémon API
api_client = ApiClient(base_url='http://localhost:8000')  
pokedex_api = DefaultApi(api_client=api_client)

@app.get("/data", response_model=List[Pokemon], summary="Hent alle Pokémon data")
def get_data():
    try:
        response = pokedex_api.get_data()  # Call the method to fetch data
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
