import os
import sys
import pandas as pd
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

# Append the path to the output directory to the system path
output_directory = os.path.join(os.path.dirname(__file__), 'output_directory')
sys.path.append(output_directory)

app = FastAPI()

# Load Pokémon data from a CSV file
def load_pokemon_data():
    try:
        df = pd.read_csv('pokedex.csv')  # Adjust path as needed
        return df  # Return the DataFrame directly for further manipulation
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading data: {str(e)}")

# Pokémon model
class Pokemon(BaseModel):
    Image: str
    Index: int
    Name: str
    Type_1: str
    Type_2: Optional[str] = None
    Total: int
    HP: int
    Attack: int
    Defense: int
    SP_Atk: int
    SP_Def: int
    Speed: int

@app.get("/data", response_model=List[dict], summary="Retrieve all Pokémon data")
def get_data(sort_by: Optional[str] = None, filter: Optional[str] = None):
    """Fetch Pokémon data from a data source with optional sorting and filtering."""
    df = load_pokemon_data()

    # Apply filtering if provided
    if filter:
        filter_conditions = filter.split("&")
        for condition in filter_conditions:
            field, value = condition.split("=")
            if field in df.columns:
                # Filtering with case-insensitive matching
                df = df[df[field].astype(str).str.lower().str.contains(value.lower())]

    # Apply sorting if provided
    if sort_by:
        sort_columns = sort_by.split(",")
        # Ensure valid columns for sorting
        invalid_columns = [col for col in sort_columns if col not in df.columns]
        if invalid_columns:
            raise HTTPException(status_code=400, detail=f"Invalid sort column(s): {', '.join(invalid_columns)}")
        
        df = df.sort_values(by=sort_columns)

    # Convert the DataFrame to a list of dictionaries and return
    return df.to_dict(orient='records')

@app.post("/data", response_model=Pokemon, summary="Adds a single record")
def add_data(pokemon: Pokemon):
    """Add a single Pokémon record to the dataset."""
    df = load_pokemon_data()
    new_record = pokemon.dict()
    
    # Check for duplicate Index (as ID)
    if new_record['Index'] in df['Index'].values:
        raise HTTPException(status_code=400, detail="A Pokémon with this Index already exists.")
    
    # Append the new record to the DataFrame
    df = df.append(new_record, ignore_index=True)
    df.to_csv('pokedex.csv', index=False)  # Save the updated DataFrame back to the CSV file
    return new_record

