# Pokémon API Projekt

## Om Projektet

Pokémon API-projektet er en simpel web-API bygget med FastAPI og pandas. Den giver brugerne mulighed for at få adgang til en stor samling af Pokémon-data. Med denne API kan brugerne se, sortere, filtrere og tilføje nye Pokémon. Projektet er en nyttig ressource for dem, der ønsker at arbejde med Pokémon-information.

## Nøglefunktioner

1. **Vis Data**: 
   - Endpoint: `GET /data`
   - Henter hele Pokémon-datasættet i JSON-format, så brugerne kan se oplysninger om hver Pokémon.

2. **Sortering**:
   - Endpoint: `GET /data?sort_by=kolonne1,kolonne2`
   - Brugerne kan sortere dataene efter forskellige kolonner, så de kan finde det, de leder efter (f.eks. sortere efter HP eller Angreb).

3. **Filtrering**:
   - Endpoint: `GET /data?filter=felt1=værdi1&felt2=værdi2`
   - API'en gør det muligt for brugerne at filtrere datasættet, så de kun får Pokémon, der matcher deres krav (f.eks. filtrere efter Type).


## Datasæt

Datasættet, der bruges i dette projekt, er en CSV-fil ved navn `pokedex.csv` som jeg hentet fra **Kaggle**, der indeholder vigtige oplysninger om Pokémon, som for eksempel:

- Image
- Index
- Name
- Type 1
- Type 2
- Total
- HP
- Attack
- Defense
- Special Attack (SP. Atk.)
- Special Defense (SP. Def.)
- Speed

## Værktøjer og Teknologier

- **FastAPI**: Et hurtigt webframework til at bygge API'er med Python.
- **Pandas**: Et bibliotek til at arbejde med data i Python. Det bruges til at indlæse og behandle Pokémon-data.
- **Uvicorn**: En server, der kører FastAPI-applikationen lokalt.
- **OpenAPI Specification**: En standard måde at beskrive API'en på, så brugerne kan forstå, hvordan den virker.

## ChatGPT
**Promt**: lave en openapi specifikation som auto genere api koden, api skal have funktionaliteter: vis data, sortering, filtering og tilføj data. her er eksempel data på pokedex.csv datasæt: Image,Index,Name,Type 1,Type 2,Total,HP,Attack,Defense,SP. Atk.,SP. Def,Speed
images/1.png,1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45
images/2.png,2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60
images/3.png,3,Venusaur,Grass,Poison,525,80,82,83,100,100,80
images/4.png,3,Venusaur Mega Venusaur,Grass,Poison,625,80,100,123,122,120,80
images/5.png,4,Charmander,Fire,,309,39,52,43,60,50,65

## Konklusion

Pokémon API-projektet viser, hvordan man bygger en API til at arbejde med Pokémon-data. .
