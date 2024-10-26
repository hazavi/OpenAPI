# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data**](DefaultApi.md#add_data) | **POST** /data/add | Tilføj en ny Pokémon
[**add_multiple_data**](DefaultApi.md#add_multiple_data) | **POST** /data/add_multiple | Tilføj flere Pokémon
[**get_data**](DefaultApi.md#get_data) | **GET** /data | Hent alle Pokémon data
[**get_filtered_data**](DefaultApi.md#get_filtered_data) | **GET** /data/filtered | Hent filtreret Pokémon data
[**get_sorted_data**](DefaultApi.md#get_sorted_data) | **GET** /data/sorted | Hent sorteret Pokémon data


# **add_data**
> AddData200Response add_data(pokemon)

Tilføj en ny Pokémon

### Example


```python
import openapi_client
from openapi_client.models.add_data200_response import AddData200Response
from openapi_client.models.pokemon import Pokemon
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    pokemon = openapi_client.Pokemon() # Pokemon | Data af Pokémon som skal tilføjes

    try:
        # Tilføj en ny Pokémon
        api_response = api_instance.add_data(pokemon)
        print("The response of DefaultApi->add_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pokemon** | [**Pokemon**](Pokemon.md)| Data af Pokémon som skal tilføjes | 

### Return type

[**AddData200Response**](AddData200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pokémon tilføjet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_multiple_data**
> AddMultipleData200Response add_multiple_data(pokemon)

Tilføj flere Pokémon

### Example


```python
import openapi_client
from openapi_client.models.add_multiple_data200_response import AddMultipleData200Response
from openapi_client.models.pokemon import Pokemon
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    pokemon = [openapi_client.Pokemon()] # List[Pokemon] | Liste af Pokémon data som skal tilføjes

    try:
        # Tilføj flere Pokémon
        api_response = api_instance.add_multiple_data(pokemon)
        print("The response of DefaultApi->add_multiple_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_multiple_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pokemon** | [**List[Pokemon]**](Pokemon.md)| Liste af Pokémon data som skal tilføjes | 

### Return type

[**AddMultipleData200Response**](AddMultipleData200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flere Pokémon tilføjet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data**
> List[Pokemon] get_data()

Hent alle Pokémon data

### Example


```python
import openapi_client
from openapi_client.models.pokemon import Pokemon
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Hent alle Pokémon data
        api_response = api_instance.get_data()
        print("The response of DefaultApi->get_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Pokemon]**](Pokemon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON array af alle Pokémon data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_data**
> List[Pokemon] get_filtered_data(name=name, type_1=type_1, type_2=type_2)

Hent filtreret Pokémon data

### Example


```python
import openapi_client
from openapi_client.models.pokemon import Pokemon
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | Filter efter Pokémon navn (optional)
    type_1 = 'type_1_example' # str | Filter efter primær type (optional)
    type_2 = 'type_2_example' # str | Filter efter sekundær type (optional)

    try:
        # Hent filtreret Pokémon data
        api_response = api_instance.get_filtered_data(name=name, type_1=type_1, type_2=type_2)
        print("The response of DefaultApi->get_filtered_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_filtered_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter efter Pokémon navn | [optional] 
 **type_1** | **str**| Filter efter primær type | [optional] 
 **type_2** | **str**| Filter efter sekundær type | [optional] 

### Return type

[**List[Pokemon]**](Pokemon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filtreret Pokémon data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sorted_data**
> List[Pokemon] get_sorted_data(columns)

Hent sorteret Pokémon data

### Example


```python
import openapi_client
from openapi_client.models.pokemon import Pokemon
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    columns = ['columns_example'] # List[str] | Kolonner at sortere efter

    try:
        # Hent sorteret Pokémon data
        api_response = api_instance.get_sorted_data(columns)
        print("The response of DefaultApi->get_sorted_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sorted_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **columns** | [**List[str]**](str.md)| Kolonner at sortere efter | 

### Return type

[**List[Pokemon]**](Pokemon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sorteret Pokémon data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

