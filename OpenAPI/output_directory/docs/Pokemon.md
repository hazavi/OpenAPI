# Pokemon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type_1** | **str** |  | [optional] 
**type_2** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**hp** | **int** |  | [optional] 
**attack** | **int** |  | [optional] 
**defense** | **int** |  | [optional] 
**sp__atk** | **int** |  | [optional] 
**sp__def** | **int** |  | [optional] 
**speed** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.pokemon import Pokemon

# TODO update the JSON string below
json = "{}"
# create an instance of Pokemon from a JSON string
pokemon_instance = Pokemon.from_json(json)
# print the JSON string representation of the object
print(Pokemon.to_json())

# convert the object into a dict
pokemon_dict = pokemon_instance.to_dict()
# create an instance of Pokemon from a dict
pokemon_from_dict = Pokemon.from_dict(pokemon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


